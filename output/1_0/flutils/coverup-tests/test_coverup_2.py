# file flutils/strutils.py:81-97
# lines [81, 97]
# branches []

import re
import pytest
from flutils.strutils import camel_to_underscore

_CAMEL_TO_UNDERSCORE_RE = re.compile(r'(?<!^)(?=[A-Z])')

def test_camel_to_underscore():
    # Test with a single uppercase letter at the beginning
    assert camel_to_underscore('Foo') == 'foo'
    # Test with a single uppercase letter in the middle
    assert camel_to_underscore('fooBar') == 'foo_bar'
    # Test with multiple uppercase letters in the middle
    assert camel_to_underscore('fooBarBaz') == 'foo_bar_baz'
    # Test with no uppercase letters
    assert camel_to_underscore('foobar') == 'foobar'
    # Test with all uppercase letters
    assert camel_to_underscore('FOOBAR') == 'foobar'
    # Test with an empty string
    assert camel_to_underscore('') == ''
    # Test with a string that starts with an underscore
    assert camel_to_underscore('_fooBar') == '_foo_bar'
    # Test with a string that ends with an uppercase letter
    assert camel_to_underscore('fooBarZ') == 'foo_bar_z'
    # Test with a string that has an uppercase letter following a non-letter character
    assert camel_to_underscore('foo_Bar') == 'foo__bar'
    # Test with a string that has an uppercase letter following a number
    assert camel_to_underscore('foo2Bar') == 'foo2_bar'
