# file apimd/parser.py:101-106
# lines [101, 103, 104, 106]
# branches ['103->104', '103->106']

import pytest
from apimd.parser import esc_underscore

def test_esc_underscore(mocker):
    # Test case where underscore count is more than 1
    doc_with_multiple_underscores = "test_document_with_underscores"
    expected_output = "test\\_document\\_with\\_underscores"
    assert esc_underscore(doc_with_multiple_underscores) == expected_output

    # Test case where underscore count is 1
    doc_with_one_underscore = "test_document"
    expected_output = "test_document"
    assert esc_underscore(doc_with_one_underscore) == expected_output

    # Test case where there are no underscores
    doc_with_no_underscores = "testdocument"
    expected_output = "testdocument"
    assert esc_underscore(doc_with_no_underscores) == expected_output
