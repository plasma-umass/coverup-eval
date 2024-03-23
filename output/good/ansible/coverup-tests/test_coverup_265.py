# file lib/ansible/playbook/taggable.py:33-43
# lines [33, 34, 35, 36, 37, 38, 39, 41, 43]
# branches ['34->35', '34->36', '36->37', '36->43', '38->39', '38->41']

import pytest
from ansible.errors import AnsibleError
from ansible.playbook.taggable import Taggable

# Mocking string_types for the purpose of the test
string_types = (str,)

# Including the mock in the Taggable class
Taggable.string_types = string_types

def test_load_tags_with_list():
    taggable = Taggable()
    tags_list = ['tag1', 'tag2', 'tag3']
    assert taggable._load_tags('tags', tags_list) == tags_list

def test_load_tags_with_string():
    taggable = Taggable()
    tags_string = 'tag1,tag2,tag3'
    expected_tags_list = ['tag1', 'tag2', 'tag3']
    assert taggable._load_tags('tags', tags_string) == expected_tags_list

def test_load_tags_with_invalid_type():
    taggable = Taggable()
    with pytest.raises(AnsibleError) as excinfo:
        taggable._load_tags('tags', 123)
    assert 'tags must be specified as a list' in str(excinfo.value)
