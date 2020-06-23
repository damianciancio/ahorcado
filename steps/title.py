from behave import given, when, then
from ahorcado import *

@given('a new hanged game')

@when('i enter the browser')
def step(context):
   context.browser.get('http://127.0.0.1:5000/')

@then('Then i should have title "Ahorcado" ')
def step(context):
   assert context.browser.title == "Ahorcado"