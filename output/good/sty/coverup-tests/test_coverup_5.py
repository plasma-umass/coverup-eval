# file sty/primitive.py:181-193
# lines [181, 185, 187, 189, 191, 193]
# branches ['187->189', '187->193', '189->187', '189->191']

import pytest
from sty.primitive import Register

@pytest.fixture
def register():
    r = Register()
    r.foo = 'bar'
    r._private = 'should not be included'
    yield r
    del r.foo
    del r._private

def test_as_dict(register):
    result = register.as_dict()
    assert 'foo' in result
    assert result['foo'] == 'bar'
    assert '_private' not in result
