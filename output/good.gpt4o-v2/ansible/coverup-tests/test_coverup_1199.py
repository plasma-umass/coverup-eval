# file: lib/ansible/parsing/utils/yaml.py:25-43
# asked: {"lines": [34, 35, 36, 37, 39, 40, 41, 43], "branches": [[35, 36], [35, 39]]}
# gained: {"lines": [34, 35, 36, 37, 39, 40, 41, 43], "branches": [[35, 36], [35, 39]]}

import pytest
from unittest.mock import Mock, patch
from ansible.errors import AnsibleParserError
from ansible.errors.yaml_strings import YAML_SYNTAX_ERROR
from ansible.module_utils._text import to_native
from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
from ansible.parsing.utils.yaml import _handle_error

def test_handle_error_with_problem_mark():
    json_exc = Mock()
    yaml_exc = Mock()
    yaml_exc.problem_mark = Mock()
    yaml_exc.problem_mark.line = 1
    yaml_exc.problem_mark.column = 1
    yaml_exc.problem = "some problem"
    file_name = "test_file.yml"
    show_content = True

    with pytest.raises(AnsibleParserError) as excinfo:
        _handle_error(json_exc, yaml_exc, file_name, show_content)

    assert excinfo.value.obj.ansible_pos == (file_name, 2, 2)
    assert "Syntax Error while loading YAML" in str(excinfo.value)
    assert "some problem" in str(excinfo.value)

def test_handle_error_without_problem_mark():
    json_exc = Mock()
    yaml_exc = Mock()
    del yaml_exc.problem_mark  # Ensure problem_mark attribute does not exist
    yaml_exc.problem = "some problem"
    file_name = "test_file.yml"
    show_content = True

    with pytest.raises(AnsibleParserError) as excinfo:
        _handle_error(json_exc, yaml_exc, file_name, show_content)

    assert excinfo.value.obj is None
    assert "Syntax Error while loading YAML" in str(excinfo.value)
    assert "some problem" in str(excinfo.value)
