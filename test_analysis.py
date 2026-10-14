
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
