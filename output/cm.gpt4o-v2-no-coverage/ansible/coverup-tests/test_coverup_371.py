# file: lib/ansible/utils/jsonrpc.py:81-89
# asked: {"lines": [81, 82, 83, 84, 85, 86, 87, 88, 89], "branches": [[83, 84], [83, 85], [85, 86], [85, 88]]}
# gained: {"lines": [81, 82, 83, 84, 85, 86, 87, 88, 89], "branches": [[83, 84], [83, 85], [85, 86], [85, 88]]}

import pytest
from ansible.module_utils._text import to_text
from ansible.module_utils.six import binary_type, text_type
from ansible.module_utils.six.moves import cPickle
from ansible.utils.jsonrpc import JsonRpcServer

class TestJsonRpcServer:
    
    @pytest.fixture
    def server(self):
        server = JsonRpcServer()
        server._identifier = 1  # Mocking the _identifier attribute
        return server

    def test_response_with_binary_type(self, server):
        result = b'binary data'
        response = server.response(result)
        assert response['result'] == to_text(result)
        assert 'result_type' not in response

    def test_response_with_text_type(self, server):
        result = 'text data'
        response = server.response(result)
        assert response['result'] == result
        assert 'result_type' not in response

    def test_response_with_other_type(self, server):
        result = {'key': 'value'}
        response = server.response(result)
        assert response['result_type'] == 'pickle'
        assert response['result'] == to_text(cPickle.dumps(result, protocol=0))
