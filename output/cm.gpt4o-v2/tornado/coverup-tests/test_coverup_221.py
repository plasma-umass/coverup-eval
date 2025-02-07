# file: tornado/options.py:470-485
# asked: {"lines": [485], "branches": []}
# gained: {"lines": [485], "branches": []}

import pytest
from unittest import mock
from tornado.options import OptionParser, _Mockable

class TestOptionParser:
    def test_mockable(self):
        options = OptionParser()
        mockable_options = options.mockable()
        
        # Use an existing option to test
        options.define('name', default='initial_value')
        
        with mock.patch.object(mockable_options, 'name', 'test_value'):
            assert mockable_options.name == 'test_value'
        
        # Ensure the attribute is reset after the patch
        assert mockable_options.name == 'initial_value'
