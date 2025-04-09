# file: lib/ansible/cli/console.py:357-364
# asked: {"lines": [359, 360, 361, 363, 364], "branches": [[359, 360], [359, 363]]}
# gained: {"lines": [359, 360, 361, 363, 364], "branches": [[359, 360], [359, 363]]}

import pytest
from ansible.cli.console import ConsoleCLI
from ansible.utils.display import Display

class TestConsoleCLI:
    @pytest.fixture(autouse=True)
    def setup(self, monkeypatch):
        self.cli = ConsoleCLI(args=['test'])
        self.display = Display()
        monkeypatch.setattr('ansible.cli.console.display', self.display)
        monkeypatch.setattr(self.display, 'verbosity', 3)  # Ensure verbosity is high enough

    def test_do_become_method_with_arg(self, capsys):
        self.cli.do_become_method('sudo')
        captured = capsys.readouterr()
        assert self.cli.become_method == 'sudo'
        assert "become_method changed to sudo" in captured.out

    def test_do_become_method_without_arg(self, capsys):
        self.cli.become_method = 'sudo'
        self.cli.do_become_method('')
        captured = capsys.readouterr()
        assert "Please specify a become_method, e.g. `become_method su`" in captured.out
        assert "Current become_method is sudo" in captured.out
