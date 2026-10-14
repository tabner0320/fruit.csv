import pandas as pd
import pytest

from analysis import (
    create_sales_data,
    calculate_yearly_totals,
    calculate_fruit_totals,
    calculate_sales_growth,
)


@pytest.fixture
def sales_data():
    """Provide the fruit sales DataFrame for tests."""
    return create_sales_data()


def test_yearly_sales_totals(sales_data):
    totals = calculate_yearly_totals(sales_data)

    assert totals["2017 Sales"] == 56
    assert totals["2018 Sales"] == 75


def test_fruit_sales_totals(sales_data):
    totals = calculate_fruit_totals(sales_data)

    assert totals["Apples"] == 76
    assert totals["Bananas"] == 55


def test_sales_growth(sales_data):
    growth = calculate_sales_growth(sales_data)

    assert round(growth["Apples"], 2) == 17.14
    assert round(growth["Bananas"], 2) == 61.90


def test_yearly_totals_with_empty_data():
    """An empty dataset should return no yearly totals."""
    import pandas as pd

    empty_df = pd.DataFrame(columns=["Apples", "Bananas"])

    totals = calculate_yearly_totals(empty_df)

    assert totals.empty


def test_sales_growth_with_decreasing_sales():
    """Verify that declining sales produce negative growth."""
    import pandas as pd

    declining_data = pd.DataFrame(
        {
            "Apples": [100, 75],
            "Bananas": [80, 40],
        },
        index=["2017 Sales", "2018 Sales"]
    )

    growth = calculate_sales_growth(declining_data)

    assert growth["Apples"] == -25.0
    assert growth["Bananas"] == -50.0
