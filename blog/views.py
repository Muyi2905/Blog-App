from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts =[
    {
        'author': 'Redice',
        'book_title' : 'Solo Levelling',
        'content': 'Hunter Sung-jun woo',
        'date_posted': '10 January,2024'
        
    },
    
        {
        'author': 'George. R.R Martin',
        'book_title' : 'Game of Thrones',
        'content': 'House Lannister',
        'date_posted': '16 March,1997'
        
    },
]


def home(requests):
    context = {
        'posts':posts
    }    
    return render(requests, 'blog\home.html', context)

def about(requests):
    return render(requests, 'about.html')