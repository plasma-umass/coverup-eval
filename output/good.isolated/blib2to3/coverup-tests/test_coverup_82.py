# file src/blib2to3/pytree.py:724-766
# lines [759]
# branches ['754->763']

import pytest
from blib2to3.pytree import WildcardPattern

def test_wildcard_pattern_with_empty_content():
    with pytest.raises(AssertionError):
        WildcardPattern(content=[])

def test_wildcard_pattern_with_empty_alternative():
    with pytest.raises(AssertionError):
        WildcardPattern(content=[[], ['a']])
