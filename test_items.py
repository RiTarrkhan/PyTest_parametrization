import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(30)
    res_test =  browser.find_elements(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket") 
    assert res_test, "button doesn't exist"
    
