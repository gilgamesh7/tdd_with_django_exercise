# from django.test import TestCase

from django.urls import resolve
from django.template.loader import render_to_string
from pytest_django.asserts import assertTemplateUsed
from django.test import Client
from django.http import HttpRequest

from selenium import webdriver

from lists.views import home_page

def test_root_url_resolves_to_home_page_view():
    found = resolve('/home/')

    assert found.func == home_page

def test_home_page_returns_correct_html_using_render_to_string():
    response = home_page(HttpRequest())
    html = response.content.decode('utf-8')

    expected_html = render_to_string('lists/home.html')

    assert expected_html == html

def test_home_page_returns_correct_html_using_assertTemplateUsed():
    client = Client()
    response = client.get('http://localhost:8000/home/')
    assertTemplateUsed(response, 'lists/home.html')


