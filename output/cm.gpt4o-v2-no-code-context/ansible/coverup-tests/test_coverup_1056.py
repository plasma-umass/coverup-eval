# file: lib/ansible/playbook/base.py:229-241
# asked: {"lines": [], "branches": [[231, 233], [237, 240]]}
# gained: {"lines": [], "branches": [[231, 233]]}

import pytest
from unittest.mock import MagicMock, patch

# Assuming the FieldAttributeBase class is imported from ansible.playbook.base
from ansible.playbook.base import FieldAttributeBase

class TestFieldAttributeBase:
    @patch('ansible.playbook.base.display')
    def test_dump_me_depth_0(self, mock_display):
        obj = FieldAttributeBase()
        obj.dump_me(depth=0)
        mock_display.debug.assert_any_call("DUMPING OBJECT ------------------------------------------------------")
        mock_display.debug.assert_any_call("%s- %s (%s, id=%s)" % (" " * 0, obj.__class__.__name__, obj, id(obj)))

    @patch('ansible.playbook.base.display')
    def test_dump_me_with_parent_and_dep_chain(self, mock_display):
        parent = MagicMock()
        dep = MagicMock()
        parent.get_dep_chain.return_value = [dep]
        obj = FieldAttributeBase()
        obj._parent = parent

        obj.dump_me(depth=1)

        parent.dump_me.assert_called_once_with(3)
        dep.dump_me.assert_called_once_with(3)

    @patch('ansible.playbook.base.display')
    def test_dump_me_with_play(self, mock_display):
        play = MagicMock()
        obj = FieldAttributeBase()
        obj._play = play

        obj.dump_me(depth=1)

        play.dump_me.assert_called_once_with(3)
