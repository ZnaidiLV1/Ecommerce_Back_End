from random import random

from django.shortcuts import render

def generate_six_digit_id():
    return f'{random.randint(100000, 999999)}'
# Create your views here.
