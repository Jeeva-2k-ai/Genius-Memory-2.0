from django.shortcuts import render, redirect
from django.http import JsonResponse
import random

def game1(request):
    # Define syntax error questions related to various languages
    questions = [
        {
            "question": "What is wrong with this code? <br><code>console.log('Hello World';</code>",
            "correctCode": "console.log('Hello World');",
            "error": "Missing closing parenthesis"
        },
        {
            "question": "What is wrong with this code? <br><code>let 1variable = 10;</code>",
            "correctCode": "let variable1 = 10;",
            "error": "Variable name cannot start with a number"
        },
        {
            "question": "What is wrong with this code? <br><code>if (x == 5) { console.log('Equal'); }</code>",
            "correctCode": "if (x === 5) { console.log('Equal'); }",
            "error": "Using == instead of === for strict comparison"
        },
        {
            "question": "What is wrong with this Python code? <br><code>for i in range(0,5) print(i)</code>",
            "correctCode": "for i in range(0,5): print(i)",
            "error": "Missing colon (:) at the end of the for loop declaration."
        },
        {
            "question": "What is wrong with this Java code? <br><code>System.out.println('Hello World');</code>",
            "correctCode": "System.out.println('Hello World');",
            "error": "Incorrect quote used, should be double quotes in Java"
        }
    ]
    
    # Randomly shuffle questions for variety
    random.shuffle(questions)

    # Initialize score and current question index
    score = 0
    current_question_index = 0

    context = {
        'questions': questions,
        'score': score,
        'current_question_index': current_question_index,
    }

    return render(request, 'game_page1.html', context)

def ins1(request):
    return render(request, 'instruction1.html')

def count1(request):
    return render(request, 'countdown1.html')
