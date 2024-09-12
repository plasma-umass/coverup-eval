# file: lib/ansible/galaxy/api.py:293-296
# asked: {"lines": [293, 296], "branches": []}
# gained: {"lines": [293, 296], "branches": []}

import pytest
from ansible.module_utils._text import to_text
from ansible.galaxy.api import GalaxyAPI

def test_unicode_method():
    # Create a GalaxyAPI instance with a name
    galaxy_api_instance = GalaxyAPI(galaxy=None, name="test_name", url="http://example.com")

    # Call the __unicode__ method
    unicode_representation = galaxy_api_instance.__unicode__()

    # Assert that the unicode representation is correct
    assert unicode_representation == to_text("test_name")
