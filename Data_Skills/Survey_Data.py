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

said_no = df[df['BetterLife'] == 'No']
# said_no = creates new variable and makes it equal to 'No', whats on the right side of the = sign
# df makes said_no equivalent to the dataframe, but df['BetterLife'] == 'No' only includes rows from
# df in which the answer in the BL column is equal to 'No'
print(said_no.head(3))
said_no.shape
print(said_no.shape)
print(said_no['BetterLife'].value_counts())
