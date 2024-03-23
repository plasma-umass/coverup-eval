# file mimesis/enums.py:191-218
# lines [191, 192, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218]
# branches []

import pytest
from mimesis.enums import UnitName

@pytest.mark.parametrize("unit_enum, expected", [
    (UnitName.MASS, ('gram', 'gr')),
    (UnitName.INFORMATION, ('byte', 'b')),
    (UnitName.THERMODYNAMIC_TEMPERATURE, ('kelvin', 'K')),
    (UnitName.AMOUNT_OF_SUBSTANCE, ('mole', 'mol')),
    (UnitName.ANGLE, ('radian', 'r')),
    (UnitName.SOLID_ANGLE, ('steradian', '㏛')),
    (UnitName.FREQUENCY, ('hertz', 'Hz')),
    (UnitName.FORCE, ('newton', 'N')),
    (UnitName.PRESSURE, ('pascal', 'P')),
    (UnitName.ENERGY, ('joule', 'J')),
    (UnitName.POWER, ('watt', 'W')),
    (UnitName.FLUX, ('watt', 'W')),
    (UnitName.ELECTRIC_CHARGE, ('coulomb', 'C')),
    (UnitName.VOLTAGE, ('volt', 'V')),
    (UnitName.ELECTRIC_CAPACITANCE, ('farad', 'F')),
    (UnitName.ELECTRIC_RESISTANCE, ('ohm', 'Ω')),
    (UnitName.ELECTRICAL_CONDUCTANCE, ('siemens', 'S')),
    (UnitName.MAGNETIC_FLUX, ('weber', 'Wb')),
    (UnitName.MAGNETIC_FLUX_DENSITY, ('tesla', 'T')),
    (UnitName.INDUCTANCE, ('henry', 'H')),
    (UnitName.TEMPERATURE, ('Celsius', '°C')),
    (UnitName.RADIOACTIVITY, ('becquerel', 'Bq')),
])
def test_unit_name_enum(unit_enum, expected):
    assert unit_enum.value == expected
