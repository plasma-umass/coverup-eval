# file: lib/ansible/plugins/connection/psrp.py:777-880
# asked: {"lines": [777, 778, 779, 780, 782, 783, 784, 785, 786, 787, 788, 789, 790, 792, 793, 795, 796, 798, 799, 800, 801, 802, 803, 805, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 818, 819, 820, 821, 822, 823, 824, 825, 826, 828, 829, 830, 831, 832, 833, 835, 836, 837, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 861, 862, 863, 864, 868, 869, 870, 872, 873, 874, 875, 878, 879, 880], "branches": [[784, 785], [784, 787], [787, 788], [787, 789], [789, 790], [789, 792], [800, 801], [800, 802], [802, 803], [802, 805], [829, 830], [829, 831], [835, 836], [835, 839], [861, 862], [861, 863], [863, 864], [863, 868], [868, 869], [868, 872], [872, 873], [872, 874], [874, 875], [874, 878], [878, 0], [878, 879]]}
# gained: {"lines": [777, 778, 779, 780, 782, 783, 784, 785, 786, 787, 788, 789, 790, 792, 793, 795, 796, 798, 799, 800, 801, 802, 803, 805, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 818, 819, 820, 821, 822, 823, 824, 825, 826, 828, 829, 830, 831, 832, 833, 835, 836, 837, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 861, 862, 863, 864, 868, 869, 870, 872, 873, 874, 875, 878], "branches": [[784, 785], [784, 787], [787, 788], [787, 789], [789, 790], [789, 792], [800, 801], [800, 802], [802, 803], [802, 805], [829, 830], [829, 831], [835, 836], [835, 839], [861, 862], [861, 863], [863, 864], [868, 869], [868, 872], [872, 873], [874, 875], [878, 0]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.connection.psrp import Connection
from ansible.playbook.play_context import PlayContext
from pypsrp.wsman import AUTH_KWARGS

@pytest.fixture
def connection():
    play_context = PlayContext()
    play_context.shell = 'powershell'
    conn = Connection(play_context, None)
    return conn

@pytest.mark.parametrize("protocol, port, expected_protocol, expected_port", [
    (None, None, 'https', 5986),
    (None, 5985, 'http', 5985),
    ('http', None, 'http', 5985),
    ('https', None, 'https', 5986),
])
@patch('ansible.plugins.connection.psrp.Connection.get_option')
def test_build_kwargs_protocol_port(mock_get_option, connection, protocol, port, expected_protocol, expected_port):
    mock_get_option.side_effect = lambda option: {
        'remote_addr': 'test_host',
        'remote_user': 'test_user',
        'remote_password': 'test_pass',
        'protocol': protocol,
        'port': port,
        'path': 'test_path',
        'auth': 'test_auth',
        'cert_validation': 'ignore',
        'ca_cert': None,
        'connection_timeout': 30,
        'read_timeout': 60,
        'message_encryption': True,
        'proxy': 'test_proxy',
        'ignore_proxy': 'yes',
        'operation_timeout': 120,
        'max_envelope_size': 153600,
        'configuration_name': 'test_config',
        'reconnection_retries': 5,
        'reconnection_backoff': 2.0,
        'certificate_key_pem': 'test_key_pem',
        'certificate_pem': 'test_cert_pem',
        'credssp_auth_mechanism': 'test_mech',
        'credssp_disable_tlsv1_2': True,
        'credssp_minimum_version': 'test_version',
        'negotiate_send_cbt': True,
        'negotiate_delegate': 'test_delegate',
        'negotiate_hostname_override': 'test_override',
        'negotiate_service': 'test_service',
        '_extras': []
    }.get(option, None)

    connection._build_kwargs()

    assert connection._psrp_protocol == expected_protocol
    assert connection._psrp_port == expected_port

