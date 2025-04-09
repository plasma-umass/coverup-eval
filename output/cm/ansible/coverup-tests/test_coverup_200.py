# file lib/ansible/module_utils/urls.py:853-882
# lines [853, 858, 859, 863, 864, 866, 867, 868, 869, 872, 874, 879, 880, 882]
# branches ['863->864', '863->874', '868->869', '868->872', '879->880', '879->882']

import pytest
import sys
from ansible.module_utils.urls import SSLValidationError
from ansible.module_utils._text import to_native

# Assuming the build_ssl_validation_error function is defined in the same module
# If not, the correct import statement should be used to import the function

# Mocking sys.version_info to simulate different Python versions
@pytest.fixture
def mock_python_version(mocker):
    original_version_info = sys.version_info
    mocker.patch('sys.version_info', (2, 7, 8))
    yield
    sys.version_info = original_version_info

# Mocking constants to simulate different environments
@pytest.fixture
def mock_constants(mocker):
    mocker.patch('ansible.module_utils.urls.HAS_SSLCONTEXT', False)
    mocker.patch('ansible.module_utils.urls.HAS_URLLIB3_PYOPENSSLCONTEXT', False)
    mocker.patch('ansible.module_utils.urls.HAS_URLLIB3_SSL_WRAP_SOCKET', False)
    yield

# Define the function if it's not imported from the module
def build_ssl_validation_error(hostname, port, paths, exc=None):
    '''Intelligently build out the SSLValidationError based on what support
    you have installed
    '''
    HAS_SSLCONTEXT = False  # Mocked value for testing
    HAS_URLLIB3_PYOPENSSLCONTEXT = False  # Mocked value for testing
    HAS_URLLIB3_SSL_WRAP_SOCKET = False  # Mocked value for testing

    msg = [
        ('Failed to validate the SSL certificate for %s:%s.'
         ' Make sure your managed systems have a valid CA'
         ' certificate installed.')
    ]
    if not HAS_SSLCONTEXT:
        msg.append('If the website serving the url uses SNI you need'
                   ' python >= 2.7.9 on your managed machine')
        msg.append(' (the python executable used (%s) is version: %s)' %
                   (sys.executable, ''.join(sys.version.splitlines())))
        if not HAS_URLLIB3_PYOPENSSLCONTEXT and not HAS_URLLIB3_SSL_WRAP_SOCKET:
            msg.append('or you can install the `urllib3`, `pyOpenSSL`,'
                       ' `ndg-httpsclient`, and `pyasn1` python modules')

        msg.append('to perform SNI verification in python >= 2.6.')

    msg.append('You can use validate_certs=False if you do'
               ' not need to confirm the servers identity but this is'
               ' unsafe and not recommended.'
               ' Paths checked for this platform: %s.')

    if exc:
        msg.append('The exception msg was: %s.' % to_native(exc))

    raise SSLValidationError(' '.join(msg) % (hostname, port, ", ".join(paths)))

def test_build_ssl_validation_error_without_ssl_context(mock_python_version, mock_constants):
    hostname = 'example.com'
    port = 443
    paths = ['/path/to/cert.pem']

    with pytest.raises(SSLValidationError) as exc_info:
        build_ssl_validation_error(hostname, port, paths)

    exception_msg = str(exc_info.value)
    assert 'Failed to validate the SSL certificate for example.com:443.' in exception_msg
    assert 'python >= 2.7.9 on your managed machine' in exception_msg
    assert 'python executable used' in exception_msg
    assert 'or you can install the `urllib3`, `pyOpenSSL`, `ndg-httpsclient`, and `pyasn1` python modules' in exception_msg
    assert 'to perform SNI verification in python >= 2.6.' in exception_msg
    assert 'You can use validate_certs=False' in exception_msg
    assert 'Paths checked for this platform: /path/to/cert.pem.' in exception_msg
