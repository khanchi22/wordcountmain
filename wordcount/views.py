from django.shortcuts import render
from django.http import HttpResponse
import operator

def homepage(request):
    return render(request, 'home.html')

def counting(request):
    textbox = request.GET['textbox']
    wordlist = textbox.split()
    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            #increase
            worddictionary[word] += 1
        else:
            #add to the worddictionary
            worddictionary[word] = 1
        sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'counting.html', {'textbox':textbox,'count':len(wordlist), 'sortedwords':sortedwords})

def about(request):
    return render(request, 'about.html')
