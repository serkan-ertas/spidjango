import sys
import os

from django.shortcuts import render

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from utils.spider import *


def home(request):
    data = {
        'spiders': get_all_spiders()
    }

    return render(request, 'spider/home.html', data)


def about(request):
    return render(request, 'spider/about.html')


def spider(request, spider_name):
    data = {
        'spider_name': spider_name,
    }
    return render(request, 'spider/spider.html', data)
