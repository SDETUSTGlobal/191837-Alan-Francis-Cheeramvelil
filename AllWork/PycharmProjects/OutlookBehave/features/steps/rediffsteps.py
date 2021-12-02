from behave import *
from selenium import webdriver
@given(u'chrome is launched')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path="C:/Software/chromedriver/chromedriver.exe")


@when(u'we navigate to Rediff website')
def step_impl(context):
    context.driver.get("https://mypage.rediff.com/login/dologin")


@when(u'we enter username "afc2702@gmail.com" password "test"')
def step_impl(context):
    context.driver.find_element_by_id("txtlogin").send_keys("afc2702@gmail.com")
    context.driver.find_element_by_id("pass_box").send_keys("test")


@when(u'we press the login button')
def step_impl(context):
   context.driver.find_element_by_xpath("/html/body/div[3]/div[5]/div[1]/form/div[2]/input[3]").click()


@then(u'we successfully navigate tologin incorrect page')
def step_impl(context):
    context.driver.get("https://mypage.rediff.com/login/dologin")
