# file: typesystem/schemas.py:166-173
# asked: {"lines": [166, 167, 168, 170, 171, 172, 173], "branches": [[167, 168], [167, 170], [170, 171], [170, 173], [171, 170], [171, 172]]}
# gained: {"lines": [166, 167, 168, 170, 171, 172, 173], "branches": [[167, 168], [167, 170], [170, 171], [170, 173], [171, 170], [171, 172]]}

import pytest
from unittest.mock import MagicMock, patch
from typesystem.schemas import Schema
from typesystem.fields import Field

class TestSchema:
    def test_eq_same_instance(self):
        schema = Schema()
        assert schema == schema

    def test_eq_different_class(self):
        schema = Schema()
        other = MagicMock()
        assert schema != other

    def test_eq_different_fields(self):
        schema1 = Schema()
        schema2 = Schema()
        
        with patch.object(schema1, 'fields', {'field1': Field()}), \
             patch.object(schema2, 'fields', {'field1': Field()}), \
             patch.object(schema1, 'field1', 'value1', create=True), \
             patch.object(schema2, 'field1', 'value2', create=True):
            assert schema1 != schema2

    def test_eq_same_fields(self):
        schema1 = Schema()
        schema2 = Schema()
        
        with patch.object(schema1, 'fields', {'field1': Field()}), \
             patch.object(schema2, 'fields', {'field1': Field()}), \
             patch.object(schema1, 'field1', 'value1', create=True), \
             patch.object(schema2, 'field1', 'value1', create=True):
            assert schema1 == schema2
