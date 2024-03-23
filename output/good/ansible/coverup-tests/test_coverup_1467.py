# file lib/ansible/playbook/conditional.py:51-60
# lines []
# branches ['55->60']

import pytest
from ansible.errors import AnsibleError
from ansible.playbook.conditional import Conditional

class MockLoader:
    pass

def test_conditional_without_loader_raises_error():
    with pytest.raises(AnsibleError) as excinfo:
        Conditional()
    assert "a loader must be specified when using Conditional() directly" in str(excinfo.value)

def test_conditional_with_loader_sets_loader():
    loader = MockLoader()
    conditional = Conditional(loader=loader)
    assert hasattr(conditional, '_loader')
    assert conditional._loader is loader

def test_conditional_inheritance_without_loader():
    class MockPlaybookBase:
        def __init__(self):
            self._loader = MockLoader()
            super(MockPlaybookBase, self).__init__()

    class MockPlaybook(MockPlaybookBase, Conditional):
        pass

    playbook = MockPlaybook()
    assert hasattr(playbook, '_loader')
    assert isinstance(playbook._loader, MockLoader)
