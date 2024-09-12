# file: flutils/strutils.py:81-97
# asked: {"lines": [81, 97], "branches": []}
# gained: {"lines": [81, 97], "branches": []}

import pytest
from flutils.strutils import camel_to_underscore

def test_camel_to_underscore():
    assert camel_to_underscore('FooBar') == 'foo_bar'
    assert camel_to_underscore('fooBarBaz') == 'foo_bar_baz'
    assert camel_to_underscore('fooBARBaz') == 'foo_bar_baz'
    assert camel_to_underscore('foo') == 'foo'
    assert camel_to_underscore('Foo') == 'foo'
    assert camel_to_underscore('fooBar1Baz') == 'foo_bar1_baz'
    assert camel_to_underscore('foo1BarBaz') == 'foo1_bar_baz'
    assert camel_to_underscore('foo1barBaz') == 'foo1bar_baz'
