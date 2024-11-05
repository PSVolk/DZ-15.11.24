from datetime import date
from django.http import HttpResponse


def index(request):
    return HttpResponse('Main')
def news(request):
    return HttpResponse('City News')
def news_(request, wrong):
    return news(request)
def manag(request):
    return HttpResponse('City Managment')
def fact(request):
    return HttpResponse('City Fuck')
def dayofweek(request):
    days = ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье')
    d = date.today().weekday()

    return HttpResponse(days[d])

def calc(request, a, operator, b):
    match operator:
        case '+':
            return HttpResponse(a+b)
        case '-':
            return HttpResponse(a-b)
        case '*':
            return HttpResponse(a*b)
        case 'del':
            return HttpResponse(a/b)
        case _:
            return HttpResponse('error')