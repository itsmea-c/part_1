import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
df = pd.read_csv(r"C:\Users\saran\Downloads\studentperformance_data.csv") # load the dataset
print(df.head())  # first 5 rows
print(df.dtypes)
print(df.shape)
print("Null values: ", df.isnull().sum())
print("Null value percentage: ", (df.isnull().sum() / df.shape[0]) * 100) # null value percentage
print("Duplicate Values: ", df.duplicated().sum()) # count of duplicates
df = df.drop(columns=["parent_education", "student_id"])
print(df.shape)
print("Memory usage before conversion: ", df.memory_usage(deep=True).sum())
df["extracurricular"] = df["extracurricular"].astype("category")
print(df.dtypes)
print("Memory usage after conversion: ", df.memory_usage(deep=True).sum()) # memory usage after changing to category
print(df.describe())
print("Age Skew: ", df["age"].skew())
print("Study hours per week Skew: ", df["study_hours_per_week"].skew())
print("Attendance rate Skew: ", df["attendance_rate"].skew())
print("Previous Score Skew: ", df["previous_score"].skew())
print("Final Score Skew: ", df["final_score"].skew())
skews = {col: df[col].skew() for col in df.select_dtypes(include=[np.number]).columns}
max_skew_col = max(skews, key=lambda k: abs(skews[k]))
print("Column with highest absolute skewness:", max_skew_col, skews[max_skew_col]) # highest absolute skewness
q1_previousscore = df["previous_score"].quantile(0.25)
print("Q1 Previous Score: ", q1_previousscore)
q3_previousscore = df["previous_score"].quantile(0.75)
print("Q3 Previous Score: ", q3_previousscore)
iqr_previousscore = q3_previousscore-q1_previousscore
print("IQR Previous Score: ", iqr_previousscore) # iqr
lowerbound_previousscore = q1_previousscore - 1.5 * iqr_previousscore
print("Lowerbound Previous Score: ", lowerbound_previousscore)
upperbound_previousscore = q3_previousscore + 1.5 * iqr_previousscore
print("Upperbound Previous Score: ", upperbound_previousscore)
q1_finalscore = df["final_score"].quantile(0.25)
print("Q1 Final Score: ", q1_finalscore)
q3_finalscore = df["final_score"].quantile(0.75)
print("Q3 Final Score: ", q3_finalscore)
iqr_finalscore = q3_finalscore-q1_finalscore
print("IQR Final Score: ", iqr_finalscore) #iqr
lowerbound_finalscore = q1_finalscore - 1.5 * iqr_finalscore
print("Lowerbound Final Score: ", lowerbound_finalscore)
upperbound_finalscore = q3_finalscore + 1.5 * iqr_finalscore
print("Upperbound Final Score: ", upperbound_finalscore)
outliers_previousscore = df[(df["previous_score"] < lowerbound_previousscore) | (df["previous_score"] > upperbound_previousscore)]
print("Outliers of Previous Score: ", len(outliers_previousscore))
outliers_finalscore = df[(df["final_score"] < lowerbound_finalscore) | (df["final_score"] > upperbound_finalscore)]
print("Outliers of Final Score: ", len(outliers_finalscore))
plt.plot(df.index, df["final_score"], marker="o") # line plot
plt.title("Line Plot - Final Score Analysis")
plt.xlabel("Row Index")
plt.ylabel("Final Score")
plt.show()
df.groupby("passed")["final_score"].mean().plot.bar(color="brown") # bar chart
plt.title("Bar Chart - Mean comparison")
plt.xlabel("Passed")
plt.ylabel("Final Score Mean")
plt.show()
sns.histplot(df["attendance_rate"], bins=20, kde=True, color="blue") # histogram
plt.title("Histogram - Attendance Rate")
plt.xlabel("Attendance Rate")
plt.ylabel("Frequency")
plt.show()
sns.scatterplot(x=df["study_hours_per_week"], y=df["final_score"], color="green") # scatter plot
plt.title("Scatter Plot - Study Hours vs Final Score")
plt.xlabel("Study Hours")
plt.ylabel("Final Score")
plt.show()
sns.boxplot(x=df["passed"], y=df["final_score"], palette="Set2") # box plot
plt.title("Box Plot of Final Score")
plt.xlabel("Passed")
plt.ylabel("Final Score")
plt.show()
numeric_df = df.select_dtypes(include=["number"])
correlation_matrix = numeric_df.corr() # heat map
plt.figure(figsize=(8,6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("Heat Map")
plt.show()
absolute_correlation = correlation_matrix.abs()
np.fill_diagonal(absolute_correlation.values, 0)
highest_absolute_correlation_pair = absolute_correlation.unstack().idxmax()
print("Highest Absolute Crrelation Pairs: ", highest_absolute_correlation_pair)
attendance_rate_mean = df["attendance_rate"].mean()
attendance_rate_median = df["attendance_rate"].median()
print("Attendance Rate Mean, Attendance Rate Median: ", attendance_rate_mean, attendance_rate_median)
final_score_mean = df["final_score"].mean()
final_score_median = df["final_score"].median()
print("Final Score Mean, Final Score Median: ", final_score_mean, final_score_median) #mean, median
pearson_correlation = numeric_df.corr(method="pearson")
spearman_correlation = numeric_df.corr(method="spearman")
absolute_difference = (spearman_correlation - pearson_correlation).abs()
np.fill_diagonal(absolute_difference.values, 0)
print("Pearson Correlation Matrix: ", pearson_correlation)
print("Spearman Correlation Matrix: ", spearman_correlation)
absolute_difference_table = absolute_difference.unstack().reset_index()
absolute_difference_table.columns = ["Column1", "Column2", "AbsoluteDifference"]
absolute_difference_table = absolute_difference_table[absolute_difference_table["Column1"] < absolute_difference_table["Column2"]]
print("Absolute difference in table: ", absolute_difference_table)
absolute_difference_table = absolute_difference_table.sort_values(by="AbsoluteDifference", ascending=False).head(3) # 3 pairs with largest absolute difference
print("Three pairs with largest absolute difference in table: ", absolute_difference_table)
stat = df.groupby("passed")["study_hours_per_week"].agg(['mean', 'std', 'count']) # aggregation
print("Aggregation: ", stat)
df.to_csv("C:/Users/saran/Documents/AIML/part_1/cleaned_data.csv", index=False) # save clean dataset