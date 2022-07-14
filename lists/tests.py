# from django.test import TestCase

from django.urls import resolve
from lists.views import home_page

import pytest

def test_root_url_resolves_to_home_page_view():
    found = resolve('/home/home/')
    print(found.func)
    assert found.func == home_page