# file youtube_dl/jsinterp.py:31-36
# lines []
# branches ['32->34']

import pytest
from youtube_dl.jsinterp import JSInterpreter

def test_js_interpreter_init_with_none_objects():
    # Test initialization with objects set to None
    code = "var test = 5;"
    interpreter = JSInterpreter(code, objects=None)
    assert interpreter.code == code
    assert interpreter._functions == {}
    assert interpreter._objects == {}

def test_js_interpreter_init_with_custom_objects():
    # Test initialization with custom objects
    code = "var test = 5;"
    custom_objects = {'custom': 'object'}
    interpreter = JSInterpreter(code, objects=custom_objects)
    assert interpreter.code == code
    assert interpreter._functions == {}
    assert interpreter._objects == custom_objects