@patch('ansible.plugins.connection.psrp.Connection.get_option')
def test_build_kwargs_cert_validation(mock_get_option, connection):
    mock_get_option.side_effect = lambda option: {
        'remote_addr': 'test_host',
        'remote_user': 'test_user',
        'remote_password': 'test_pass',
        'protocol': 'https',
        'port': 5986,
        'path': 'test_path',
        'auth': 'test_auth',
        'cert_validation': 'ignore',
        'ca_cert': 'test_ca_cert',
        'connection_timeout': 30,
        'read_timeout': 60,
        'message_encryption': True,
        'proxy': 'test_proxy',
        'ignore_proxy': 'yes',
        'operation_timeout': 120,
        'max_envelope_size': 153600,
        'configuration_name': 'test_config',
        'reconnection_retries': 5,
        'reconnection_backoff': 2.0,
        'certificate_key_pem': 'test_key_pem',
        'certificate_pem': 'test_cert_pem',
        'credssp_auth_mechanism': 'test_mech',
        'credssp_disable_tlsv1_2': True,
        'credssp_minimum_version': 'test_version',
        'negotiate_send_cbt': True,
        'negotiate_delegate': 'test_delegate',
        'negotiate_hostname_override': 'test_override',
        'negotiate_service': 'test_service',
        '_extras': []
    }.get(option, None)

    connection._build_kwargs()

    assert connection._psrp_cert_validation == False

    mock_get_option.side_effect = lambda option: {
        'remote_addr': 'test_host',
        'remote_user': 'test_user',
        'remote_password': 'test_pass',
        'protocol': 'https',
        'port': 5986,
        'path': 'test_path',
        'auth': 'test_auth',
        'cert_validation': 'validate',
        'ca_cert': 'test_ca_cert',
        'connection_timeout': 30,
        'read_timeout': 60,
        'message_encryption': True,
        'proxy': 'test_proxy',
        'ignore_proxy': 'yes',
        'operation_timeout': 120,
        'max_envelope_size': 153600,
        'configuration_name': 'test_config',
        'reconnection_retries': 5,
        'reconnection_backoff': 2.0,
        'certificate_key_pem': 'test_key_pem',
        'certificate_pem': 'test_cert_pem',
        'credssp_auth_mechanism': 'test_mech',
        'credssp_disable_tlsv1_2': True,
        'credssp_minimum_version': 'test_version',
        'negotiate_send_cbt': True,
        'negotiate_delegate': 'test_delegate',
        'negotiate_hostname_override': 'test_override',
        'negotiate_service': 'test_service',
        '_extras': []
    }.get(option, None)

    connection._build_kwargs()

    assert connection._psrp_cert_validation == 'test_ca_cert'

    mock_get_option.side_effect = lambda option: {
        'remote_addr': 'test_host',
        'remote_user': 'test_user',
        'remote_password': 'test_pass',
        'protocol': 'https',
        'port': 5986,
        'path': 'test_path',
        'auth': 'test_auth',
        'cert_validation': 'validate',
        'ca_cert': None,
        'connection_timeout': 30,
        'read_timeout': 60,
        'message_encryption': True,
        'proxy': 'test_proxy',
        'ignore_proxy': 'yes',
        'operation_timeout': 120,
        'max_envelope_size': 153600,
        'configuration_name': 'test_config',
        'reconnection_retries': 5,
        'reconnection_backoff': 2.0,
        'certificate_key_pem': 'test_key_pem',
        'certificate_pem': 'test_cert_pem',
        'credssp_auth_mechanism': 'test_mech',
        'credssp_disable_tlsv1_2': True,
        'credssp_minimum_version': 'test_version',
        'negotiate_send_cbt': True,
        'negotiate_delegate': 'test_delegate',
        'negotiate_hostname_override': 'test_override',
        'negotiate_service': 'test_service',
        '_extras': []
    }.get(option, None)

    connection._build_kwargs()

    assert connection._psrp_cert_validation == True

@patch('ansible.plugins.connection.psrp.Connection.get_option')
@patch('ansible.plugins.connection.psrp.display')
def test_build_kwargs_warnings(mock_display, mock_get_option, connection):
    mock_get_option.side_effect = lambda option: {
        'remote_addr': 'test_host',
        'remote_user': 'test_user',
        'remote_password': 'test_pass',
        'protocol': 'https',
        'port': 5986,
        'path': 'test_path',
        'auth': 'test_auth',
        'cert_validation': 'validate',
        'ca_cert': None,
        'connection_timeout': 30,
        'read_timeout': 60,
        'message_encryption': True,
        'proxy': 'test_proxy',
        'ignore_proxy': 'yes',
        'operation_timeout': 120,
        'max_envelope_size': 153600,
        'configuration_name': 'test_config',
        'reconnection_retries': 5,
        'reconnection_backoff': 2.0,
        'certificate_key_pem': 'test_key_pem',
        'certificate_pem': 'test_cert_pem',
        'credssp_auth_mechanism': 'test_mech',
        'credssp_disable_tlsv1_2': True,
        'credssp_minimum_version': 'test_version',
        'negotiate_send_cbt': True,
        'negotiate_delegate': 'test_delegate',
        'negotiate_hostname_override': 'test_override',
        'negotiate_service': 'test_service',
        '_extras': ['ansible_psrp_unsupported_arg']
    }.get(option, None)

    with patch('pypsrp.FEATURES', new_callable=set):
        connection._build_kwargs()

    mock_display.warning.assert_any_call("ansible_psrp_unsupported_arg is unsupported by the current psrp version installed")
    mock_display.warning.assert_any_call("ansible_psrp_read_timeout is unsupported by the current psrp version installed, using ansible_psrp_connection_timeout value for read_timeout instead.")
    mock_display.warning.assert_any_call("ansible_psrp_reconnection_retries is unsupported by the current psrp version installed.")
    mock_display.warning.assert_any_call("ansible_psrp_reconnection_backoff is unsupported by the current psrp version installed.")
