# file: lib/ansible/playbook/base.py:229-241
# asked: {"lines": [231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241], "branches": [[231, 232], [231, 233], [234, 235], [234, 240], [237, 238], [237, 240], [238, 239], [238, 240], [240, 0], [240, 241]]}
# gained: {"lines": [231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241], "branches": [[231, 232], [231, 233], [234, 235], [234, 240], [237, 238], [238, 239], [238, 240], [240, 0], [240, 241]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.playbook.base import FieldAttributeBase
from ansible.utils.display import Display

@pytest.fixture
def field_attribute_base():
    return FieldAttributeBase()

def test_dump_me_no_depth(field_attribute_base, mocker):
    mock_display = mocker.patch.object(Display, 'debug')
    field_attribute_base.dump_me(depth=0)
    mock_display.assert_any_call("DUMPING OBJECT ------------------------------------------------------")
    mock_display.assert_any_call(f"- {field_attribute_base.__class__.__name__} ({field_attribute_base}, id={id(field_attribute_base)})")

def test_dump_me_with_parent(field_attribute_base, mocker):
    mock_display = mocker.patch.object(Display, 'debug')
    parent_mock = MagicMock()
    field_attribute_base._parent = parent_mock
    parent_mock.get_dep_chain.return_value = [MagicMock(), MagicMock()]
    field_attribute_base.dump_me(depth=1)
    parent_mock.dump_me.assert_called_with(3)
    for dep in parent_mock.get_dep_chain():
        dep.dump_me.assert_called_with(3)

def test_dump_me_with_play(field_attribute_base, mocker):
    mock_display = mocker.patch.object(Display, 'debug')
    play_mock = MagicMock()
    field_attribute_base._play = play_mock
    field_attribute_base.dump_me(depth=1)
    play_mock.dump_me.assert_called_with(3)
