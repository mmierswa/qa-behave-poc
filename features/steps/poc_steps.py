from behave import *

@given(u'I visit the Feedback Genius page')
def step_impl(context):
    context.browser.get("https://www.feedbackgenius.com/")

@then(u'the title should say "{title}"')
def step_impl(context,title):
    assert context.browser.title == title

@given('we have behave installed')
def step_impl(context):
    pass

@when('we implement a test')
def step_impl(context):
    assert True is not False

@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False

@then('the result page will include "{text}"')
def step_impl(context, text):
    if text not in context.response:
        fail('%r not in %r' % (text, context.response))
