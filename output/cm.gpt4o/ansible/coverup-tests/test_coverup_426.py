# file lib/ansible/playbook/conditional.py:51-60
# lines [51, 55, 56, 57, 59, 60]
# branches ['55->56', '55->60', '56->57', '56->59']

import pytest
from ansible.errors import AnsibleError
from ansible.playbook.conditional import Conditional

def test_conditional_no_loader():
    with pytest.raises(AnsibleError, match=r"a loader must be specified when using Conditional\(\) directly"):
        Conditional()

def test_conditional_with_loader(mocker):
    mock_loader = mocker.Mock()
    cond = Conditional(loader=mock_loader)
    assert cond._loader == mock_loader
