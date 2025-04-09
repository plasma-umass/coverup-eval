# file: lib/ansible/playbook/conditional.py:51-60
# asked: {"lines": [51, 55, 56, 57, 59, 60], "branches": [[55, 56], [55, 60], [56, 57], [56, 59]]}
# gained: {"lines": [51, 55, 56, 57, 59, 60], "branches": [[55, 56], [55, 60], [56, 57], [56, 59]]}

import pytest
from ansible.errors import AnsibleError
from ansible.playbook.conditional import Conditional

def test_conditional_no_loader():
    with pytest.raises(AnsibleError, match=r"a loader must be specified when using Conditional\(\) directly"):
        Conditional()

def test_conditional_with_loader():
    class MockLoader:
        pass

    loader = MockLoader()
    cond = Conditional(loader=loader)
    assert cond._loader is loader

def test_conditional_as_mixin():
    class MockBase:
        def __init__(self):
            self._loader = "existing_loader"

    class MockConditional(MockBase, Conditional):
        def __init__(self, loader=None):
            MockBase.__init__(self)
            Conditional.__init__(self, loader=loader)

    mock_conditional = MockConditional()
    assert mock_conditional._loader == "existing_loader"
