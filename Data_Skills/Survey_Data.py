import pandas as pd

df = pd.read_csv('survey_results_public_2019.csv')
# df = pd.read_csv('survey_results_public_2021.csv')
#df = pd.Series([1, 2, 3])
# df = tells python we're creating a new variablel called df
# pd tells Python to look at the pandas library we imported
# .read_csv('survey_results_public.csv') tells Python to use the function
# .read_csv() to read the file survey_results_public.csv
df.shape
# df.shape gives the size of the data set
print(df.head())
print(df.shape)
print(df['BetterLife'].value_counts())
# .value_counts() looks at a single column of data at a time and counts instances 
# of each unique entry that column contains.
# a specific column can be specified by writing the name of the dataframe like:
# df["BetterLife"].value_counts()
print()
print(df['MgrMoney'].value_counts(normalize=True))
print()

said_no = df[df['BetterLife'] == 'No']
# said_no = creates new variable and makes it equal to 'No', whats on the right side of the = sign
# df makes said_no equivalent to the dataframe, but df['BetterLife'] == 'No' only includes rows from
# df in which the answer in the BL column is equal to 'No'
print(said_no.head(3))
said_no.shape
print(said_no.shape)
print(said_no['BetterLife'].value_counts())
print()

said_yes = df[df['BetterLife'] == 'Yes']
print(said_yes.head(3))
said_yes.shape
print(said_yes.shape)
print(said_yes['BetterLife'].value_counts())
print()

print(said_no['Age'].mean(),
said_yes['Age'].mean(),
said_no['Age'].median(),
said_yes['Age'].median())
print()

over50 = df[df['Age'] >= 50]
under25 = df[df['Age'] <= 25]
print(over50['BetterLife'].value_counts(normalize=True))
print()
print(under25['BetterLife'].value_counts(normalize=True))
print()

print(len(over50))
print(len(under25))
print()

filtered_1 = df[(df['BetterLife'] == 'Yes') & (df['Country'] == 'India')]
print(filtered_1['BetterLife'].value_counts())
print(filtered_1['Country'].value_counts())
print()

filtered = df[(df['BetterLife'] == 'Yes') & (df['Age'] >= 50) & (df['Country'] == 'India') &~ (df['Hobbyist'] == "Yes") &~ (df['OpenSourcer'] == "Never")]
print(filtered)
print()

print(df["LanguageWorkedWith"].head())
print()

python_bool = df["LanguageWorkedWith"].str.contains('Python')
print(python_bool.value_counts(normalize=True))
print()

lang_lists = df["LanguageWorkedWith"].str.split(';' , expand=True)
print(lang_lists.head())
print()

print(lang_lists.stack().value_counts())
