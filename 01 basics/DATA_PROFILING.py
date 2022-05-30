# pip install pandas
# pip install pandas-profiling
import pandas as pd 
from pandas_profiling import ProfileReport

df = pd.read_csv('cars_engage_2022.csv')
# print(df)

# Generate a report
profile = ProfileReport(df)
profile.to_file(output_file="cars.html")