# file: lib/ansible/module_utils/urls.py:1034-1050
# asked: {"lines": [1035, 1036, 1037, 1039, 1041, 1042, 1043, 1044, 1046, 1048, 1049, 1050], "branches": [[1036, 1037], [1036, 1039], [1041, 1042], [1041, 1043], [1043, 1044], [1043, 1046], [1048, 1049], [1048, 1050]]}
# gained: {"lines": [1035, 1036, 1037, 1039, 1041, 1042, 1043, 1046, 1048, 1049, 1050], "branches": [[1036, 1037], [1036, 1039], [1041, 1042], [1041, 1043], [1043, 1046], [1048, 1049]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.urls import SSLValidationHandler

@pytest.fixture
def ssl_validation_handler():
    handler = SSLValidationHandler(hostname="example.com", port=443)
    handler.ca_path = None
    return handler

def test_make_context_with_cafile(ssl_validation_handler):
    cafile = "/path/to/cafile"
    cadata = None

    with patch("ansible.module_utils.urls.create_default_context") as mock_create_default_context:
        mock_context = MagicMock()
        mock_create_default_context.return_value = mock_context

        ssl_validation_handler.make_context(cafile, cadata)

        mock_create_default_context.assert_called_once_with(cafile=cafile)
        mock_context.load_verify_locations.assert_called_once_with(cafile=cafile, cadata=cadata)

def test_make_context_with_cadata(ssl_validation_handler):
    cafile = None
    cadata = "some_cadata"

    with patch("ansible.module_utils.urls.create_default_context") as mock_create_default_context:
        mock_context = MagicMock()
        mock_create_default_context.return_value = mock_context

        ssl_validation_handler.make_context(cafile, cadata)

        mock_create_default_context.assert_called_once_with(cafile=cafile)
        mock_context.load_verify_locations.assert_called_once_with(cafile=cafile, cadata=cadata)

def test_make_context_with_ca_path(ssl_validation_handler):
    ssl_validation_handler.ca_path = "/path/to/ca_path"
    cafile = "/path/to/cafile"
    cadata = "some_cadata"

    with patch("ansible.module_utils.urls.create_default_context") as mock_create_default_context:
        mock_context = MagicMock()
        mock_create_default_context.return_value = mock_context

        ssl_validation_handler.make_context(cafile, cadata)

        mock_create_default_context.assert_called_once_with(cafile=ssl_validation_handler.ca_path)
        mock_context.load_verify_locations.assert_called_once_with(cafile=ssl_validation_handler.ca_path, cadata=None)

def test_make_context_no_ssl_support(ssl_validation_handler):
    cafile = None
    cadata = None

    with patch("ansible.module_utils.urls.HAS_SSLCONTEXT", False), \
         patch("ansible.module_utils.urls.HAS_URLLIB3_PYOPENSSLCONTEXT", False):
        with pytest.raises(NotImplementedError, match="Host libraries are too old to support creating an sslcontext"):
            ssl_validation_handler.make_context(cafile, cadata)
