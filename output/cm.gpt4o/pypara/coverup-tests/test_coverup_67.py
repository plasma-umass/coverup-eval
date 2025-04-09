# file pypara/dcc.py:277-293
# lines [277, 278]
# branches []

import pytest
from decimal import Decimal
import datetime
from pypara.dcc import DCCRegistry, Money, Currencies

@pytest.fixture
def setup_dcc_registry():
    # Setup any necessary state or objects here
    principal = Money.of(Currencies["USD"], Decimal(1000000), datetime.date.today())
    start = datetime.date(2007, 12, 28)
    end = datetime.date(2008, 2, 28)
    rate = Decimal(0.01)
    dcc = DCCRegistry.find("Act/Act")
    return principal, start, end, rate, dcc

def test_dcc_registry_machinery(setup_dcc_registry):
    principal, start, end, rate, dcc = setup_dcc_registry

    # Test calculate_fraction method
    fraction = dcc.calculate_fraction(start, end, end)
    assert round(fraction, 14) == Decimal('0.16942884946478')

    # Test interest calculation for normal period
    interest = dcc.interest(principal, rate, start, end, end)
    assert interest.qty == Decimal('1694.29')

    # Test interest calculation for reversed period
    interest_reversed = dcc.interest(principal, rate, end, start, start)
    assert interest_reversed.qty == Decimal('0.00')

@pytest.fixture(autouse=True)
def cleanup():
    # Cleanup code to ensure no side effects
    yield
    # Add any necessary cleanup steps here
