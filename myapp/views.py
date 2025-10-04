from django.http import HttpResponse
import datetime

from django.shortcuts  import render


def home(request):
    now = datetime.datetime.now()
    # return HttpResponse(f"<H1>Hello this is index page.</H1>" + str(now))
    check = request.GET.get("check")
    if request.method == "POST":
        check = request.POST.get("check")
        print(check)
    isActive = True
    name = "coding from youtube"
    list_of_program = ['WAP to print even numbers', 'WAP to print odd numbers', 'WAP to print prime numbers']
    student = {
        'student_name': "Sunny Shah",
        'student_age': 24,
        'student_city': "Ahmedabad",
        'student_college': "GEC",
        'student_degree': "B.E",
        'student_branch': "Computer Engineering",
    }
    data = {
        "isActive": isActive,
        "name": name,
        "list_of_program": list_of_program,
        "student": student,
        "now": now,
    }
    return render(request, "home.html", data)

def about(request):
    # return HttpResponse(f"<H1>Hello this is about page.</H1>")
    return render(request, "about.html", {
        "title": "About Page",
        "message": "Your application description page.",
    })
def service(request):
    # return HttpResponse(f"Hello this is service page.")
    return render(request, "services.html", {
        "title": "Services Page",
        "message": "Your application services page.",
    })
