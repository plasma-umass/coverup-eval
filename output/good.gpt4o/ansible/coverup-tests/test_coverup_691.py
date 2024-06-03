# file lib/ansible/cli/doc.py:78-87
# lines [78, 79, 86]
# branches []

import pytest
from unittest import mock
from ansible.cli.doc import RoleMixin
import ansible.constants as C

@pytest.fixture
def mock_yaml_extensions(mocker):
    original_yaml_extensions = C.YAML_FILENAME_EXTENSIONS
    mocker.patch.object(C, 'YAML_FILENAME_EXTENSIONS', ['.yml', '.yaml'])
    yield
    C.YAML_FILENAME_EXTENSIONS = original_yaml_extensions

def test_role_argspec_files(mock_yaml_extensions):
    # Reinitialize the ROLE_ARGSPEC_FILES to reflect the patched YAML_FILENAME_EXTENSIONS
    RoleMixin.ROLE_ARGSPEC_FILES = ['argument_specs' + e for e in C.YAML_FILENAME_EXTENSIONS] + ["main" + e for e in C.YAML_FILENAME_EXTENSIONS]
    expected_files = ['argument_specs.yml', 'argument_specs.yaml', 'main.yml', 'main.yaml']
    assert RoleMixin.ROLE_ARGSPEC_FILES == expected_files
