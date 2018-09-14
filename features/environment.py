from behave import fixture, use_fixture
#from behave4my_project.fixtures import wsgi_server
# from selenium import webdriver
from nerodia.browser import Browser

@fixture
def selenium_browser_chrome(context):
    # -- HINT: @behave.fixture is similar to @contextlib.contextmanager
    # context.browser = Browser(browser='chrome')
    # yield context.browser
    # -- CLEANUP-FIXTURE PART:
    # context.browser.close()

def before_all(context):
    context.browser = Browser(browser='chrome')
    yield context.browser

def after_all(context):
    context.browser.close()

#example hooks:
# def before_step(context, step)
# def after_step(context, step)
# def before_scenario(context, scenario)
# def after_scenario(context, scenario)
# def before_feature(context, feature)
# def after_feature(context, feature)
# def before_tag(context, tag)
# def after_tag(context, tag)
# def before_all(context)
# def after_all(context)
