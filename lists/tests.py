# from django.test import TestCase

from django.urls import resolve
from lists.views import home_page

import pytest

from django.http import HttpRequest

def test_root_url_resolves_to_home_page_view():
    found = resolve('/home/home/')
    print(found.func)
    assert found.func == home_page

def test_home_page_returns_correct_html():
    response = home_page(HttpRequest())
    html = response.content.decode('utf-8')

    print(f"----- {html} -----")
    assert '<title>To-Do lists</title>' in html