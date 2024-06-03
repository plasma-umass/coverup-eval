# file lib/ansible/cli/console.py:121-122
# lines [121, 122]
# branches []

import pytest
from unittest import mock
from ansible.cli.console import ConsoleCLI

@pytest.fixture
def console_cli():
    return ConsoleCLI(args=['test'])

def test_get_names(console_cli):
    # Mocking the dir function to ensure it returns a predictable list
    with mock.patch('ansible.cli.console.dir', return_value=['method1', 'method2']):
        names = console_cli.get_names()
        assert names == ['method1', 'method2']

    # Ensure the original dir function is restored after the test
    assert dir(console_cli) != ['method1', 'method2']
