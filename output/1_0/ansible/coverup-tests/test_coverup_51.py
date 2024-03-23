# file lib/ansible/plugins/doc_fragments/shell_windows.py:7-48
# lines [7, 12]
# branches []

import pytest

@pytest.fixture
def mock_ansible_module(mocker):
    mocker.patch('ansible.plugins.doc_fragments.shell_windows.ModuleDocFragment')

def test_module_doc_fragment():
    from ansible.plugins.doc_fragments.shell_windows import ModuleDocFragment
    assert hasattr(ModuleDocFragment, 'DOCUMENTATION')
    doc = ModuleDocFragment.DOCUMENTATION
    assert 'options' in doc
    assert 'async_dir' in doc
    assert 'remote_tmp' in doc
    assert 'set_module_language' in doc
    assert 'environment' in doc
