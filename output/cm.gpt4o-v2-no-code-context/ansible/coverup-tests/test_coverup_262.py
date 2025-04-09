# file: lib/ansible/module_utils/urls.py:1669-1687
# asked: {"lines": [1669, 1674, 1675, 1676, 1677, 1678, 1679, 1680, 1681, 1682, 1683, 1684, 1685, 1686], "branches": []}
# gained: {"lines": [1669, 1674, 1675, 1676, 1677, 1678, 1679, 1680, 1681, 1682, 1683, 1684, 1685, 1686], "branches": []}

import pytest
from ansible.module_utils.urls import url_argument_spec

def test_url_argument_spec():
    spec = url_argument_spec()
    
    assert 'url' in spec
    assert spec['url']['type'] == 'str'
    
    assert 'force' in spec
    assert spec['force']['type'] == 'bool'
    assert spec['force']['default'] is False
    assert 'thirsty' in spec['force']['aliases']
    assert spec['force']['deprecated_aliases'][0]['name'] == 'thirsty'
    assert spec['force']['deprecated_aliases'][0]['version'] == '2.13'
    assert spec['force']['deprecated_aliases'][0]['collection_name'] == 'ansible.builtin'
    
    assert 'http_agent' in spec
    assert spec['http_agent']['type'] == 'str'
    assert spec['http_agent']['default'] == 'ansible-httpget'
    
    assert 'use_proxy' in spec
    assert spec['use_proxy']['type'] == 'bool'
    assert spec['use_proxy']['default'] is True
    
    assert 'validate_certs' in spec
    assert spec['validate_certs']['type'] == 'bool'
    assert spec['validate_certs']['default'] is True
    
    assert 'url_username' in spec
    assert spec['url_username']['type'] == 'str'
    
    assert 'url_password' in spec
    assert spec['url_password']['type'] == 'str'
    assert spec['url_password']['no_log'] is True
    
    assert 'force_basic_auth' in spec
    assert spec['force_basic_auth']['type'] == 'bool'
    assert spec['force_basic_auth']['default'] is False
    
    assert 'client_cert' in spec
    assert spec['client_cert']['type'] == 'path'
    
    assert 'client_key' in spec
    assert spec['client_key']['type'] == 'path'
    
    assert 'use_gssapi' in spec
    assert spec['use_gssapi']['type'] == 'bool'
    assert spec['use_gssapi']['default'] is False
