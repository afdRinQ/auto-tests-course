from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x1_element = browser.find_element_by_id("num1")
    x2_element = browser.find_element_by_id("num2")
    x1 = x1_element.text
    x2 = x2_element.text
    y = int(x2) + int(x1)
    y2 = str(y)
    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(y2)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
