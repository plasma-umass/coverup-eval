# file lib/ansible/modules/pip.py:583-602
# lines [596, 597]
# branches ['595->596']

import pytest
from unittest.mock import patch
from ansible.modules.pip import Package
from pkg_resources import Requirement

def test_package_distribute_to_setuptools():
    with patch('pkg_resources.Requirement.parse') as mock_parse:
        mock_req = mock_parse.return_value
        mock_req.project_name = "distribute"
        
        pkg = Package("setuptools", "==1.0")
        
        assert pkg.package_name == "setuptools"
        assert pkg._requirement.project_name == "setuptools"
