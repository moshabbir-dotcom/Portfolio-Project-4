from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')


def contact(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        return render(request, 'contact.html', {'fname': fname})

    else:
        return render(request, 'contact.html')

