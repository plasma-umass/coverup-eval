# file mimesis/providers/structure.py:102-138
# lines [122, 123, 124, 125, 136, 137]
# branches ['133->136']

import pytest
from mimesis.providers import Structure

# Assuming HTML_CONTAINER_TAGS is a dictionary available within the scope of the module
# that contains the structure.py file. If it's not, you would need to mock it accordingly.

@pytest.fixture
def structure_provider():
    return Structure()

def test_html_attribute_value_unsupported_tag(structure_provider):
    with pytest.raises(NotImplementedError) as excinfo:
        structure_provider.html_attribute_value(tag='unsupported_tag', attribute='href')
    assert 'Tag unsupported_tag or attribute href is not supported' in str(excinfo.value)

def test_html_attribute_value_unsupported_attribute(structure_provider):
    with pytest.raises(NotImplementedError) as excinfo:
        structure_provider.html_attribute_value(tag='a', attribute='unsupported_attribute')
    assert 'Tag a or attribute unsupported_attribute is not supported' in str(excinfo.value)

def test_html_attribute_value_unsupported_value_type(structure_provider, mocker):
    mocker.patch.dict('mimesis.providers.structure.HTML_CONTAINER_TAGS', {'a': {'href': 'unsupported_type'}}, clear=True)
    with pytest.raises(NotImplementedError) as excinfo:
        structure_provider.html_attribute_value(tag='a', attribute='href')
    assert 'Attribute type unsupported_type is not implemented' in str(excinfo.value)
