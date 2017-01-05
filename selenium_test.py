# selenium_test.py

from selenium import webdriver

browser = webdriver.Chrome('chromedriver')
browser.get('http://localhost:8000')

assert 'Django' in browser.title
