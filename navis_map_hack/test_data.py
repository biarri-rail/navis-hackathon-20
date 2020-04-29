import pandas as pd
from .data import get_data, get_lat_long


# Just check that it doesn't error
def test_get_data():
    get_data()


def test_get_lat_long():
    result = get_lat_long("Tasmania, Australia")
    assert result == [-42.14220555, 146.6723517878467]
