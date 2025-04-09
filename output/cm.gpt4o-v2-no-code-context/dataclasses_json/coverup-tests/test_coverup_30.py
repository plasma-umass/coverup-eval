# file: dataclasses_json/undefined.py:169-191
# asked: {"lines": [176, 177, 179, 181, 182, 183, 184, 185, 189, 191], "branches": [[183, 184], [183, 185], [185, 189], [185, 191]]}
# gained: {"lines": [176, 177, 179, 181, 182, 183, 185, 189, 191], "branches": [[183, 185], [185, 189], [185, 191]]}

import pytest
import dataclasses
from dataclasses import field, Field
from dataclasses_json.undefined import _CatchAllUndefinedParameters

class TestCatchAllUndefinedParameters:
    def test_get_default_with_default(self):
        @dataclasses.dataclass
        class TestClass:
            catch_all: dict = field(default_factory=lambda: {"key": "value"})

        catch_all_field = TestClass.__dataclass_fields__['catch_all']
        default_value = _CatchAllUndefinedParameters._get_default(catch_all_field)
        assert default_value == {"key": "value"}

    def test_get_default_with_default_factory(self):
        @dataclasses.dataclass
        class TestClass:
            catch_all: dict = field(default_factory=lambda: {"key": "value"})

        catch_all_field = TestClass.__dataclass_fields__['catch_all']
        default_value = _CatchAllUndefinedParameters._get_default(catch_all_field)
        assert default_value == {"key": "value"}

    def test_get_default_with_no_default(self):
        @dataclasses.dataclass
        class TestClass:
            catch_all: dict = field(default_factory=dict)

        catch_all_field = TestClass.__dataclass_fields__['catch_all']
        default_value = _CatchAllUndefinedParameters._get_default(catch_all_field)
        assert default_value == {}

    def test_get_default_with_missing_type(self, monkeypatch):
        @dataclasses.dataclass
        class TestClass:
            catch_all: dict = field(default=dataclasses.MISSING)

        catch_all_field = TestClass.__dataclass_fields__['catch_all']
        default_value = _CatchAllUndefinedParameters._get_default(catch_all_field)
        assert default_value == _CatchAllUndefinedParameters._SentinelNoDefault
