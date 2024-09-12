# file: lib/ansible/playbook/taggable.py:33-43
# asked: {"lines": [33, 34, 35, 36, 37, 38, 39, 41, 43], "branches": [[34, 35], [34, 36], [36, 37], [36, 43], [38, 39], [38, 41]]}
# gained: {"lines": [33, 34, 35, 36, 37, 38, 39, 43], "branches": [[34, 35], [34, 36], [36, 37], [36, 43], [38, 39]]}

import pytest
from ansible.errors import AnsibleError
from ansible.playbook.taggable import Taggable

class TestTaggable:
    def setup_method(self):
        self.taggable = Taggable()

    def test_load_tags_with_list(self):
        result = self.taggable._load_tags('tags', ['tag1', 'tag2'])
        assert result == ['tag1', 'tag2']

    def test_load_tags_with_string(self):
        result = self.taggable._load_tags('tags', 'tag1, tag2')
        assert result == ['tag1', 'tag2']

    def test_load_tags_with_empty_string(self):
        result = self.taggable._load_tags('tags', '')
        assert result == ['']

    def test_load_tags_with_invalid_type(self):
        with pytest.raises(AnsibleError, match='tags must be specified as a list'):
            self.taggable._load_tags('tags', 123)

    def test_load_tags_with_string_no_comma(self):
        result = self.taggable._load_tags('tags', 'tag1')
        assert result == ['tag1']
