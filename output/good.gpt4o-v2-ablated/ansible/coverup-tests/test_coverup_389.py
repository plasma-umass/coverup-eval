# file: lib/ansible/modules/pip.py:310-312
# asked: {"lines": [310, 312], "branches": []}
# gained: {"lines": [310, 312], "branches": []}

import pytest

def test_is_package_name():
    from ansible.modules.pip import _is_package_name

    # Mocking op_dict to ensure the test is self-contained
    op_dict = {'==': 'equal', '>=': 'greater_equal', '<=': 'less_equal'}

    # Test cases
    test_cases = [
        ("package_name", True),
        ("==1.0.0", False),
        (">=2.0.0", False),
        ("<=3.0.0", False),
        ("  ==1.0.0", False),
        ("  package_name", True),
    ]

    for name, expected in test_cases:
        assert _is_package_name(name) == expected

@pytest.fixture(autouse=True)
def mock_op_dict(monkeypatch):
    monkeypatch.setattr('ansible.modules.pip.op_dict', {'==': 'equal', '>=': 'greater_equal', '<=': 'less_equal'})
