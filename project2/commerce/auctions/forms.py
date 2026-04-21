from django import forms
from .models import Listing,Bid,Comment

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'starting_bid', 'category', 'image']
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'Starting_bid': forms.NumberInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['bid_amount']
        widgets = {
            'bid_amount': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Bid Amount'})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        widgets = {
            'comment': forms.NumberInput(attrs={'class': 'form-control'})
        }