# file lib/ansible/module_utils/urls.py:853-882
# lines [853, 858, 859, 863, 864, 866, 867, 868, 869, 872, 874, 879, 880, 882]
# branches ['863->864', '863->874', '868->869', '868->872', '879->880', '879->882']

import pytest
from unittest import mock
from ansible.module_utils.urls import build_ssl_validation_error, SSLValidationError

def test_build_ssl_validation_error(mocker):
    # Mocking the necessary global variables and functions
    mocker.patch('ansible.module_utils.urls.HAS_SSLCONTEXT', False)
    mocker.patch('ansible.module_utils.urls.HAS_URLLIB3_PYOPENSSLCONTEXT', False)
    mocker.patch('ansible.module_utils.urls.HAS_URLLIB3_SSL_WRAP_SOCKET', False)
    mocker.patch('ansible.module_utils.urls.sys.executable', '/usr/bin/python')
    mocker.patch('ansible.module_utils.urls.sys.version', '2.7.5')
    mocker.patch('ansible.module_utils.urls.to_native', lambda x: str(x))

    hostname = 'example.com'
    port = 443
    paths = ['/etc/ssl/certs', '/usr/local/share/ca-certificates']
    exc = Exception('Test exception message')

    with pytest.raises(SSLValidationError) as excinfo:
        build_ssl_validation_error(hostname, port, paths, exc)

    expected_message = (
        'Failed to validate the SSL certificate for example.com:443. Make sure your managed systems have a valid CA'
        ' certificate installed. If the website serving the url uses SNI you need python >= 2.7.9 on your managed machine'
        ' (the python executable used (/usr/bin/python) is version: 2.7.5) or you can install the `urllib3`, `pyOpenSSL`,'
        ' `ndg-httpsclient`, and `pyasn1` python modules to perform SNI verification in python >= 2.6. You can use'
        ' validate_certs=False if you do not need to confirm the servers identity but this is unsafe and not recommended.'
        ' Paths checked for this platform: /etc/ssl/certs, /usr/local/share/ca-certificates. The exception msg was: Test exception message.'
    )

    # Remove extra spaces for comparison
    assert ' '.join(str(excinfo.value).split()) == ' '.join(expected_message.split())
