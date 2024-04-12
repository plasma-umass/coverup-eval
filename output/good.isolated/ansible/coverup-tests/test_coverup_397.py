# file lib/ansible/plugins/lookup/random_choice.py:42-53
# lines [42, 44, 46, 47, 48, 49, 50, 51, 53]
# branches ['47->48', '47->53']

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.lookup import random_choice
from unittest.mock import patch
import random

# Test function to cover the exception branch
def test_random_choice_exception():
    with patch.object(random, 'choice', side_effect=Exception("Test Exception")):
        lookup = random_choice.LookupModule()

        with pytest.raises(AnsibleError) as excinfo:
            lookup.run(['a', 'b', 'c'])

        assert "Unable to choose random term: Test Exception" in str(excinfo.value)
