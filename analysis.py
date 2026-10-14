
import pandas as pd
import matplotlib.pyplot as plt


# --------------------------------------------------
# 1. Create the fruit sales dataset
# --------------------------------------------------

def create_sales_data():
    """Create a DataFrame containing fruit sales data."""
    data = {
        "Apples": [35, 41],
        "Bananas": [21, 34]
    }

    index = ["2017 Sales", "2018 Sales"]

    return pd.DataFrame(data, index=index)


# --------------------------------------------------
# 2. Calculate total sales by year
# --------------------------------------------------

def calculate_yearly_totals(dataframe):
    """Calculate total fruit sales for each year."""
    return dataframe.sum(axis=1)


# --------------------------------------------------
# 3. Calculate total sales by fruit
# --------------------------------------------------

def calculate_fruit_totals(dataframe):
    """Calculate total sales for each fruit."""
    return dataframe.sum(axis=0)


# --------------------------------------------------
# 4. Calculate percentage growth
# --------------------------------------------------

def calculate_sales_growth(dataframe):
    """Calculate percentage growth from 2017 to 2018."""
    sales_2017 = dataframe.loc["2017 Sales"]
    sales_2018 = dataframe.loc["2018 Sales"]

    growth = ((sales_2018 - sales_2017) / sales_2017) * 100

    return growth


# --------------------------------------------------
# 5. Create the fruit sales comparison chart
# --------------------------------------------------

def create_sales_comparison_chart(dataframe):
    """Create and save a bar chart comparing yearly sales."""
    ax = dataframe.plot(kind="bar", figsize=(9, 5))

    ax.set_title("Fruit Sales Comparison: 2017 vs 2018")
    ax.set_xlabel("Year")
    ax.set_ylabel("Sales")
    ax.set_xticklabels(["2017", "2018"], rotation=0)

    plt.tight_layout()
    plt.savefig("fruit-sales-comparison.png")
    plt.close()

    print("\nChart saved as fruit-sales-comparison.png")


# --------------------------------------------------
# 6. Create the percentage growth chart
# --------------------------------------------------

def create_sales_growth_chart(growth):
    """Create and save a chart showing sales growth by fruit."""
    ax = growth.plot(
        kind="bar",
        figsize=(8, 5),
        color=["green", "orange"]
    )

    ax.set_title("Fruit Sales Growth: 2017 to 2018")
    ax.set_xlabel("Fruit")
    ax.set_ylabel("Growth (%)")
    ax.set_xticklabels(growth.index, rotation=0)

    # Display percentage labels above each bar
    for i, value in enumerate(growth):
        ax.text(
            i,
            value + 1,
            f"{value:.2f}%",
            ha="center"
        )

    plt.tight_layout()
    plt.savefig("fruit-sales-growth.png")
    plt.close()

    print("\nChart saved as fruit-sales-growth.png")


# --------------------------------------------------
# 7. Main application
# --------------------------------------------------

def main():
    """Run the fruit sales analysis."""

    # Create the sales dataset
    df = create_sales_data()

    # Export dataset to CSV
    df.to_csv("fruit.csv")
    print("DataFrame has been written to 'fruit.csv'.")

    # Calculate yearly totals
    yearly_totals = calculate_yearly_totals(df)

    print("\nTotal Sales by Year:")
    print(yearly_totals)

    # Calculate fruit totals
    fruit_totals = calculate_fruit_totals(df)

    print("\nTotal Sales by Fruit:")
    print(fruit_totals)

    # Calculate sales growth
    growth = calculate_sales_growth(df)

    print("\nSales Growth from 2017 to 2018:")
    print(growth.round(2).astype(str) + "%")

    # Generate charts
    create_sales_comparison_chart(df)
    create_sales_growth_chart(growth)

    print("\nFruit Sales Analysis completed successfully!")


# --------------------------------------------------
# 8. Run the application
# --------------------------------------------------

if __name__ == "__main__":
    main()
