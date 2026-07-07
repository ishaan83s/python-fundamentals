import pandas as pd
df = pd.read_csv('side_quests/csv file handling/student_scores.csv')

#PRINTS ALL THE DATA
print(df) #PRINTS ALL THE DATA

# PRINTS FIRST 5 ROWS
print(df.head()) #PRINTS FIRST 5 ROWS (USED for getting familiarity /info of the data)

#PRINTS NUMBER OF ROWS AND COLUMNS
print(df.shape) #prints number of rows and columns

#SHOWS ALL THE COLUMNS NAMES
print(df.columns) #shows column names

# AVERAGE OF THE "marks" COLUMN
print(df['marks'].mean()) #PRINTS average of the marks column

# HOW TO FIND TOPPER (and prints its details):
topper = df.loc[df['marks'].idxmax()]
print(topper['name'],topper['marks'])

#AVERAGE MARKS PER SUBJECT :
print(df.groupby("subject")['marks'].mean())