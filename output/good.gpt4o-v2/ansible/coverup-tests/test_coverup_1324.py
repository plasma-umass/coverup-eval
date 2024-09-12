# file: lib/ansible/module_utils/urls.py:909-1003
# asked: {"lines": [913, 914, 915, 917, 918, 919, 920, 921, 922, 923, 926, 928, 929, 931, 934, 935, 936, 937, 938, 939, 940, 941, 942, 943, 944, 945, 949, 951, 952, 953, 954, 957, 958, 959, 960, 961, 965, 967, 972, 973, 974, 975, 976, 977, 978, 979, 980, 981, 982, 983, 984, 985, 986, 989, 990, 992, 993, 994, 995, 997, 998, 999, 1001, 1003], "branches": [[917, 918], [917, 928], [920, 921], [920, 926], [928, 929], [928, 931], [934, 935], [934, 938], [938, 939], [938, 940], [940, 941], [940, 942], [942, 943], [942, 944], [944, 945], [944, 949], [952, 953], [952, 957], [957, 958], [957, 972], [958, 959], [958, 965], [972, 973], [972, 997], [973, 972], [973, 974], [975, 972], [975, 976], [977, 975], [977, 978], [979, 975], [979, 980], [982, 983], [982, 992], [997, 998], [997, 1001]]}
# gained: {"lines": [913, 914, 915, 917, 918, 919, 920, 921, 922, 923, 926, 928, 929, 931, 934, 935, 936, 937, 938, 939, 940, 941, 942, 943, 944, 945, 949, 951, 952, 953, 954, 957, 958, 959, 960, 961, 967, 972, 973, 974, 975, 976, 977, 978, 979, 980, 981, 982, 992, 993, 997, 998, 999, 1001, 1003], "branches": [[917, 918], [917, 928], [920, 921], [928, 929], [928, 931], [934, 935], [934, 938], [938, 939], [938, 940], [940, 941], [940, 942], [942, 943], [942, 944], [944, 945], [944, 949], [952, 953], [952, 957], [957, 958], [957, 972], [958, 959], [972, 973], [972, 997], [973, 972], [973, 974], [975, 972], [975, 976], [977, 975], [977, 978], [979, 980], [982, 992], [997, 998], [997, 1001]]}

import pytest
import os
import tempfile
import platform
from ansible.module_utils.urls import SSLValidationHandler, HAS_SSLCONTEXT, b_DUMMY_CA_CERT, LOADED_VERIFY_LOCATIONS, atexit_remove_file
from ansible.module_utils._text import to_bytes

@pytest.fixture
def ssl_validation_handler():
    return SSLValidationHandler(hostname='localhost', port=443)

def test_get_ca_certs_with_ca_path(ssl_validation_handler, monkeypatch):
    ca_cert_content = b"-----BEGIN CERTIFICATE-----\n...\n-----END CERTIFICATE-----\n"
    with tempfile.NamedTemporaryFile(delete=False) as ca_file:
        ca_file.write(ca_cert_content)
        ca_file_path = ca_file.name

    monkeypatch.setattr(ssl_validation_handler, 'ca_path', ca_file_path)
    result = ssl_validation_handler.get_ca_certs()

    assert result[0] == ca_file_path
    assert result[2] == [ca_file_path]

    os.remove(ca_file_path)

def test_get_ca_certs_without_sslcontext(ssl_validation_handler, monkeypatch):
    monkeypatch.setattr('ansible.module_utils.urls.HAS_SSLCONTEXT', False)
    result = ssl_validation_handler.get_ca_certs()

    assert result[0] is not None
    assert '/etc/ssl/certs' in result[2]

    os.remove(result[0])

def test_get_ca_certs_on_darwin(ssl_validation_handler, monkeypatch):
    monkeypatch.setattr('platform.system', lambda: 'Darwin')
    result = ssl_validation_handler.get_ca_certs()

    assert '/usr/local/etc/openssl' in result[2]

    if result[0]:
        os.remove(result[0])

def test_get_ca_certs_on_linux(ssl_validation_handler, monkeypatch):
    monkeypatch.setattr('platform.system', lambda: 'Linux')
    result = ssl_validation_handler.get_ca_certs()

    assert '/etc/pki/ca-trust/extracted/pem' in result[2]
    assert '/etc/pki/tls/certs' in result[2]
    assert '/usr/share/ca-certificates/cacert.org' in result[2]

def test_get_ca_certs_on_freebsd(ssl_validation_handler, monkeypatch):
    monkeypatch.setattr('platform.system', lambda: 'FreeBSD')
    result = ssl_validation_handler.get_ca_certs()

    assert '/usr/local/share/certs' in result[2]

def test_get_ca_certs_on_openbsd(ssl_validation_handler, monkeypatch):
    monkeypatch.setattr('platform.system', lambda: 'OpenBSD')
    result = ssl_validation_handler.get_ca_certs()

    assert '/etc/ssl' in result[2]

def test_get_ca_certs_on_netbsd(ssl_validation_handler, monkeypatch):
    monkeypatch.setattr('platform.system', lambda: 'NetBSD')
    result = ssl_validation_handler.get_ca_certs()

    assert result[0] is None or '/etc/openssl/certs' in result[0]

def test_get_ca_certs_on_sunos(ssl_validation_handler, monkeypatch):
    monkeypatch.setattr('platform.system', lambda: 'SunOS')
    result = ssl_validation_handler.get_ca_certs()

    assert '/opt/local/etc/openssl/certs' in result[2]

def test_get_ca_certs_with_loaded_verify_locations(ssl_validation_handler, monkeypatch):
    with tempfile.NamedTemporaryFile(delete=False) as ca_file:
        ca_file.write(b_DUMMY_CA_CERT)
        ca_file_path = ca_file.name

    LOADED_VERIFY_LOCATIONS.add(ca_file_path)
    monkeypatch.setattr(ssl_validation_handler, 'ca_path', ca_file_path)
    result = ssl_validation_handler.get_ca_certs()

    assert ca_file_path in LOADED_VERIFY_LOCATIONS

    os.remove(ca_file_path)
