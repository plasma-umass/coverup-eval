# file: lib/ansible/plugins/connection/psrp.py:777-880
# asked: {"lines": [778, 779, 780, 782, 783, 784, 785, 786, 787, 788, 789, 790, 792, 793, 795, 796, 798, 799, 800, 801, 802, 803, 805, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 818, 819, 820, 821, 822, 823, 824, 825, 826, 828, 829, 830, 831, 832, 833, 835, 836, 837, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 861, 862, 863, 864, 868, 869, 870, 872, 873, 874, 875, 878, 879, 880], "branches": [[784, 785], [784, 787], [787, 788], [787, 789], [789, 790], [789, 792], [800, 801], [800, 802], [802, 803], [802, 805], [829, 830], [829, 831], [835, 836], [835, 839], [861, 862], [861, 863], [863, 864], [863, 868], [868, 869], [868, 872], [872, 873], [872, 874], [874, 875], [874, 878], [878, 0], [878, 879]]}
# gained: {"lines": [778, 779, 780, 782, 783, 784, 785, 786, 792, 793, 795, 796, 798, 799, 800, 801, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 818, 819, 820, 821, 822, 823, 824, 825, 826, 828, 829, 830, 831, 832, 833, 835, 836, 837, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 861, 862, 868, 869, 870, 878], "branches": [[784, 785], [800, 801], [829, 830], [829, 831], [835, 836], [835, 839], [861, 862], [868, 869], [878, 0]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.connection.psrp import Connection

@pytest.fixture
def connection():
    play_context = MagicMock()
    new_stdin = MagicMock()
    shell = MagicMock()
    return Connection(play_context, new_stdin, shell=shell)

def test_build_kwargs(connection, monkeypatch):
    # Mocking get_option to return specific values for testing
    options = {
        'remote_addr': '192.168.1.1',
        'remote_user': 'user',
        'remote_password': 'pass',
        'protocol': None,
        'port': None,
        'path': '/wsman',
        'auth': 'basic',
        'cert_validation': 'ignore',
        'ca_cert': None,
        'connection_timeout': 30,
        'read_timeout': 60,
        'message_encryption': True,
        'proxy': 'proxy.example.com',
        'ignore_proxy': 'yes',
        'operation_timeout': 120,
        'max_envelope_size': 153600,
        'configuration_name': 'config',
        'reconnection_retries': 5,
        'reconnection_backoff': 2.0,
        'certificate_key_pem': 'key.pem',
        'certificate_pem': 'cert.pem',
        'credssp_auth_mechanism': 'auto',
        'credssp_disable_tlsv1_2': False,
        'credssp_minimum_version': '1.0',
        'negotiate_send_cbt': True,
        'negotiate_delegate': False,
        'negotiate_hostname_override': 'hostname',
        'negotiate_service': 'service',
        '_extras': {'ansible_psrp_extra_arg': 'extra_value'}
    }
    
    def get_option_mock(name):
        return options.get(name)
    
    monkeypatch.setattr(connection, 'get_option', get_option_mock)
    
    with patch('pypsrp.FEATURES', new=['wsman_read_timeout', 'wsman_reconnections']):
        connection._build_kwargs()
    
    assert connection._psrp_host == '192.168.1.1'
    assert connection._psrp_user == 'user'
    assert connection._psrp_pass == 'pass'
    assert connection._psrp_protocol == 'https'
    assert connection._psrp_port == 5986
    assert connection._psrp_path == '/wsman'
    assert connection._psrp_auth == 'basic'
    assert connection._psrp_cert_validation is False
    assert connection._psrp_connection_timeout == 30
    assert connection._psrp_read_timeout == 60
    assert connection._psrp_message_encryption is True
    assert connection._psrp_proxy == 'proxy.example.com'
    assert connection._psrp_ignore_proxy is True
    assert connection._psrp_operation_timeout == 120
    assert connection._psrp_max_envelope_size == 153600
    assert connection._psrp_configuration_name == 'config'
    assert connection._psrp_reconnection_retries == 5
    assert connection._psrp_reconnection_backoff == 2.0
    assert connection._psrp_certificate_key_pem == 'key.pem'
    assert connection._psrp_certificate_pem == 'cert.pem'
    assert connection._psrp_credssp_auth_mechanism == 'auto'
    assert connection._psrp_credssp_disable_tlsv1_2 is False
    assert connection._psrp_credssp_minimum_version == '1.0'
    assert connection._psrp_negotiate_send_cbt is True
    assert connection._psrp_negotiate_delegate is False
    assert connection._psrp_negotiate_hostname_override == 'hostname'
    assert connection._psrp_negotiate_service == 'service'
    assert 'extra_arg' not in connection._psrp_conn_kwargs
