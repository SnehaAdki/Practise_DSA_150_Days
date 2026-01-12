import pandas as pd

# # Creating a DataFrame from a dictionary
# my_df = pd.DataFrame({'Yes':[1,231,'abc'],'No': [11,'paq',1.1]}) 

# print(my_df)

my_df_with_index = pd.DataFrame({'Yes':[1,231,'abc'],'No': [11,'paq',1.1]},index=['P1','P2','P3']) 
print(my_df_with_index)


print(my_df_with_index.loc['P1'])



# # Creating a Series from a List

# nmrl = pd.Series([10,'pqr','20'])
# print(nmrl)

# nmrl_index = pd.Series([10,'pqr','20'],index=['Price','Rating','Avg Price'])
# print(nmrl_index)

nmrl_index_name = pd.Series([10,'pqr','20'],index=['Price','Rating','Avg Price'],name = 'Product Rating Details')
print(nmrl_index_name)
