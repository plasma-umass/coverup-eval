# file: lib/ansible/galaxy/api.py:293-296
# asked: {"lines": [293, 296], "branches": []}
# gained: {"lines": [293, 296], "branches": []}

import pytest
from ansible.module_utils._text import to_text
from ansible.galaxy.api import GalaxyAPI

class TestGalaxyAPI:
    
    def test_unicode_method(self):
        class MockGalaxyAPI(GalaxyAPI):
            def __init__(self, name):
                self.name = name

        instance = MockGalaxyAPI(name="TestAPI")
        result = instance.__unicode__()
        assert result == "TestAPI"

    def test_to_text_with_nonstring(self):
        result = to_text(123, nonstring='simplerepr')
        assert result == "123"

        result = to_text(123, nonstring='empty')
        assert result == ""

        result = to_text(123, nonstring='passthru')
        assert result == 123

        with pytest.raises(TypeError):
            to_text(123, nonstring='strict')
