# file tornado/netutil.py:555-591
# lines [568, 569, 570, 571, 574, 575, 576, 577, 579, 580, 581, 582, 583, 584, 585, 590, 591]
# branches ['568->569', '568->570', '575->576', '575->579', '579->580', '579->581', '581->582', '581->583', '583->584', '583->585', '585->590', '585->591']

import pytest
import ssl
from tornado.netutil import ssl_options_to_context

@pytest.fixture
def ssl_context():
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    return context

def test_ssl_options_to_context_with_ssl_context(ssl_context):
    result = ssl_options_to_context(ssl_context)
    assert result == ssl_context

def test_ssl_options_to_context_with_dict(mocker):
    mocker.patch('ssl.SSLContext.load_cert_chain')
    mocker.patch('ssl.SSLContext.load_verify_locations')
    mocker.patch('ssl.SSLContext.set_ciphers')

    ssl_options = {
        'ssl_version': ssl.PROTOCOL_TLS_SERVER,
        'certfile': 'path/to/certfile.pem',
        'keyfile': 'path/to/keyfile.pem',
        'cert_reqs': ssl.CERT_REQUIRED,
        'ca_certs': 'path/to/cacerts.pem',
        'ciphers': 'HIGH:!aNULL:!kRSA:!PSK:!SRP:!MD5:!RC4'
    }

    result = ssl_options_to_context(ssl_options)

    assert isinstance(result, ssl.SSLContext)
    ssl.SSLContext.load_cert_chain.assert_called_once_with('path/to/certfile.pem', 'path/to/keyfile.pem')
    ssl.SSLContext.load_verify_locations.assert_called_once_with('path/to/cacerts.pem')
    ssl.SSLContext.set_ciphers.assert_called_once_with('HIGH:!aNULL:!kRSA:!PSK:!SRP:!MD5:!RC4')
    assert result.verify_mode == ssl.CERT_REQUIRED
    if hasattr(ssl, "OP_NO_COMPRESSION"):
        assert result.options & ssl.OP_NO_COMPRESSION
