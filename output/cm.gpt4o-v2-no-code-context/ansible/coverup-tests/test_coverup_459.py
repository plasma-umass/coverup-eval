# file: lib/ansible/modules/dnf.py:403-414
# asked: {"lines": [403, 408, 409, 410, 412, 414], "branches": [[408, 412], [408, 414]]}
# gained: {"lines": [403, 408, 409, 410, 412, 414], "branches": [[408, 412], [408, 414]]}

import pytest
from ansible.modules.dnf import DnfModule
from ansible.module_utils.common.text.converters import to_text

class MockYumDnf:
    pass

class MockModule:
    pass

class TestDnfModule:
    @pytest.fixture
    def dnf_module(self, monkeypatch):
        def mock_init(self, module):
            self.module = module
        monkeypatch.setattr(DnfModule, "__init__", mock_init)
        return DnfModule(MockModule())

    def test_sanitize_dnf_error_msg_install_no_package_matched(self, dnf_module):
        spec = 'somepackage'
        error = 'no package matched'
        result = dnf_module._sanitize_dnf_error_msg_install(spec, error)
        assert result == "No package somepackage available."

    def test_sanitize_dnf_error_msg_install_no_match_for_argument(self, dnf_module):
        spec = 'somepackage'
        error = 'No match for argument: somepackage'
        result = dnf_module._sanitize_dnf_error_msg_install(spec, error)
        assert result == "No package somepackage available."

    def test_sanitize_dnf_error_msg_install_other_error(self, dnf_module):
        spec = 'somepackage'
        error = 'Some other error'
        result = dnf_module._sanitize_dnf_error_msg_install(spec, error)
        assert result == 'Some other error'
