# file lib/ansible/module_utils/urls.py:1669-1687
# lines [1669, 1674, 1675, 1676, 1677, 1678, 1679, 1680, 1681, 1682, 1683, 1684, 1685, 1686]
# branches []

import pytest
from ansible.module_utils.urls import url_argument_spec

def test_url_argument_spec():
    spec = url_argument_spec()
    assert isinstance(spec, dict)
    assert 'url' in spec
    assert spec['force']['default'] is False
    assert 'thirsty' in spec['force']['aliases']
    assert spec['http_agent']['default'] == 'ansible-httpget'
    assert spec['use_proxy']['default'] is True
    assert spec['validate_certs']['default'] is True
    assert 'url_username' in spec
    assert 'url_password' in spec
    assert spec['force_basic_auth']['default'] is False
    assert 'client_cert' in spec
    assert 'client_key' in spec
    assert spec['use_gssapi']['default'] is False
    # Check deprecated alias
    assert spec['force']['deprecated_aliases'][0]['name'] == 'thirsty'
    assert spec['force']['deprecated_aliases'][0]['version'] == '2.13'
    assert spec['force']['deprecated_aliases'][0]['collection_name'] == 'ansible.builtin'
