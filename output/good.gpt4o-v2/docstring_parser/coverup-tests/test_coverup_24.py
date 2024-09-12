# file: docstring_parser/numpydoc.py:207-218
# asked: {"lines": [211, 213, 214, 216, 217], "branches": [[213, 214], [213, 216]]}
# gained: {"lines": [211, 213, 214, 216, 217], "branches": [[213, 214], [213, 216]]}

import pytest
from docstring_parser.common import DocstringDeprecated
from docstring_parser.numpydoc import DeprecationSection

class MockSphinxSection:
    key = "deprecation"

def _clean_str(s):
    return s.strip()

class TestDeprecationSection:
    @pytest.fixture
    def deprecation_section(self, monkeypatch):
        section = DeprecationSection(title="Deprecation Warning", key=MockSphinxSection.key)
        return section

    def test_parse_with_description(self, deprecation_section):
        text = "v1.0\nThis is deprecated."
        result = list(deprecation_section.parse(text))
        assert len(result) == 1
        assert result[0].version == "v1.0"
        assert result[0].description == "This is deprecated."
        assert result[0].args == ["deprecation"]

    def test_parse_without_description(self, deprecation_section):
        text = "v1.0"
        result = list(deprecation_section.parse(text))
        assert len(result) == 1
        assert result[0].version == "v1.0"
        assert result[0].description is None
        assert result[0].args == ["deprecation"]
