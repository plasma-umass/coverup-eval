# file: lib/ansible/playbook/conditional.py:51-60
# asked: {"lines": [51, 55, 56, 57, 59, 60], "branches": [[55, 56], [55, 60], [56, 57], [56, 59]]}
# gained: {"lines": [51, 55, 56, 57, 59, 60], "branches": [[55, 56], [55, 60], [56, 57], [56, 59]]}

import pytest
import re
from ansible.errors import AnsibleError
from ansible.playbook.conditional import Conditional

def test_conditional_init_with_loader(mocker):
    mock_loader = mocker.Mock()
    conditional = Conditional(loader=mock_loader)
    assert conditional._loader == mock_loader

def test_conditional_init_without_loader_raises_error():
    with pytest.raises(AnsibleError, match=re.escape("a loader must be specified when using Conditional() directly")):
        Conditional(loader=None)

def test_conditional_init_with_existing_loader_attribute(mocker):
    class MockBase:
        _loader = "existing_loader"
    
    class TestConditional(MockBase, Conditional):
        def __init__(self, loader=None):
            Conditional.__init__(self, loader=loader)
    
    mock_loader = mocker.Mock()
    test_conditional = TestConditional(loader=mock_loader)
    assert test_conditional._loader == "existing_loader"
