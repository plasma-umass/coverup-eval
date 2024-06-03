# file lib/ansible/cli/vault.py:24-38
# lines [24, 25, 35, 36, 37]
# branches []

import pytest
from ansible.cli.vault import VaultCLI

def test_vault_cli_constants():
    # Verify the class constants
    assert VaultCLI.FROM_STDIN == "stdin"
    assert VaultCLI.FROM_ARGS == "the command line args"
    assert VaultCLI.FROM_PROMPT == "the interactive prompt"

    # Verify the class docstring
    expected_doc = ''' can encrypt any structured data file used by Ansible.
                This can include *group_vars/* or *host_vars/* inventory variables,
                variables loaded by *include_vars* or *vars_files*, or variable files
                passed on the ansible-playbook command line with *-e @file.yml* or *-e @file.json*.
                Role variables and defaults are also included!
            
                Because Ansible tasks, handlers, and other objects are data, these can also be encrypted with vault.
                If you'd like to not expose what variables you are using, you can keep an individual task file entirely encrypted.
                '''
    # Normalize whitespace for comparison
    assert ' '.join(VaultCLI.__doc__.split()) == ' '.join(expected_doc.split())
