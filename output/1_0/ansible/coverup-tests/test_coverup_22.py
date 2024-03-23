# file lib/ansible/plugins/doc_fragments/url_windows.py:10-59
# lines [10, 13]
# branches []

import pytest

# Assuming the ModuleDocFragment class is in a file named url_windows.py
from ansible.plugins.doc_fragments.url_windows import ModuleDocFragment

def test_module_doc_fragment():
    # Instantiate the ModuleDocFragment to access the DOCUMENTATION attribute
    doc_fragment = ModuleDocFragment()
    documentation = doc_fragment.DOCUMENTATION

    # Assertions to check if the documentation string contains expected options
    assert 'method' in documentation
    assert 'follow_redirects' in documentation
    assert 'headers' in documentation
    assert 'http_agent' in documentation
    assert 'maximum_redirection' in documentation
    assert 'timeout' in documentation

    # Assertions to check default values and choices
    assert 'default: safe' in documentation
    assert 'choices:' in documentation
    assert '- all' in documentation
    assert '- none' in documentation
    assert '- safe' in documentation
    assert 'default: ansible-httpget' in documentation
    assert 'default: 50' in documentation

    # Assertions to check types
    assert 'type: str' in documentation
    assert 'type: dict' in documentation
    assert 'type: int' in documentation

    # No cleanup is necessary as we are not modifying any state
