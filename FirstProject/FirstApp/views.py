from django.shortcuts import render
from django.http import HttpResponse;

# Create your views here.
def display(request):
    ss="<h2>Hello User, Welcome to Django First-Project First-App</h2>";
    return HttpResponse(ss);

def show(request):
    ss = "<center> \
            <h1>Welcome to DJANGO HTML webpage</h1> \
            <hr color='brown' width='95%/'> \
            <h2>Welcome to DJANGO HTML webpage</h2> \
            <hr color='brown' width='95%/'> \
            <h3>Welcome to DJANGO HTML webpage</h3> \
            <hr color='brown' width='95%/'> \
            <h4>Welcome to DJANGO HTML webpage</h4> \
            <hr color='brown' width='95%/'> \
            <h5>Welcome to DJANGO HTML webpage<h5> \
            <hr color='brown' width='95%/'> \
            <h6>Welcome to DJANGO HTML webpage<h6> \
            <hr color='brown' width='95%/'> \
    </center>";
    return HttpResponse(ss);

def demo(request):
    htmldata="<center> \
        <h1>Welcome Demo User..!!</h2> \
        <hr/> \
        <h2>This is same output for different requests</h2> \
        <hr/> \
        <h3>Have a Great Day<h3> \
    </center>";
    return HttpResponse(htmldata);
    
def homepage(request):
    htmldata="<center> \
        <h1>Welcome Home-page..!!</h2> \
        <hr/> \
        <h2>Your Request Page is Not-Found...</h2> \
        <hr/> \
        <h3>Try other URL or Links!!!<h3> \
    </center>";
    return HttpResponse(htmldata);
    
  
