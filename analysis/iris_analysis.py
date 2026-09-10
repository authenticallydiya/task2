from pathlib import Path
import pandas as pd
from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Find the project folder
BASE_DIR = Path(__file__).resolve().parents[1]

# File locations
DATA_PATH = BASE_DIR / "data" / "iris.csv"
RESULTS_DIR = BASE_DIR / "results"
RESULTS_DIR.mkdir(exist_ok=True)

# Load the Iris dataset
df = pd.read_csv(DATA_PATH)

# Keep only the variables needed for this analysis
df = df.dropna(subset=["species", "petal length (cm)"])

# Calculate summary statistics
summary = (
    df.groupby("species")["petal length (cm)"]
    .agg(["count", "mean", "std"])
    .reset_index()
)

# Calculate 95% confidence intervals
ci_low = []
ci_high = []

for _, row in summary.iterrows():
    n = int(row["count"])
    mean = row["mean"]
    sd = row["std"]

    standard_error = sd / (n ** 0.5)
    t_critical = stats.t.ppf(0.975, n - 1)

    ci_low.append(mean - t_critical * standard_error)
    ci_high.append(mean + t_critical * standard_error)

summary["ci_low_95"] = ci_low
summary["ci_high_95"] = ci_high

# Perform one-way ANOVA
groups = [
    group["petal length (cm)"].values
    for _, group in df.groupby("species")
]

f_statistic, p_value = stats.f_oneway(*groups)

# Save summary statistics
summary.to_csv(
    RESULTS_DIR / "summary_statistics.csv",
    index=False
)

# Save ANOVA results
with open(RESULTS_DIR / "anova_results.txt", "w") as file:
    file.write("One-Way ANOVA Results\n")
    file.write("=====================\n")
    file.write(f"F-statistic: {f_statistic:.4f}\n")
    file.write(f"p-value: {p_value:.6f}\n")
    file.write("Significance level: 0.05\n")

# Perform Tukey's HSD if ANOVA is significant
if p_value < 0.05:
    tukey = pairwise_tukeyhsd(
        endog=df["petal length (cm)"],
        groups=df["species"],
        alpha=0.05
    )

    tukey_table = pd.DataFrame(
        data=tukey.summary().data[1:],
        columns=tukey.summary().data[0]
    )

    tukey_table.to_csv(
        RESULTS_DIR / "tukey_results.csv",
        index=False
    )

print("Analysis completed successfully.")
print("\nSummary statistics:")
print(summary)
print(f"\nANOVA F-statistic: {f_statistic:.4f}")
print(f"ANOVA p-value: {p_value:.6f}")

if p_value < 0.05:
    print("\nANOVA is statistically significant.")
    print("Tukey HSD results were saved.")
else:
    print("\nANOVA is not statistically significant.")