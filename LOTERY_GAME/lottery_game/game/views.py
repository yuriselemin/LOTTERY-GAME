from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Counter
import random

def home(request):
    return render(request, 'game/home.html')

def generate_numbers(request):
    # Получаем или создаем счетчик
    counter, created = Counter.objects.get_or_create(id=1)
    counter.value += 1
    counter.save()

    # Генерация чисел
    if counter.value % 10 == 0:
        number = random.randint(1, 100)
        numbers = [number, number, number]
        message = "Вы выиграли!"
    else:
        numbers = [random.randint(1, 100) for _ in range(3)]
        message = "Попробуйте еще раз."

    # Обнуляем счетчик после 10-го запуска
    if counter.value % 10 == 0:
        counter.value = 0
        counter.save()

    return JsonResponse({'numbers': numbers, 'message': message})
