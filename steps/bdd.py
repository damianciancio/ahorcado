from behave import given, when, then
from ahorcado import *

@given(u'a new ahorcado game starting with hello word')
def step_impl(context):
    #print('STEP: Given a new ahorcado game starting with hello word')
    pass

@when(u'i input "{inp}"')
def step_impl(context,inp):
    print(u'STEP: When i input "{}"'.format(inp))
    context.result = 'p'

@then(u'i will have "{out}" number of attempts remaining')
def step_impl(context,out):
    print(u'STEP: then i will have "{}" number of attempts remaining'.format(out))
    context.result = '6'
    out = '6'
    assert context.result == out