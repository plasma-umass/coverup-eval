# file: typesystem/schemas.py:204-247
# asked: {"lines": [233], "branches": []}
# gained: {"lines": [233], "branches": []}

import pytest
from typesystem.schemas import Reference, Schema

class DummySchema(Schema):
    pass

def test_reference_with_string_and_definitions():
    definitions = {"DummySchema": DummySchema}
    ref = Reference(to="DummySchema", definitions=definitions)
    assert ref.target == DummySchema

def test_reference_with_string_missing_definitions():
    ref = Reference(to="DummySchema")
    with pytest.raises(AssertionError, match="String reference missing 'definitions'."):
        _ = ref.target

def test_reference_with_class():
    ref = Reference(to=DummySchema)
    assert ref.target == DummySchema

@pytest.fixture(autouse=True)
def run_around_tests(monkeypatch):
    # Setup: nothing to setup before tests
    yield
    # Teardown: clean up any state if necessary
    monkeypatch.undo()
