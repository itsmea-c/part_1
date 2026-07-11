This is Part 1 of Capstone Project where Data Acquisition, Cleaning, and Exploratory Analysis have been performed

The dataset which we have taken is Student Performance data which has numerical final_score column for Linear Regression model and categorical passed column for
Logistic Regression model

1. Load the dataset: Loaded the dataset into a pandas DataFrame using pd.read_csv(). Printed the first five rows, the column data types and the DataFrame shape.
2. Null value analysis: Computed the count and percentage of missing values in every column. parent_education column exceeded 20% null rate and it was not strong for target prediction hence dropped that column. Apart from that there are no null values in any column
3. Duplicate detection and removal: Counted the number of duplicate rows and found no duplicate rows so no change in the data
4. Data type correction: Validated the datatype of all columns and they were stored with the correct datatype. Converted one repetitive string column (extracurricular) to Category datatype and found the memory usage before and after conversion. Memory usage was less after conversion
5. Descriptive statistics and skewness: Performed descriptive statistics and skewness in all columns. attendance_rate column has the highest absolute skewness. Positive Skew means most students will have low or medium attendance rate and few students will have high attendance rate and it will pull the mean upward. Negative Skew means most students will have high attendance rate and few students will have low attendance rate and it will pull the mean downward. Mean is sensitive to outliers and so imputing null values with mean in this scenario will bias the dataset and hence imputing the null values with median is preferred
6. Outlier detection with IQR: Computed Q1, Q3, IQR, lower bound and upper bound for two numeric columns previous_score and final_score. Counted the number of rows that fall outside these bounds and there are no outliers found
7. Visualizations:
    1. Line Plot: A line plot of a numerical variable Final Score sorted by row index is produced
    2. Bar Chart: A bar chart comparing the mean of one numeric column (Final Score) across categories of one categorical column (Passed) is produced
    3. Histogram: A histogram of the most skewed numeric column (attendance_rate) is produced. The distribution is slightly right skewed so it is positive skew            which means few students have high attendance rate
    4. Scatter Plot: A scatter plot between two numeric columns study_hours_per_week and final_score is produced
