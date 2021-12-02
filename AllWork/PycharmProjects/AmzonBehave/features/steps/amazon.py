from behave import *
from selenium import webdriver
@given(u'chrome is launched')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path="C:/Software/chromedriver/chromedriver.exe")


@when(u'we navigate to Amazon website')
def step_impl(context):
    context.driver.get("https://www.amazon.in/")


@when(u'we enter product "iphone12" in search bar')
def step_impl(context):
    context.driver.find_element_by_id("twotabsearchtextbox").send_keys("iphone12")




@when(u'we press the search button')
def step_impl(context):
    context.driver.find_element_by_id("nav-search-submit-button").click()


@then(u'we successfully navigate to the product list page')
def step_impl(context):
   context.driver.get("https://www.amazon.in/s?k=iphone12&ref=nb_sb_noss_2")
