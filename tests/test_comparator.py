import pandas as pd
import pytest
from exceldiffy.comparator import Comparator


@pytest.fixture
def sample_data():
    # Sample data with duplicate composite keys
    df1 = pd.DataFrame({
        "CUSTOMER_NAME": ["Alice", "Bob", "Charlie"],
        "SECTOR": ["Tech", "Finance", "Healthcare"],
        "OUTSTANDING BALANCE (USD)": [1000, 2000, 1500],
    })

    df2 = pd.DataFrame({
        "CUSTOMER_NAME": ["Alice", "Bob", "Charlie", "Alice"],
        "SECTOR": ["Tech", "Finance", "Healthcare", "Tech"],
        "OUTSTANDING BALANCE (USD)": [1100, 2000, 1450, 1080],
    })

    return df1, df2


def test_calculate_pct_change():
    comparator = Comparator()
    assert comparator.calculate_pct_change(100, 110) == 10.0
    assert comparator.calculate_pct_change(100, 90) == -10.0
    assert comparator.calculate_pct_change(0, 100) is None  # Avoid division by zero


def test_compare_dataframes(sample_data):
    """Test the dataframe comparison functionality with duplicate keys."""
    df1, df2 = sample_data
    comparator = Comparator()
    key_columns = ['CUSTOMER_NAME', 'SECTOR']
    compare_columns = ['OUTSTANDING BALANCE (USD)']
    results = comparator.compare_dataframes(df1, df2, key_columns, compare_columns)

    assert 'OUTSTANDING BALANCE (USD)' in results
    changes = results['OUTSTANDING BALANCE (USD)']['data']

    # Expect 3 changes: two for Alice|Tech (due to duplicates), one for Charlie|Healthcare
    assert len(changes) == 3

    keys = changes['key'].tolist()
    assert keys.count('Alice|Tech') == 2
    assert 'Charlie|Healthcare' in keys


def test_display_comparison(capsys, sample_data):
    """Test the display of comparison results."""
    df1, df2 = sample_data
    comparator = Comparator()
    key_columns = ['CUSTOMER_NAME', 'SECTOR']
    compare_columns = ['OUTSTANDING BALANCE (USD)']
    results = comparator.compare_dataframes(df1, df2, key_columns, compare_columns)

    # Capture the printed output
    comparator.display_comparison(results)
    captured = capsys.readouterr()

    assert "Changes in 'OUTSTANDING BALANCE (USD)'" in captured.out
    assert "Total rows with changes: 3" in captured.out
    assert "Alice|Tech" in captured.out
    assert "Charlie|Healthcare" in captured.out
