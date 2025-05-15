import pytest
import pandas as pd
import datamol as dm

def test_pandas2_dataframe_conversion():
    """
    Smoke test to ensure Datamol works with pandas >= 2.0 and RDKit >= 2024.03.6.
    """
    # Only run this check under pandas >=2.0
    major, minor, *_ = map(int, pd.__version__.split("."))
    if (major, minor) < (2, 0):
        pytest.skip("Skipping pandas <2.0 compatibility test.")

    # Fetch a sample dataframe and convert to molecules
    df = dm.data.freesolv()
    assert isinstance(df, pd.DataFrame)
    mols = dm.from_df(df)
    # Each molecule should have RDKit properties
    assert all(hasattr(m, "GetNumAtoms") for m in mols)
