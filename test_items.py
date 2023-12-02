import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_button_add_to_basket(browser):

    link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    assert browser.find_element(By.XPATH, '//form[@id="add_to_basket_form"]//button[@type="submit"]'), 'not found'
    print('asdfasdfasd')