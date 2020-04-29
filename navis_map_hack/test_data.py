import pandas as pd
from .data import get_data


# Just check that it doesn't error
def test_get_data():
    get_data()
