from selenium import webdriver

import pytest

@pytest.fixture(scope='module')
def browser():
    print("------ setup ------")

    # Open browser
    browser = webdriver.Firefox()

    yield browser

    print("------ teardown ------")

    # Close browser
    browser.quit()

def test_can_start_a_list_and_retrieve_it_later(browser):
    # Edith heard about te app. She opens it in her browser.
    browser.get("http://localhost:8000")

    # She checks the page title to ensure it has "To-Do" in it
    assert 'To-Do' in browser.title

    # She is invited to enter a To-Do item

    # She types "Buy peacock feathers"

    # She hits enter. Page updates. Displays "1: Buy peacock feathers" as an item.

    # She enters "Use peacock feather to make a fly" in the text box that displays for this.

    # She checks if the page shows both items on the list

    # She sees the explnatory text that shows the unique URL generated for her

    # She visits the URL to check if the to do items are still there



