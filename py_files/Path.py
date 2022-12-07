import pandas as pd
df = pd.read_csv("C:\\Users\\rajha\\OneDrive\\Desktop\\New folder\\dirtydata.csv")
#new_df = df.dropna()
#print(new_df)

#Drop Na
#df.dropna(inplace= True)

#Replace Na values with particular value
#df.fillna(145, inplace = True)

#Replace particular row:
#df["Calories"].fillna(145, inplace= True)

#Replacing with 'mean':
#x = df["Calories"].mean()
#df["Calories"].fillna(x, inplace = True)

#Replacing with 'median':
#x = df["Calories"].median()
#df["Calories"].fillna(x, inplace = True)

#Replacing with 'mode':
#x = df["Calories"].mode()[0]
#df["Calories"].fillna(x, inplace = True)

#correcting wrong date format
#df['Date'] = pd.to_datetime(df['Date'])

#DROPPING THE WRONG DATE FORMAT:
#df.dropna(subset = ["Date"], inplace = True)

#CORRECTING THE MISTAKEN VALUE:
#df.loc[7, 'Duration'] = 45

#CORRECTING WITH THE RULES:
#for x in df.index:
    #if df.loc[x, 'Duration'] > 120:
        #df.loc[x, 'Duration'] = 120

#DROPPING THE WRONG NUMBER:
for x in df.index:
    if df.loc[x, 'Duration'] > 120:
        df.drop(x, inplace = True)
print(df)