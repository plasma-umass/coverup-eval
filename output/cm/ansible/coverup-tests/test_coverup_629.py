# file lib/ansible/cli/vault.py:24-38
# lines [24, 25, 35, 36, 37]
# branches []

import pytest
from ansible.cli.vault import VaultCLI

def test_vault_cli_from_sources(mocker):
    mocker.patch.object(VaultCLI, '__init__', return_value=None)
    
    vault_cli = VaultCLI()
    assert vault_cli.FROM_STDIN == "stdin"
    assert vault_cli.FROM_ARGS == "the command line args"
    assert vault_cli.FROM_PROMPT == "the interactive prompt"
