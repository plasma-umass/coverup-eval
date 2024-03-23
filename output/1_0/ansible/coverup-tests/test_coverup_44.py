# file lib/ansible/plugins/doc_fragments/shell_common.py:7-56
# lines [7, 10]
# branches []

import pytest
from ansible.plugins.doc_fragments.shell_common import ModuleDocFragment

@pytest.fixture
def mock_ansible_config(mocker):
    mock_config = mocker.patch('ansible.config.manager.ConfigManager.get_config_value')
    return mock_config

def test_module_doc_fragment(mock_ansible_config):
    mock_ansible_config.return_value = None
    doc_fragment = ModuleDocFragment()
    assert 'options' in doc_fragment.DOCUMENTATION
    assert 'remote_tmp' in doc_fragment.DOCUMENTATION
    assert 'common_remote_group' in doc_fragment.DOCUMENTATION
    assert 'system_tmpdirs' in doc_fragment.DOCUMENTATION
    assert 'async_dir' in doc_fragment.DOCUMENTATION

    # Verify the default values and structure
    assert 'default: \'~/.ansible/tmp\'' in doc_fragment.DOCUMENTATION
    assert 'default: null' in doc_fragment.DOCUMENTATION
    assert 'default: [ /var/tmp, /tmp ]' in doc_fragment.DOCUMENTATION
    assert 'default: \'~/.ansible_async\'' in doc_fragment.DOCUMENTATION

    # Verify environment variables and INI settings
    assert 'env: [{name: ANSIBLE_REMOTE_TEMP}, {name: ANSIBLE_REMOTE_TMP}]' in doc_fragment.DOCUMENTATION
    assert 'env: [{name: ANSIBLE_COMMON_REMOTE_GROUP}]' in doc_fragment.DOCUMENTATION
    assert 'env: [{name: ANSIBLE_SYSTEM_TMPDIRS}]' in doc_fragment.DOCUMENTATION
    assert 'env: [{name: ANSIBLE_ASYNC_DIR}]' in doc_fragment.DOCUMENTATION

    # Verify INI sections and keys
    assert 'ini:' in doc_fragment.DOCUMENTATION
    assert 'section: defaults' in doc_fragment.DOCUMENTATION
    assert 'key: remote_tmp' in doc_fragment.DOCUMENTATION
    assert 'key: common_remote_group' in doc_fragment.DOCUMENTATION
    assert 'key: system_tmpdirs' in doc_fragment.DOCUMENTATION
    assert 'key: async_dir' in doc_fragment.DOCUMENTATION

    # Verify variable names
    assert 'vars:' in doc_fragment.DOCUMENTATION
    assert 'name: ansible_remote_tmp' in doc_fragment.DOCUMENTATION
    assert 'name: ansible_common_remote_group' in doc_fragment.DOCUMENTATION
    assert 'name: ansible_system_tmpdirs' in doc_fragment.DOCUMENTATION
    assert 'name: ansible_async_dir' in doc_fragment.DOCUMENTATION

    # Verify version added
    assert 'version_added: "2.10"' in doc_fragment.DOCUMENTATION
