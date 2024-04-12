# file src/blib2to3/pytree.py:800-809
# lines [802, 803, 804, 805, 806, 807, 808, 809]
# branches ['802->803', '802->809', '803->802', '803->804', '804->805', '804->808', '806->807', '806->808']

import pytest
from blib2to3.pytree import WildcardPattern, LeafPattern
from blib2to3.pgen2.token import NAME

class TestWildcardPattern:
    @pytest.fixture
    def cleanup(self, mocker):
        # Setup fixture to clean up any global state after the test
        yield
        mocker.stopall()

    def test_wildcard_pattern_match_seq_full_coverage(self, mocker, cleanup):
        # Create a WildcardPattern with a name and content
        content = [(LeafPattern(NAME, 'foo'),)]
        wildcard = WildcardPattern(content=content, name='wildcard')
        # Create a mock node that will be used to match the pattern
        mock_node = mocker.MagicMock()
        mock_node.type = NAME
        mock_node.value = 'foo'
        # Set up the generate_matches method to return a match with the correct count
        mocker.patch.object(wildcard, 'generate_matches', return_value=[(1, {})])
        # Create a results dictionary to be updated
        results = {}

        # Call match_seq with a single node and the results dictionary
        matched = wildcard.match_seq([mock_node], results)

        # Assert that the match was successful
        assert matched
        # Assert that the results dictionary was updated with the wildcard name
        assert 'wildcard' in results
        # Assert that the list of nodes is stored in the results under the wildcard name
        assert results['wildcard'] == [mock_node]
