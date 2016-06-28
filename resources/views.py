from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    variables = {
        'course_name': 'Python e Django na Pratica',
        'alunos_list':[
            {
                'name': 'João'
            },
            {
                'name': 'Maria'
            },
            {
                'name': 'João'
            }
        ]
    }

    return render(request, "hello.html", variables)
