# file mimesis/builtins/pt_br.py:60-101
# lines [60, 69, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 88, 90, 91, 93, 94, 96, 98, 99, 100, 101]
# branches ['77->78', '77->79', '79->80', '79->81', '81->82', '81->83', '84->85', '84->86', '98->99', '98->101']

import pytest
from mimesis.builtins.pt_br import BrazilSpecProvider

@pytest.fixture
def brazil_provider():
    return BrazilSpecProvider()

def test_cnpj_without_mask(brazil_provider):
    cnpj = brazil_provider.cnpj(with_mask=False)
    assert len(cnpj) == 14
    assert cnpj.isdigit()

def test_cnpj_with_mask(brazil_provider):
    cnpj = brazil_provider.cnpj(with_mask=True)
    assert len(cnpj) == 18
    assert cnpj.count('.') == 2
    assert cnpj.count('/') == 1
    assert cnpj.count('-') == 1
