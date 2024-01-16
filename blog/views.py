from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

posts =[
    {
        'author': 'Redice Studio',
        'book_title' : '5G Internet',
        'content': '5G internet, the fifth generation of mobile networks, delivers blazing-fast speeds, ultra-low latency, and enhanced connectivity. With data rates surpassing its predecessors, 5G empowers seamless streaming, rapid downloads, and supports the burgeoning Internet of Things (IoT), ushering in a new era of high-speed, responsive wireless communication.',
        'date_posted': '10 January,2024'
        
    },
    
        {
        'author': 'Kara Chambers',
        'book_title' : 'Web Development',
        'content': 'Web development is the art and science of creating websites and web applications. It involves designing, coding, and maintaining digital interfaces that users interact with. From front-end design for a visually appealing experience to back-end development for functionality, web development plays a crucial role in shaping the online world we navigate every day.',
        'date_posted': '16 December,2023'
        
    },
        
        {
        'author': 'Muyiwa Obaremi',
        'book_title' : 'Misfit of Students',
        'content': 'The misfit of students refers to individuals who may feel disconnected or out of sync with the mainstream academic environment. Whether due to unique learning styles, diverse interests, or unconventional approaches, addressing the needs of misfit students involves fostering inclusive educational spaces that cater to diverse talents and learning pathways, ensuring each student can thrive in their own way.',
        'date_posted': '1 January,2024'
        }
]


def home(requests):
    context = {
        'posts':posts
    }    
    return render(requests, 'blog\home.html', context)

def about(requests):
    return render(requests, 'about.html',{'title':'About'})