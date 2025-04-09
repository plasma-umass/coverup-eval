# file lib/ansible/modules/pip.py:315-349
# lines [329, 330, 331, 332, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349]
# branches ['330->331', '330->332', '338->339', '338->348', '339->340', '339->343', '340->341', '340->342', '343->344', '343->345', '345->346', '345->347']

import pytest
from ansible.modules.pip import _recover_package_name

def test_recover_package_name():
    # Test case to cover lines 329-349
    input_data = ['django>1.11.1,<1.11.3,ipaddress', 'simpleproject>1.1.0,<2.0.0']
    expected_output = ['django>1.11.1,<1.11.3', 'ipaddress', 'simpleproject>1.1.0,<2.0.0']
    assert _recover_package_name(input_data) == expected_output

    input_data = ['django>1.11.1', '<1.11.3', 'ipaddress', 'simpleproject>1.1.0', '<2.0.0']
    expected_output = ['django>1.11.1,<1.11.3', 'ipaddress', 'simpleproject>1.1.0,<2.0.0']
    assert _recover_package_name(input_data) == expected_output

    input_data = ['package[extra1,extra2]', 'anotherpackage']
    expected_output = ['package[extra1,extra2]', 'anotherpackage']
    assert _recover_package_name(input_data) == expected_output

    input_data = ['package[extra1,extra2,extra3]', 'anotherpackage']
    expected_output = ['package[extra1,extra2,extra3]', 'anotherpackage']
    assert _recover_package_name(input_data) == expected_output

    input_data = ['package[extra1,extra2]', 'anotherpackage[extra3]']
    expected_output = ['package[extra1,extra2]', 'anotherpackage[extra3]']
    assert _recover_package_name(input_data) == expected_output
