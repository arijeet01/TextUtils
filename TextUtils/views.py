
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
     
     return render(request,'index.html')


def analyze(request):
     djtext = (request.POST.get('text', 'default'))
     removepunc = (request.POST.get('removepunc', 'off'))
     fullcaps = (request.POST.get('fullcaps', 'off'))
     newlineremover = (request.POST.get('newlineremover', 'off'))
     spaceremover = (request.POST.get('spaceremover', 'off'))
     charcounter= (request.POST.get('charcounter', 'off'))
     
     if removepunc == "on":
          punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
          analyzed= ""
          for char in djtext:
               if char not in punctuations:
                    analyzed=analyzed+char
               
          params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
          djtext=analyzed

     if fullcaps == "on":
          analyzed=""
          for char in djtext:
               analyzed=analyzed+char.upper()
          params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
          djtext=analyzed
     
     if  newlineremover=="on":
          analyzed=""
          for char in djtext:
               if char !="\n" and char!="\r":
                    analyzed=analyzed+char
          params = {'purpose': 'Newlines Removed', 'analyzed_text': analyzed}
          djtext=analyzed
               
     if spaceremover=="on":
          djtext=djtext+" "
          analyzed=""
          for index, char in enumerate(djtext):
               if  index+1<len(djtext) and not(djtext[index]==" " and djtext[index+1]==" "):
                    analyzed=analyzed+char
          params = {'purpose': 'Extra Spaces Removed', 'analyzed_text': analyzed}
          djtext=analyzed
          
     if charcounter=="on":
          analyzed=""
          for char in djtext:
               if char!=" ":
                    analyzed=analyzed+char
          
          params = {'purpose': 'Number of Characters(excluding spaces)', 'analyzed_text': len(analyzed)}
          djtext=analyzed
               
     if removepunc != "on" and fullcaps != "on" and  newlineremover!="on" and spaceremover!="on" and charcounter!="on":
          return HttpResponse("Error!! PLEASE SELECT ANY OPERATION AND TRY AGAIN!!")

     return render(request,'analyze.html',params)
     
def about(request):
    return render(request,'about.html')

def contact(request):
     return render(request,'contact.html')     
