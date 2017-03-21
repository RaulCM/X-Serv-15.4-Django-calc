from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def suma(request, op1, op2):
    return HttpResponse("<h1>" + op1 + "+" + op2 + "=" +
                        str(int(op1) + int(op2)) + "</h1>")


def resta(request, op1, op2):
    return HttpResponse("<h1>" + op1 + "-" + op2 + "=" +
                        str(int(op1) - int(op2)) + "</h1>")


def multiplicacion(request, op1, op2):
    return HttpResponse("<h1>" + op1 + "*" + op2 + "=" +
                        str(int(op1) * int(op2)) + "</h1>")


def division(request, op1, op2):
    return HttpResponse("<h1>" + op1 + "/" + op2 + "=" +
                        str(int(op1) / int(op2)) + "</h1>")
