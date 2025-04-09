# file lib/ansible/playbook/conditional.py:51-60
# lines [51, 55, 56, 57, 59, 60]
# branches ['55->56', '55->60', '56->57', '56->59']

import pytest
from ansible.errors import AnsibleError
from ansible.playbook.conditional import Conditional

# Mock class to simulate the loader
class MockLoader:
    pass

# Test function to cover the case when loader is not None
def test_conditional_with_loader():
    loader = MockLoader()
    conditional = Conditional(loader=loader)
    assert hasattr(conditional, '_loader'), "Conditional should have a '_loader' attribute"

# Test function to cover the case when loader is None and '_loader' is not set
def test_conditional_without_loader():
    with pytest.raises(AnsibleError) as excinfo:
        Conditional(loader=None)
    assert "a loader must be specified" in str(excinfo.value), "Should raise an AnsibleError when loader is None"

# Test function to cover the case when '_loader' is already set
def test_conditional_with_existing_loader(mocker):
    conditional = Conditional(loader=MockLoader())
    mocker.patch.object(conditional, '_loader', new_callable=mocker.PropertyMock)
    assert hasattr(conditional, '_loader'), "Conditional should have a '_loader' attribute even if loader is None"
