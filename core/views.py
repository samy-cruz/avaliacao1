from django.shortcuts import render

def inicio(request):
    return render(request, 'inicio.html')
def quiz(request):
    return render(request, 'quiz.html')
def correcao(request):
    nome = request.POST.get('nome')
    q1 = request.POST.get('q1')
    q2 = request.POST.get('q2')
    q3 = request.POST.get('q3')
    resultado1 = "ACERTOU" if q1 == "b" else "ERROU"
    resultado2 = "ACERTOU" if q2 == "a" else "ERROU"
    resultado3 = "ACERTOU" if q3 == "c" else "ERROU"
    contexto = {
        'nome': nome,
        'resultado1': resultado1,
        'resultado2': resultado2,
        'resultado3': resultado3,
    }
    return render(request, 'correcao.html', contexto)