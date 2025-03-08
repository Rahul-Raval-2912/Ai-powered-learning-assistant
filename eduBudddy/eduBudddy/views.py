from django.shortcuts import redirect,render

def HOME(request):
    return render(request,'main/index.html')


def DASHBOARD(request):
    return render(request, 'main/dashboard.html')


def QA(request):
    return render(request,'dashItems/qa.html')


def SM(request):
    return render(request,'dashItems/sm.html')


def QUIZ(request):
    return render(request,'dashItems/quiz.html')