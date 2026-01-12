# Your code goes here. Create a dataframe matching the above diagram and assign it to the variable fruits.
import pandas as pd

fruits = pd.DataFrame({'Apples':[30],'Banana':[21]})
print(fruits)

# Your code goes here. Create a dataframe matching the above diagram and assign it to the variable fruit_sales.
fruit_sales = pd.DataFrame(
    {'Apples':[35,41],
     'Banana':[211,34]},
    index = ['2017 Sales','2018 Sales']
)
print(fruit_sales)

ingredients = pd.Series(['4 cups','1 cup','2 large' , '1 can'],name = 'Dinner')
print(ingredients)

import pandas as pd 
reviews = pd.read_csv('/Users/SAI15/Downloads/Practise_DSA_150_Days-main/Pandas/customers-100.csv')
print(reviews)

print(reviews.head())
print(reviews.head(10))
print(reviews.shape)

# Write the dataframe to a CSV file
fruit_sales.to_csv('/Users/SAI15/Downloads/Practise_DSA_150_Days-main/Pandas/fruit_sales.csv')
print("DataFrame saved to fruit_sales.csv")

animals = pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]}, index=['Year 1', 'Year 2'])
animals.to_csv('Pandas/cows_and_goats.csv')

print(pd.options.display.max_rows) 
print(pd.options.display.min_rows) 
print("--- min row--")
# creation via json file 
df_from_json = pd.read_json('/Users/SAI15/Downloads/Practise_DSA_150_Days-main/Pandas/ex.json')
print(df_from_json)

print("--- Tail with no")
print(df_from_json.tail())
print("------")
print(df_from_json)
print("----")
print(df_from_json.info())