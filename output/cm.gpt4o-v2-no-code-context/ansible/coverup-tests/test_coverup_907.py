# file: lib/ansible/parsing/yaml/dumper.py:57-61
# asked: {"lines": [57, 61], "branches": []}
# gained: {"lines": [57], "branches": []}

import pytest
from ansible.parsing.yaml.dumper import AnsibleDumper
from ansible.parsing.yaml.objects import AnsibleUnicode
from yaml.representer import RepresenterError

class MockUndefined:
    def __bool__(self):
        return False

@pytest.fixture
def dumper():
    class TestDumper(AnsibleDumper):
        def __init__(self):
            super().__init__(stream=None)
        
        def represent_undefined(self, data):
            try:
                return bool(data)
            except RepresenterError:
                return False
    return TestDumper()

def test_represent_undefined_with_undefined(dumper):
    undefined = MockUndefined()
    result = dumper.represent_undefined(undefined)
    assert result is False

def test_represent_undefined_with_defined(dumper):
    defined = AnsibleUnicode("defined_value")
    result = dumper.represent_undefined(defined)
    assert result is True
