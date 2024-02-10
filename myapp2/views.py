from django.shortcuts import render
from django.http import HttpResponse
import logging
# Create your views here.

logger = logging.getLogger(__name__)


def logger_deco(funk):
    def wrapper(*args, **kwargs):
        request = args[0]
        logger.info(f"Посещена страница: {request.path}")
        return funk(*args, **kwargs)
    return wrapper


@logger_deco
def home(request):
    home_html = """
    <h1>Добро пожаловать на мой 2 сайт!</h1>
    <p>Здесь вы не найдете никакого контента.</p>
    """
    return render(request, 'home.html', {'content': home_html})


@logger_deco
def about(request):
    about_html = """
    <h1>Обо мне</h1>
    <p>здесь много информации обо мне 2</p>
    """
    return render(request, 'about.html', {'content': about_html})
