# file: lib/ansible/module_utils/urls.py:1669-1687
# asked: {"lines": [1669, 1674, 1675, 1676, 1677, 1678, 1679, 1680, 1681, 1682, 1683, 1684, 1685, 1686], "branches": []}
# gained: {"lines": [1669, 1674, 1675, 1676, 1677, 1678, 1679, 1680, 1681, 1682, 1683, 1684, 1685, 1686], "branches": []}

import pytest

def test_url_argument_spec():
    from ansible.module_utils.urls import url_argument_spec

    spec = url_argument_spec()

    assert isinstance(spec, dict)
    assert spec['url']['type'] == 'str'
    assert spec['force']['type'] == 'bool'
    assert spec['force']['default'] is False
    assert spec['force']['aliases'] == ['thirsty']
    assert spec['force']['deprecated_aliases'] == [{'name': 'thirsty', 'version': '2.13', 'collection_name': 'ansible.builtin'}]
    assert spec['http_agent']['type'] == 'str'
    assert spec['http_agent']['default'] == 'ansible-httpget'
    assert spec['use_proxy']['type'] == 'bool'
    assert spec['use_proxy']['default'] is True
    assert spec['validate_certs']['type'] == 'bool'
    assert spec['validate_certs']['default'] is True
    assert spec['url_username']['type'] == 'str'
    assert spec['url_password']['type'] == 'str'
    assert spec['url_password']['no_log'] is True
    assert spec['force_basic_auth']['type'] == 'bool'
    assert spec['force_basic_auth']['default'] is False
    assert spec['client_cert']['type'] == 'path'
    assert spec['client_key']['type'] == 'path'
    assert spec['use_gssapi']['type'] == 'bool'
    assert spec['use_gssapi']['default'] is False
