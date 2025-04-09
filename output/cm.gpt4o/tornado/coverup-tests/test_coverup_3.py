# file tornado/netutil.py:555-591
# lines [555, 568, 569, 570, 571, 574, 575, 576, 577, 579, 580, 581, 582, 583, 584, 585, 590, 591]
# branches ['568->569', '568->570', '575->576', '575->579', '579->580', '579->581', '581->582', '581->583', '583->584', '583->585', '585->590', '585->591']

import ssl
import pytest
from unittest import mock
from tornado.netutil import ssl_options_to_context

_SSL_CONTEXT_KEYWORDS = {
    "ssl_version",
    "certfile",
    "keyfile",
    "cert_reqs",
    "ca_certs",
    "ciphers",
}

def test_ssl_options_to_context_with_dict(mocker):
    ssl_options = {
        "ssl_version": ssl.PROTOCOL_TLSv1_2,
        "certfile": "path/to/certfile",
        "keyfile": "path/to/keyfile",
        "cert_reqs": ssl.CERT_REQUIRED,
        "ca_certs": "path/to/ca_certs",
        "ciphers": "ECDHE-RSA-AES256-GCM-SHA384",
    }

    mocker.patch("ssl.SSLContext.load_cert_chain")
    mocker.patch("ssl.SSLContext.load_verify_locations")
    mocker.patch("ssl.SSLContext.set_ciphers")

    context = ssl_options_to_context(ssl_options)

    assert isinstance(context, ssl.SSLContext)
    assert context.protocol == ssl.PROTOCOL_TLSv1_2
    context.load_cert_chain.assert_called_once_with("path/to/certfile", "path/to/keyfile")
    context.load_verify_locations.assert_called_once_with("path/to/ca_certs")
    context.set_ciphers.assert_called_once_with("ECDHE-RSA-AES256-GCM-SHA384")
    assert context.verify_mode == ssl.CERT_REQUIRED
    if hasattr(ssl, "OP_NO_COMPRESSION"):
        assert context.options & ssl.OP_NO_COMPRESSION

def test_ssl_options_to_context_with_sslcontext():
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    result = ssl_options_to_context(ssl_context)
    assert result is ssl_context

def test_ssl_options_to_context_invalid_dict():
    ssl_options = {
        "invalid_key": "value"
    }
    with pytest.raises(AssertionError):
        ssl_options_to_context(ssl_options)
