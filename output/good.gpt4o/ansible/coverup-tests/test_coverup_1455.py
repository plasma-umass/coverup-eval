# file lib/ansible/cli/doc.py:88-132
# lines [129]
# branches ['128->129']

import os
import pytest
from unittest import mock
from ansible.errors import AnsibleError, AnsibleParserError
from ansible.cli.doc import RoleMixin

class TestRoleMixin:
    @pytest.fixture
    def role_mixin(self):
        return RoleMixin()

    @pytest.fixture
    def mock_open(self, mocker):
        return mocker.patch("builtins.open", mock.mock_open(read_data=""))

    @pytest.fixture
    def mock_exists(self, mocker):
        return mocker.patch("os.path.exists")

    def test_load_argspec_no_data(self, role_mixin, mock_open, mock_exists):
        role_mixin.ROLE_ARGSPEC_FILES = ['argument_spec.yml', 'main.yml']
        mock_exists.side_effect = lambda path: True

        result = role_mixin._load_argspec(role_name="test_role", role_path="/fake/path")

        assert result == {}
        mock_open.assert_called_once_with('/fake/path/meta/argument_spec.yml', 'r')

    def test_load_argspec_with_data_none(self, role_mixin, mock_open, mock_exists):
        role_mixin.ROLE_ARGSPEC_FILES = ['argument_spec.yml', 'main.yml']
        mock_exists.side_effect = lambda path: True

        with mock.patch('ansible.cli.doc.from_yaml', return_value=None):
            result = role_mixin._load_argspec(role_name="test_role", role_path="/fake/path")

        assert result == {}
        mock_open.assert_called_once_with('/fake/path/meta/argument_spec.yml', 'r')
