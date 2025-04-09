# file: httpie/sessions.py:100-102
# asked: {"lines": [100, 101, 102], "branches": []}
# gained: {"lines": [100, 101, 102], "branches": []}

import pytest
from httpie.sessions import Session, BaseConfigDict, RequestHeadersDict

class MockSession(Session):
    def __init__(self, data):
        self.data = data

    def __getitem__(self, item):
        return self.data[item]

class TestSession:
    @pytest.fixture
    def session(self):
        return MockSession({'headers': {'User-Agent': 'test-agent'}})

    def test_headers_property(self, session):
        headers = session.headers
        assert isinstance(headers, RequestHeadersDict)
        assert headers['User-Agent'] == 'test-agent'
