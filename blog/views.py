from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

dummy_posts =[
    {
        'author': 'Money Mase',
        'book_title' : 'manchester',
        'content': 'i love chelsea, i lied',
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
    return render(requests, 'blog\home.html')

def about(requests):
    return render(requests, 'about.html')