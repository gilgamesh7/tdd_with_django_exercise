# from django.test import TestCase

from django.urls import resolve
from django.template.loader import render_to_string
from pytest_django.asserts import assertTemplateUsed
from django.test import Client
from django.http import HttpRequest

from selenium import webdriver

from lists.views import home_page

import pytest

@pytest.fixture(scope='module')
def this_client():
    print("------ setup ------")

    # Open client
    client = Client()

    yield client

    print("------ teardown ------")

def test_root_url_resolves_to_home_page_view():
    found = resolve('/home/')

    assert found.func == home_page

# This does not work with csr Token
# def test_home_page_returns_correct_html_using_render_to_string():
#     response = home_page(HttpRequest())
#     html = response.content.decode('utf-8')

#     expected_html = render_to_string('lists/home.html')

#     assert expected_html == html

def test_home_page_returns_correct_html_using_assertTemplateUsed(this_client):
    response = this_client.get('http://localhost:8000/home/')
    assertTemplateUsed(response, 'lists/home.html')

def test_can_save_a_POST_request(this_client):
    response = this_client.post('/', data={'item_text': 'A new list item'})
    assert 'A new list item' in response.content.decode()


