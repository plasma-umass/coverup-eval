# file: typesystem/fields.py:316-353
# asked: {"lines": [316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 329, 331, 332, 333, 335, 336, 338, 339, 340, 342, 343, 345, 346, 348, 349, 350, 351, 353], "branches": [[332, 333], [332, 335], [335, 336], [335, 338], [338, 339], [338, 353], [339, 340], [339, 342], [342, 343], [342, 345], [345, 346], [345, 348]]}
# gained: {"lines": [316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 329, 331], "branches": []}

import pytest
from typesystem.fields import Field

class TestBooleanField:
    @pytest.fixture
    def boolean_field(self):
        class Boolean(Field):
            errors = {"type": "Must be a boolean.", "null": "May not be null."}
            coerce_values = {
                "true": True,
                "false": False,
                "on": True,
                "off": False,
                "1": True,
                "0": False,
                "": False,
                1: True,
                0: False,
            }
            coerce_null_values = {"", "null", "none"}

            def validate(self, value, *, strict=False):
                if value is None and self.allow_null:
                    return None

                elif value is None:
                    raise self.validation_error("null")

                elif not isinstance(value, bool):
                    if strict:
                        raise self.validation_error("type")

                    if isinstance(value, str):
                        value = value.lower()

                    if self.allow_null and value in self.coerce_null_values:
                        return None

                    try:
                        value = self.coerce_values[value]
                    except (KeyError, TypeError):
                        raise self.validation_error("type")

                return value

        return Boolean()

    def test_validate_none_allow_null(self, boolean_field, monkeypatch):
        monkeypatch.setattr(boolean_field, 'allow_null', True)
        assert boolean_field.validate(None) is None

    def test_validate_none_not_allow_null(self, boolean_field, monkeypatch):
        monkeypatch.setattr(boolean_field, 'allow_null', False)
        with pytest.raises(Exception) as excinfo:
            boolean_field.validate(None)
        assert str(excinfo.value) == "May not be null."

    def test_validate_non_bool_strict(self, boolean_field):
        with pytest.raises(Exception) as excinfo:
            boolean_field.validate("true", strict=True)
        assert str(excinfo.value) == "Must be a boolean."

    def test_validate_non_bool_non_strict(self, boolean_field):
        assert boolean_field.validate("true") is True
        assert boolean_field.validate("false") is False
        assert boolean_field.validate("on") is True
        assert boolean_field.validate("off") is False
        assert boolean_field.validate("1") is True
        assert boolean_field.validate("0") is False
        assert boolean_field.validate("") is False
        assert boolean_field.validate(1) is True
        assert boolean_field.validate(0) is False

    def test_validate_non_bool_invalid(self, boolean_field):
        with pytest.raises(Exception) as excinfo:
            boolean_field.validate("invalid")
        assert str(excinfo.value) == "Must be a boolean."

    def test_validate_coerce_null_values(self, boolean_field, monkeypatch):
        monkeypatch.setattr(boolean_field, 'allow_null', True)
        assert boolean_field.validate("null") is None
        assert boolean_field.validate("none") is None
        assert boolean_field.validate("") is None
