from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


import pytest
import time

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
    browser.get("http://localhost:8000/home/")



    # She checks the page title to ensure it has "To-Do" in it
    assert 'To-Do' in browser.title

    # She notices that the head line mentions To-Do lists
    assert 'To-Do' in browser.find_element(By.TAG_NAME,'h1').text

    # She is invited to enter a To-Do item
    assert 'Enter a to-do item' in browser.find_element(By.ID,'id_new_item').get_attribute('placeholder')

    # She types "Buy peacock feathers"
    # She hits enter. Page updates. Displays "1: Buy peacock feathers" as an item.
    browser.find_element(By.ID,'id_new_item').send_keys('Buy peacock feathers')
    browser.find_element(By.ID,'id_new_item').send_keys(Keys.ENTER)
    time.sleep(2)

    table = browser.find_element(By.ID,'id_list_table')
    rows = table.find_elements(By.TAG_NAME,'tr') 

    assert any(row.text == '1: Buy peacock feathers' for row in rows) == True

    # She enters "Use peacock feather to make a fly" in the text box that displays for this.

    # She checks if the page shows both items on the list

    # She sees the explnatory text that shows the unique URL generated for her

    # She visits the URL to check if the to do items are still there



