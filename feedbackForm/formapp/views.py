from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .forms import *
from .models import *
import re

# Create your views here.
def feedback(request):
    form = FeedbackForm(request.POST)
    if form.is_valid():
        name = request.POST['name']
        email = request.POST['email']
        title = request.POST['title']
        feed = request.POST['feed']

        mydictionary = {
            "form": FeedbackForm()
        }

        errorflag = False
        errors = []
        regex = '([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'

        if not re.search(regex, email):
            errorflag = True
            errormsg = "Not a valid Email address"
            errors.append(errormsg)

        if errorflag != True:
            mydictionary["success"] = True
            mydictionary["successmsg"] = "Form Submitted"
            print(f"Person name that give feedback: {name}")
            print(f"Email: {email}")
            print(f"Title: {title}")
            print(f"Feedback description: {feed}")

            db_entry = Feedback(name=name, email=email, title=title, feed=feed)
            db_entry.save()


        mydictionary["error"] = errorflag
        mydictionary["errors"] = errors
        return render(request, 'feedback.html', context=mydictionary)



    return render(request, 'feedback.html', {'form': FeedbackForm})
