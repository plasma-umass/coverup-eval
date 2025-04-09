# file mimesis/builtins/pl.py:88-101
# lines [88, 93, 94, 95, 96, 97, 98, 99, 100, 101]
# branches ['98->99', '98->100']

import pytest
from mimesis.builtins.pl import PolandSpecProvider
from unittest.mock import patch

@pytest.fixture
def poland_spec_provider():
    return PolandSpecProvider()

def test_regon(poland_spec_provider):
    with patch.object(poland_spec_provider.random, 'randint', side_effect=[8, 7, 6, 5, 4, 3, 2, 1]):
        regon = poland_spec_provider.regon()
        assert len(regon) == 9
        assert regon.isdigit()
        assert regon == '876543216'

    with patch.object(poland_spec_provider.random, 'randint', side_effect=[9, 9, 9, 9, 9, 9, 9, 9]):
        regon = poland_spec_provider.regon()
        assert len(regon) == 9
        assert regon.isdigit()
        assert regon == '999999990'
