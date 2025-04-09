# file: lib/ansible/cli/doc.py:210-232
# asked: {"lines": [210, 222, 223, 225, 226, 227, 228, 229, 230, 231, 232], "branches": [[222, 223], [222, 225], [229, 230], [229, 232]]}
# gained: {"lines": [210, 222, 223, 225, 226, 227, 228, 229, 230, 231, 232], "branches": [[222, 223], [222, 225], [229, 230], [229, 232]]}

import pytest

from ansible.cli.doc import RoleMixin

class TestRoleMixin:
    @pytest.fixture
    def role_mixin(self):
        return RoleMixin()

    def test_build_summary_with_collection(self, role_mixin):
        role = "test_role"
        collection = "test_collection"
        argspec = {
            "entry1": {"short_description": "Entry 1 description"},
            "entry2": {"short_description": "Entry 2 description"},
        }

        fqcn, summary = role_mixin._build_summary(role, collection, argspec)

        assert fqcn == "test_collection.test_role"
        assert summary["collection"] == "test_collection"
        assert summary["entry_points"]["entry1"] == "Entry 1 description"
        assert summary["entry_points"]["entry2"] == "Entry 2 description"

    def test_build_summary_without_collection(self, role_mixin):
        role = "test_role"
        collection = ""
        argspec = {
            "entry1": {"short_description": "Entry 1 description"},
            "entry2": {"short_description": "Entry 2 description"},
        }

        fqcn, summary = role_mixin._build_summary(role, collection, argspec)

        assert fqcn == "test_role"
        assert summary["collection"] == ""
        assert summary["entry_points"]["entry1"] == "Entry 1 description"
        assert summary["entry_points"]["entry2"] == "Entry 2 description"

    def test_build_summary_with_empty_argspec(self, role_mixin):
        role = "test_role"
        collection = "test_collection"
        argspec = {}

        fqcn, summary = role_mixin._build_summary(role, collection, argspec)

        assert fqcn == "test_collection.test_role"
        assert summary["collection"] == "test_collection"
        assert summary["entry_points"] == {}
