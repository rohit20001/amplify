from django.shortcuts import render

# Create your views here.
def page1(request):
    return render(request, 'tmp/page1.html')
