import pandas as pd

df = pd.read_csv('/Users/robert/Downloads/stack-overflow-developer-survey-2019/survey_results_public.csv')
#df = pd.Series([1, 2, 3])
# df = tells python we're creating a new variablel called df
# pd tells Python to look at the pandas library we imported
# .read_csv('survey_results_public.csv') tells Python to use the function
# .read_csv() to read the file survey_results_public.csv
df.shape
print(df.head())
print(df.shape)
print(df['BetterLife'].value_counts())
print(df['MgrMoney'].value_counts(normalize=True))
