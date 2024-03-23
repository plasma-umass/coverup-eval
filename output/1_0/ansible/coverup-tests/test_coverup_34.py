# file lib/ansible/plugins/doc_fragments/default_callback.py:9-58
# lines [9, 11]
# branches []

import os
import pytest
from ansible.plugins.doc_fragments.default_callback import ModuleDocFragment

# Test function to cover the missing lines/branches
def test_module_doc_fragment_env_deprecated(mocker):
    mocker.patch.dict(os.environ, {
        "DISPLAY_SKIPPED_HOSTS": "false",
        "ANSIBLE_DISPLAY_SKIPPED_HOSTS": "true",
        "ANSIBLE_DISPLAY_OK_HOSTS": "true",
        "ANSIBLE_DISPLAY_FAILED_STDERR": "true",
        "ANSIBLE_SHOW_CUSTOM_STATS": "true"
    })

    # Access the DOCUMENTATION attribute to trigger the parsing of the env vars
    doc_fragment = ModuleDocFragment.DOCUMENTATION

    # Assertions to verify the postconditions
    assert 'DISPLAY_SKIPPED_HOSTS' in os.environ
    assert os.environ['DISPLAY_SKIPPED_HOSTS'] == 'false'
    assert 'ANSIBLE_DISPLAY_SKIPPED_HOSTS' in os.environ
    assert os.environ['ANSIBLE_DISPLAY_SKIPPED_HOSTS'] == 'true'
    assert 'ANSIBLE_DISPLAY_OK_HOSTS' in os.environ
    assert os.environ['ANSIBLE_DISPLAY_OK_HOSTS'] == 'true'
    assert 'ANSIBLE_DISPLAY_FAILED_STDERR' in os.environ
    assert os.environ['ANSIBLE_DISPLAY_FAILED_STDERR'] == 'true'
    assert 'ANSIBLE_SHOW_CUSTOM_STATS' in os.environ
    assert os.environ['ANSIBLE_SHOW_CUSTOM_STATS'] == 'true'

    # Clean up the environment variables to not affect other tests
    del os.environ['DISPLAY_SKIPPED_HOSTS']
    del os.environ['ANSIBLE_DISPLAY_SKIPPED_HOSTS']
    del os.environ['ANSIBLE_DISPLAY_OK_HOSTS']
    del os.environ['ANSIBLE_DISPLAY_FAILED_STDERR']
    del os.environ['ANSIBLE_SHOW_CUSTOM_STATS']
