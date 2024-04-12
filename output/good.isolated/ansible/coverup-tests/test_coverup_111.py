# file lib/ansible/module_utils/facts/system/lsb.py:60-78
# lines [60, 61, 63, 64, 66, 67, 69, 70, 71, 72, 73, 74, 75, 76, 78]
# branches ['63->64', '63->66', '66->67', '66->78', '69->70', '69->71', '71->72', '71->73', '73->74', '73->75', '75->66', '75->76']

import os
import pytest
from ansible.module_utils.facts.system.lsb import LSBFactCollector

@pytest.fixture
def mock_etc_lsb_release(tmp_path, mocker):
    etc_lsb_release = tmp_path / "lsb-release"
    etc_lsb_release.write_text(
        "DISTRIB_ID=TestOS\n"
        "DISTRIB_RELEASE=1.0\n"
        "DISTRIB_DESCRIPTION='Test OS Description'\n"
        "DISTRIB_CODENAME=tester\n"
    )
    mocker.patch('os.path.exists', return_value=True)
    mocker.patch('ansible.module_utils.facts.system.lsb.get_file_lines', return_value=etc_lsb_release.read_text().splitlines())
    return str(etc_lsb_release)

def test_lsb_release_file(mock_etc_lsb_release):
    collector = LSBFactCollector()
    lsb_facts = collector._lsb_release_file(mock_etc_lsb_release)
    
    assert lsb_facts['id'] == 'TestOS'
    assert lsb_facts['release'] == '1.0'
    assert lsb_facts['description'] == "'Test OS Description'"
    assert lsb_facts['codename'] == 'tester'
