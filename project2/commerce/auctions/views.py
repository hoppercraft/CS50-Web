from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import ListingForm,BidForm
from .models import User,Listing,Bid
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.db.models import Max
def index(request):
    listings=Listing.objects.all()
    for listing in listings:
        highest_bid = listing.bids.aggregate(Max("bid_amount"))["bid_amount__max"] 
        if highest_bid:
            listing.starting_bid=highest_bid
    return render(request, "auctions/index.html",{
        "listings":listings
    })

@login_required
def createlisting(request):
    if request.method == "POST":
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            new_listing = form.save(commit=False)
            new_listing.owner = request.user
            new_listing.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form = ListingForm()

    return render(request, "auctions/createlisting.html", {
        "form": form
    })
    

def login_view(request):
    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.POST.get('next')
            if next_url:
                return HttpResponseRedirect(next_url)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required
def listing_page(request,listing_id):
    listing=get_object_or_404(Listing, pk=listing_id)
    highest_bid_obj = listing.bids.order_by('-bid_amount').first()
    highest_bid = listing.starting_bid
    highest_bidder = None
    if highest_bid_obj:
        highest_bid = highest_bid_obj.bid_amount
        highest_bidder = highest_bid_obj.bidder
    total_bids = listing.bids.count()
    if highest_bid_obj:
        listing.starting_bid=highest_bid
    else:
        highest_bid=listing.starting_bid

    if request.method == 'POST':
        form = BidForm(request.POST)
        if form.is_valid():
            new_bid = form.save(commit=False)
            if new_bid.bid_amount > highest_bid:
                new_bid.bidder = request.user
                new_bid.bid_item = listing
                new_bid.save()
                return HttpResponseRedirect(reverse("listing", args=(listing_id,)))
            else:
                form.add_error('bid_amount', f"Must be higher than ${highest_bid}")
    else:
        form = BidForm()
    
    return render(request, "auctions/listing.html",{
        "listing":listing,
        "highest_bid":highest_bid,
        "total_bids":total_bids,
        "form": form,
        "highest_bidder":highest_bidder
    })