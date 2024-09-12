# file: lib/ansible/plugins/doc_fragments/shell_windows.py:7-48
# asked: {"lines": [7, 12], "branches": []}
# gained: {"lines": [7, 12], "branches": []}

import pytest
from ansible.plugins.doc_fragments.shell_windows import ModuleDocFragment

def test_module_doc_fragment_documentation():
    # Ensure the DOCUMENTATION attribute is correctly set
    expected_documentation = """
options:
  async_dir:
    description:
    - Directory in which ansible will keep async job information.
    - Before Ansible 2.8, this was set to C(remote_tmp + "\\.ansible_async").
    default: '%USERPROFILE%\\.ansible_async'
    ini:
    - section: powershell
      key: async_dir
    vars:
    - name: ansible_async_dir
    version_added: '2.8'
  remote_tmp:
    description:
    - Temporary directory to use on targets when copying files to the host.
    default: '%TEMP%'
    ini:
    - section: powershell
      key: remote_tmp
    vars:
    - name: ansible_remote_tmp
  set_module_language:
    description:
    - Controls if we set the locale for modules when executing on the
      target.
    - Windows only supports C(no) as an option.
    type: bool
    default: 'no'
    choices: ['no', False]
  environment:
    description:
    - List of dictionaries of environment variables and their values to use when
      executing commands.
    type: list
    default: [{}]
    """
    assert ModuleDocFragment.DOCUMENTATION.strip() == expected_documentation.strip()
