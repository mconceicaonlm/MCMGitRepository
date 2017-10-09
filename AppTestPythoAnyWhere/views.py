from django.shortcuts import render

#https://www.youtube.com/watch?v=3tf8XlhsQAo

def Inicio (request):
    return render (request, 'home.html')

def contact (request):
    return render (request, 'basic.html',{'content':['Pode o usar o endereço: comprasdasao@outlook.com', 'ou prencher o formulário abaixo']})


