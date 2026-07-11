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
    2. Bar Chart: A bar chart comparing the mean of one numeric column (final_score) across categories of one categorical column (passed) is produced
    3. Histogram: A histogram of the most skewed numeric column (attendance_rate) is produced. The distribution is slightly right skewed so it is positive skew          which means few students have high attendance rate
    4. Scatter Plot: A scatter plot between two numeric columns study_hours_per_week and final_score is produced. The scatter plot shows a strong positive linear        relationship between study hours and final score and the points form an upward trend that means when study hours increase final scores also increase.             There is a strong correlation between these two numeric columns
    5. A box plot of a numeric column (final_score) split by a categorical column (passed) is produced. The The box plot shows that students who passed have             higher median final score and students who did not pass have lower scores
8. Correlation heat map: Computed the correlation matrix of all numeric columns and visualized it with a heat map. Identified study_hours_per_week and final_score as the pair of variables with the highest absolute correlation. The highest correlation indicates the string relationship between study_hours_per_week and final_score. If the study hours is increased the final score is getting increased but other factors like attendance_rate and prior knowledge could also increase the final score
9. a. Imputation strategy comparison: For the two numeric columns with the highest absolute skewness identified in Task 5 (attendance_rate and final_score), we have computed both the column mean and the column median. Printed both values for each column. There are no null columns and no imputation is done. However if any null value is present we will impute with median values as positive skew will pull the mean upward and negative skew will pull the mean downward
   b. Spearman rank correlation: Computed Spearman and Pearson rank correlation matrix for all numeric columns. Identified the three column pairs where the absolute difference between the Spearman correlation and the Pearson correlation is largest. Printed both matrices and a difference table showing |Spearman − Pearson| for each pair.
      Three Pairs:
      attendance_rate, final_score
      a) Pearson ≥ Spearman, indicating an approximately linear relationship
      b) Rely on Pearson correlation measure as it has an approximate linear relationship
      age, final_score
      a) Spearman > Pearson, indicating monotonic but non-linear relationship
      b) Rely on Spearman correlation measure as it has non-linear relationship
      final_score, study_hours_per_week
      a) Spearman > Pearson, indicating monotonic but non-linear relationship
      b) Though it indicates Spearman > Pearson and it has non-linear relationship we will rely on Pearson correlation measure because the difference between              Spearman and Pearson correlation measure is very less and there is a strong correlation between final_score and study_hours_per_week
   
   
