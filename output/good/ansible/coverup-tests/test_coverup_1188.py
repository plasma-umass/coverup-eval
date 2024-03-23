# file lib/ansible/module_utils/common/dict_transformations.py:86-109
# lines [88, 89, 91, 92, 96, 98, 100, 101, 102, 103, 106, 107, 108, 109]
# branches ['91->92', '91->96', '100->101', '100->102', '102->103', '102->106']

import pytest
from ansible.module_utils.common.dict_transformations import _camel_to_snake

def test_camel_to_snake_reversible():
    # Test the reversible branch
    assert _camel_to_snake('CamelCase', reversible=True) == 'camel_case'
    assert _camel_to_snake('CamelCamelCase', reversible=True) == 'camel_camel_case'
    assert _camel_to_snake('Camel2Camel2Case', reversible=True) == 'camel2_camel2_case'
    # Corrected assertion
    assert _camel_to_snake('getHTTPResponseCode', reversible=True) == 'get_h_t_t_p_response_code'
    assert _camel_to_snake('get2HTTPResponseCode', reversible=True) == 'get2_h_t_t_p_response_code'
    assert _camel_to_snake('HTTPResponseCode', reversible=True) == 'h_t_t_p_response_code'
    assert _camel_to_snake('HTTPResponseCodeXYZ', reversible=True) == 'h_t_t_p_response_code_x_y_z'

def test_camel_to_snake_non_reversible():
    # Test the non-reversible branch with pluralized abbreviation at the end
    assert _camel_to_snake('TargetGroupARNs') == 'target_group_arns'
    assert _camel_to_snake('HTTPResponseCodes') == 'http_response_codes'
    assert _camel_to_snake('SimpleXMLRPCServer') == 'simple_xmlrpc_server'
    assert _camel_to_snake('SimpleXMLRPCServerABCs') == 'simple_xmlrpc_server_abcs'

    # Test the non-reversible branch with no pluralized abbreviation at the end
    assert _camel_to_snake('CamelCase') == 'camel_case'
    assert _camel_to_snake('CamelCamelCase') == 'camel_camel_case'
    assert _camel_to_snake('Camel2Camel2Case') == 'camel2_camel2_case'
    assert _camel_to_snake('getHTTPResponseCode') == 'get_http_response_code'
    assert _camel_to_snake('get2HTTPResponseCode') == 'get2_http_response_code'
    assert _camel_to_snake('HTTPResponseCode') == 'http_response_code'
    assert _camel_to_snake('HTTPResponseCodeXYZ') == 'http_response_code_xyz'
