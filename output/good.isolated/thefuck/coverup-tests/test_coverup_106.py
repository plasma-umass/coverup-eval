# file thefuck/shells/generic.py:76-77
# lines [76, 77]
# branches []

import pytest
from thefuck.shells.generic import Generic

def test_or_method():
    shell = Generic()
    assert shell.or_('echo "hello"', 'echo "world"') == 'echo "hello" || echo "world"'
    assert shell.or_('false', 'echo "fallback"') == 'false || echo "fallback"'
    assert shell.or_() == ''
