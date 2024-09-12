# file: lib/ansible/modules/ping.py:71-86
# asked: {"lines": [71, 72, 73, 74, 76, 79, 80, 82, 83, 86], "branches": [[79, 80], [79, 82]]}
# gained: {"lines": [71, 72, 73, 74, 76, 79, 80, 82, 83, 86], "branches": [[79, 80], [79, 82]]}

import pytest
from ansible.module_utils.basic import AnsibleModule

def test_main_pong(monkeypatch):
    def mock_exit_json(self, **kwargs):
        assert kwargs == {'ping': 'pong'}
        raise SystemExit(0)

    monkeypatch.setattr(AnsibleModule, 'exit_json', mock_exit_json)

    from ansible.modules.ping import main
    with pytest.raises(SystemExit):
        main()

def test_main_custom_data(monkeypatch):
    def mock_exit_json(self, **kwargs):
        assert kwargs == {'ping': 'custom'}
        raise SystemExit(0)

    monkeypatch.setattr(AnsibleModule, 'exit_json', mock_exit_json)

    def mock_init(self, *args, **kwargs):
        self.params = {'data': 'custom'}

    monkeypatch.setattr(AnsibleModule, '__init__', mock_init)

    from ansible.modules.ping import main
    with pytest.raises(SystemExit):
        main()

def test_main_crash(monkeypatch):
    def mock_exit_json(self, **kwargs):
        raise SystemExit(0)

    monkeypatch.setattr(AnsibleModule, 'exit_json', mock_exit_json)

    def mock_init(self, *args, **kwargs):
        self.params = {'data': 'crash'}

    monkeypatch.setattr(AnsibleModule, '__init__', mock_init)

    from ansible.modules.ping import main
    with pytest.raises(Exception, match="boom"):
        main()
