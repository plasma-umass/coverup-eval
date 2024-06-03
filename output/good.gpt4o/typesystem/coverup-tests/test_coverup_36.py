# file typesystem/schemas.py:204-247
# lines [204, 205, 207, 210, 213, 214, 215, 216, 217, 219, 220, 222, 223, 224, 225, 226, 228, 229, 230, 231, 232, 233, 234, 235, 237, 238, 239, 240, 241, 242, 244, 245, 246, 247]
# branches ['216->217', '216->219', '224->225', '224->226', '230->231', '230->235', '238->239', '238->240', '240->241', '240->242', '245->246', '245->247']

import pytest
import typing
from typesystem.schemas import Schema, Field
from typesystem import ValidationError

class Reference(Field):
    errors = {"null": "May not be null."}

    def __init__(
        self,
        to: typing.Union[str, typing.Type[Schema]],
        definitions: typing.Mapping = None,
        **kwargs: typing.Any,
    ) -> None:
        super().__init__(**kwargs)
        self.to = to
        self.definitions = definitions
        if isinstance(to, str):
            self._target_string = to
        else:
            assert issubclass(to, Schema)
            self._target = to

    @property
    def target_string(self) -> str:
        if not hasattr(self, "_target_string"):
            self._target_string = self._target.__name__
        return self._target_string

    @property
    def target(self) -> typing.Union[Field, typing.Type[Schema]]:
        if not hasattr(self, "_target"):
            assert (
                self.definitions is not None
            ), "String reference missing 'definitions'."
            self._target = self.definitions[self.to]
        return self._target

    def validate(self, value: typing.Any, *, strict: bool = False) -> typing.Any:
        if value is None and self.allow_null:
            return None
        elif value is None:
            raise self.validation_error("null")
        return self.target.validate(value, strict=strict)

    def serialize(self, obj: typing.Any) -> typing.Any:
        if obj is None:
            return None
        return dict(obj)

class TestReferenceField:
    class MockSchema(Schema):
        def validate(self, value: typing.Any, *, strict: bool = False) -> typing.Any:
            return value

    def test_reference_field_with_string_target(self):
        definitions = {"MockSchema": self.MockSchema}
        ref = Reference(to="MockSchema", definitions=definitions)
        
        assert ref.target_string == "MockSchema"
        assert ref.target == self.MockSchema

    def test_reference_field_with_class_target(self):
        ref = Reference(to=self.MockSchema)
        
        assert ref.target_string == "MockSchema"
        assert ref.target == self.MockSchema

    def test_reference_field_validate_with_null(self):
        ref = Reference(to=self.MockSchema, allow_null=True)
        
        assert ref.validate(None) is None

    def test_reference_field_validate_without_null(self):
        ref = Reference(to=self.MockSchema, allow_null=False)
        
        with pytest.raises(ValidationError, match="May not be null."):
            ref.validate(None)

    def test_reference_field_serialize(self):
        ref = Reference(to=self.MockSchema)
        obj = {"key": "value"}
        
        assert ref.serialize(obj) == obj
        assert ref.serialize(None) is None
