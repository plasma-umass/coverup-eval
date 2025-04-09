# file httpie/client.py:135-144
# lines [135, 136, 139, 140, 141, 142, 144]
# branches []

import pytest
import http.client
from contextlib import contextmanager

# Assuming the contextmanager max_headers is part of the httpie.client module,
# we need to import it correctly. For the sake of this example, I'll assume it's
# a standalone function in the httpie.client module.
# Adjust the import according to the actual structure of the httpie package.

from httpie.client import max_headers

class TestMaxHeaders:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        # Store the original value to restore it after the test
        self.original_max_headers = http.client._MAXHEADERS
        yield
        # Restore the original value
        http.client._MAXHEADERS = self.original_max_headers

    def test_max_headers_context_manager(self):
        # Test with a specific limit
        with max_headers(10):
            assert http.client._MAXHEADERS == 10, "Max headers should be set to the limit within the context"

        # After the context manager, the value should be restored
        assert http.client._MAXHEADERS == self.original_max_headers, "Max headers should be restored after the context"

        # Test with None as limit, which should set it to float('Inf')
        with max_headers(None):
            assert http.client._MAXHEADERS == float('Inf'), "Max headers should be set to float('Inf') when limit is None"

        # After the context manager, the value should be restored
        assert http.client._MAXHEADERS == self.original_max_headers, "Max headers should be restored after the context"
