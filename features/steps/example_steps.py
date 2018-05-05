# -- FILE: features/steps/example_steps.py
from behave import given, when, then, step
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()

@given('I fire up a web browser')
def step_impl(context):
    driver.get("http://www.python.org")
    assert "Python" in driver.title

@when('I hit the keys')
def step_impl(context):  # -- NOTE: number is converted into integer
    elem = driver.find_element_by_name("q")
    elem.clear()
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source

@then('its all ok')
def step_impl(context):
    driver.close()

@given('we have behave installed')
def step_impl(context):
    pass

@when('we implement {number:d} tests')
def step_impl(context, number):  # -- NOTE: number is converted into integer
    assert number > 1 or number == 0
    context.tests_count = number

@then('behave will test them for us!')
def step_impl(context):
    assert context.failed is False
    assert context.tests_count >= 0