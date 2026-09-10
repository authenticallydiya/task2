import pandas as pd
from scipy import stats


def test_synthetic_anova_pipeline():
    # Small synthetic dataset for testing
    data = {
        "species": [
            "setosa", "setosa", "setosa",
            "versicolor", "versicolor", "versicolor",
            "virginica", "virginica", "virginica"
        ],
        "petal length (cm)": [
            1.4, 1.5, 1.3,
            4.2, 4.5, 4.1,
            5.5, 5.8, 5.6
        ]
    }

    df = pd.DataFrame(data)

    # Check that the required columns exist
    assert "species" in df.columns
    assert "petal length (cm)" in df.columns

    # Run the same type of ANOVA used in the main analysis
    groups = [
        group["petal length (cm)"].values
        for _, group in df.groupby("species")
    ]

    f_statistic, p_value = stats.f_oneway(*groups)

    # Check that the analysis produced valid results
    assert f_statistic > 0
    assert 0 <= p_value <= 1

    print("Synthetic pipeline test passed.")


if __name__ == "__main__":
    test_synthetic_anova_pipeline()