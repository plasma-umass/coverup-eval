# file: lib/ansible/cli/arguments/option_helpers.py:317-337
# asked: {"lines": [324, 327, 328, 329, 330, 331, 332, 333, 335, 337], "branches": []}
# gained: {"lines": [324, 327, 328, 329, 330, 331, 332, 333, 335, 337], "branches": []}

import pytest
from argparse import ArgumentParser
from ansible.cli.arguments.option_helpers import add_runas_options

def test_add_runas_options(monkeypatch):
    parser = ArgumentParser()
    
    # Mocking constants
    monkeypatch.setattr('ansible.constants.DEFAULT_BECOME', False)
    monkeypatch.setattr('ansible.constants.DEFAULT_BECOME_METHOD', 'sudo')
    monkeypatch.setattr('ansible.constants.DEFAULT_BECOME_USER', 'root')
    
    add_runas_options(parser)
    
    args = parser.parse_args(['-b', '--become-method', 'sudo', '--become-user', 'root'])
    
    assert args.become is True
    assert args.become_method == 'sudo'
    assert args.become_user == 'root'
