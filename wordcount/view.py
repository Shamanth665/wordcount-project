from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import operator

def Home(request):
	# To simply display the text in browser we use --> HttpResponse()
	#return HttpResponse('Home Page')
	
	
	# To redirect the page to prticular website/url we use --->  HttpResponseRedirect()
	#return HttpResponseRedirect("https://www.w3schools.com/")
	
	
	# To render the entire Html page we use  -->   render()
	return render(request,"Home.html",{'fName':'Shamanth'})
	
def shamDetails(request):
	return HttpResponse("<span style='color:orange;font-weight:bold'>Shamanth</span> is a good person")
	

def countWords(request):
	fullText = request.GET['txtDesc']
	wordsList = fullText.split()
	countlist = {}
	
	for w in wordsList:
		if w in countlist:
			countlist[w] += 1
		else:
			countlist[w] = 1
	
	return render(request,"count.html",{'fullText':fullText,'totalCount' : len(wordsList), 'wordCount':sorted(countlist.items(), key = operator.itemgetter(0))})

	
def gotoAboutPage(request):
	return render(request, "about.html")