import pandas as pd

# Save to CSV file
my_df = pd.read_csv('/Users/SAI15/Downloads/Practise_DSA_150_Days-main/Pandas/cleaning_data.csv')



print(my_df)
print("Max is ",end="")
print(my_df['Calories'].max())
print("Min is ",end="")
print(my_df['Calories'].min())
print("Sum is ",end="")
print(my_df['Calories'].sum())
print("Mean is ",end="")
print(my_df['Calories'].mean())
print("Mode is ",end="")
print(my_df['Calories'].mode())
print("Median is ",end="")
print(my_df['Calories'].median())
print("Count is ",end="")
print(my_df['Calories'].count())

breakpoint()

print(my_df.dropna(subset = ['Date'],inplace =True))
print(my_df)