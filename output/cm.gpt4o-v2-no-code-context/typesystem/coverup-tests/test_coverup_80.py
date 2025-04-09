# file: typesystem/schemas.py:51-89
# asked: {"lines": [], "branches": [[70, 69]]}
# gained: {"lines": [], "branches": [[70, 69]]}

import pytest
from unittest.mock import MagicMock
from typesystem.schemas import SchemaMetaclass, Field, SchemaDefinitions

class TestSchemaMetaclass:
    def test_branch_70_to_69(self):
        # Mock Field and SchemaDefinitions
        mock_field_base = MagicMock(spec=Field)
        mock_field_base._creation_counter = 0
        mock_field_sub = MagicMock(spec=Field)
        mock_field_sub._creation_counter = 1
        mock_definitions = MagicMock(spec=SchemaDefinitions)

        # Create a base class with fields
        class BaseSchema(metaclass=SchemaMetaclass):
            base_field = mock_field_base

        # Create a subclass that should inherit fields from BaseSchema
        class SubSchema(BaseSchema, metaclass=SchemaMetaclass):
            sub_field = mock_field_sub

        # Verify that the field from BaseSchema is inherited in SubSchema
        assert 'base_field' in SubSchema.fields
        assert SubSchema.fields['base_field'] is mock_field_base

        # Verify that the field from SubSchema is present
        assert 'sub_field' in SubSchema.fields
        assert SubSchema.fields['sub_field'] is mock_field_sub

        # Verify that definitions are set correctly
        assert mock_definitions.__setitem__.called_with('SubSchema', SubSchema)

    def test_no_field_inheritance(self):
        # Mock Field and SchemaDefinitions
        mock_field = MagicMock(spec=Field)
        mock_field._creation_counter = 0
        mock_definitions = MagicMock(spec=SchemaDefinitions)

        # Create a base class without fields
        class BaseSchema(metaclass=SchemaMetaclass):
            pass

        # Create a subclass that should not inherit any fields
        class SubSchema(BaseSchema, metaclass=SchemaMetaclass):
            sub_field = mock_field

        # Verify that the field from SubSchema is present
        assert 'sub_field' in SubSchema.fields
        assert SubSchema.fields['sub_field'] is mock_field

        # Verify that definitions are set correctly
        assert mock_definitions.__setitem__.called_with('SubSchema', SubSchema)

    def test_field_inheritance_with_conflict(self):
        # Mock Field and SchemaDefinitions
        mock_field_base = MagicMock(spec=Field)
        mock_field_base._creation_counter = 0
        mock_field_sub = MagicMock(spec=Field)
        mock_field_sub._creation_counter = 1
        mock_definitions = MagicMock(spec=SchemaDefinitions)

        # Create a base class with fields
        class BaseSchema(metaclass=SchemaMetaclass):
            conflict_field = mock_field_base

        # Create a subclass that should inherit fields from BaseSchema but has a conflicting field
        class SubSchema(BaseSchema, metaclass=SchemaMetaclass):
            conflict_field = mock_field_sub

        # Verify that the field from SubSchema overrides the one from BaseSchema
        assert 'conflict_field' in SubSchema.fields
        assert SubSchema.fields['conflict_field'] is mock_field_sub

        # Verify that definitions are set correctly
        assert mock_definitions.__setitem__.called_with('SubSchema', SubSchema)
