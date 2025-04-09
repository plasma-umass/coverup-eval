# file: httpie/plugins/manager.py:51-52
# asked: {"lines": [51, 52], "branches": []}
# gained: {"lines": [51, 52], "branches": []}

import pytest
from httpie.plugins import FormatterPlugin
from httpie.plugins.manager import PluginManager

class DummyFormatter(FormatterPlugin):
    def format_body(self, body: str) -> str:
        return body

def test_get_formatters():
    manager = PluginManager()
    manager.append(DummyFormatter)
    
    formatters = manager.get_formatters()
    
    assert len(formatters) == 1
    assert formatters[0] is DummyFormatter

    # Clean up
    manager.clear()
