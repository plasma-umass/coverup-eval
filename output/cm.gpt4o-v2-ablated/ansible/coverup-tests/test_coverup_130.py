# file: lib/ansible/modules/ping.py:71-86
# asked: {"lines": [71, 72, 73, 74, 76, 79, 80, 82, 83, 86], "branches": [[79, 80], [79, 82]]}
# gained: {"lines": [71, 72, 73, 74, 76, 79, 80, 82, 83, 86], "branches": [[79, 80], [79, 82]]}

import pytest
from ansible.module_utils.basic import AnsibleModule
from ansible.modules.ping import main

def test_main_pong(monkeypatch):
    def mock_init(self, argument_spec, supports_check_mode):
        self.params = {'data': 'pong'}
        self.supports_check_mode = supports_check_mode

    def mock_exit_json(self, **kwargs):
        assert kwargs == {'ping': 'pong'}
        raise SystemExit

    monkeypatch.setattr(AnsibleModule, '__init__', mock_init)
    monkeypatch.setattr(AnsibleModule, 'exit_json', mock_exit_json)

    with pytest.raises(SystemExit):
        main()

def test_main_custom_data(monkeypatch):
    def mock_init(self, argument_spec, supports_check_mode):
        self.params = {'data': 'hello'}
        self.supports_check_mode = supports_check_mode

    def mock_exit_json(self, **kwargs):
        assert kwargs == {'ping': 'hello'}
        raise SystemExit

    monkeypatch.setattr(AnsibleModule, '__init__', mock_init)
    monkeypatch.setattr(AnsibleModule, 'exit_json', mock_exit_json)

    with pytest.raises(SystemExit):
        main()

def test_main_crash(monkeypatch):
    def mock_init(self, argument_spec, supports_check_mode):
        self.params = {'data': 'crash'}
        self.supports_check_mode = supports_check_mode

    monkeypatch.setattr(AnsibleModule, '__init__', mock_init)

    with pytest.raises(Exception, match="boom"):
        main()
