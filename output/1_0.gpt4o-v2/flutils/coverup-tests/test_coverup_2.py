# file: flutils/strutils.py:212-236
# asked: {"lines": [212, 214, 233, 234, 235, 236], "branches": [[234, 235], [234, 236]]}
# gained: {"lines": [212, 214, 233, 234, 235, 236], "branches": [[234, 235], [234, 236]]}

import pytest
from flutils.strutils import underscore_to_camel

def test_underscore_to_camel_lower_first_true():
    assert underscore_to_camel('foo_bar') == 'fooBar'
    assert underscore_to_camel('_one__two___') == 'oneTwo'
    assert underscore_to_camel('') == ''
    assert underscore_to_camel('a_b_c') == 'aBC'

def test_underscore_to_camel_lower_first_false():
    assert underscore_to_camel('foo_bar', lower_first=False) == 'FooBar'
    assert underscore_to_camel('_one__two___', lower_first=False) == 'OneTwo'
    assert underscore_to_camel('', lower_first=False) == ''
    assert underscore_to_camel('a_b_c', lower_first=False) == 'ABC'
