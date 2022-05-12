import pandas as pd
df = pd.read_csv("C:\Users\rajha\OneDrive\Desktop\New folder\\")
#pd.options.display.max_rows= 9999
#print(pd.options.display.max_rows)
#print(df.tail(10))
#print(df.info())
#new_df = df.dropna()
#print(new_df.to_string())
df = df.head(101)
print(df.to_string())
#print(df.to_string())
#print(df.tail())
#print(df.to_string())
#print(df.to_string())