# Analysis Preregistration

## Research question
How accurately can iris flower species be predicted using sepal and petal measurements?

## Hypotheses
*Null hypothesis (H0):* The classification models cannot reliably predict iris flower species better than a simple baseline approach.

*Alternative hypothesis (H1):* The classification models can reliably predict iris flower species using sepal and petal measurements.

*Expected direction:* Petal measurements are expected to provide strong information for distinguishing the three iris species.

## Population, sample, and exclusions
*Target population:* Iris flowers represented in the selected Iris dataset.

*Unit of analysis:* One iris flower.

*Outcome variable:* Iris species.

*Predictor variables:* Sepal length, sepal width, petal length, and petal width.

*Inclusion rules:* Include observations containing all four measurements and the species label.

*Exclusion rules:* Exclude observations with missing values in the outcome or predictor variables.

*Stopping rule:* Use all eligible observations in the selected dataset. No observations will be removed based on model performance.

## Variables and measures
*Outcome:* Iris species with three classes: setosa, versicolor, and virginica.

*Predictors:*
- Sepal length
- Sepal width
- Petal length
- Petal width

*Transformations:* Numerical measurements will be used in their original units. Features may be standardized when required by the selected model.

*Missing data:* Rows with missing predictor or outcome values will be excluded.
## Analysis plan
First, calculate the mean and standard deviation of petal length for each iris species.

The primary analysis will use a one-way ANOVA to test whether mean petal length differs among the three species.

The significance level will be alpha = 0.05.

Report the F-statistic, p-value, group means, and 95% confidence intervals.

If the overall ANOVA is statistically significant, conduct Tukey's HSD post-hoc comparisons to determine which species differ.

As a robustness check, inspect the distribution of petal length within each species and report whether the conclusions are sensitive to the assumptions of ANOVA.

## Deviations
No deviations are planned at the time of preregistration.

If a deviation becomes necessary, record the date, reason, and description of the change.