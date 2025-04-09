# file: pypara/exchange.py:81-93
# asked: {"lines": [81, 93], "branches": []}
# gained: {"lines": [81, 93], "branches": []}

import datetime
from decimal import Decimal
from pypara.currencies import Currencies
from pypara.exchange import FXRate

def test_fxrate_invert():
    nrate = FXRate(Currencies["EUR"], Currencies["USD"], datetime.date.today(), Decimal("2"))
    rrate = FXRate(Currencies["USD"], Currencies["EUR"], datetime.date.today(), Decimal("0.5"))
    assert ~nrate == rrate
