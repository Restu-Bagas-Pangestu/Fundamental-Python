import pandas as pd

##membuat variable kolom
state = ['California', 'Texas', 'Florida','New York']
population =  [39613493, 29730311,21944577,19299981]

##membuat dictionary/gabungan dari beberapa kolom
dict_states = {'States':state,'Population':population}

##membuat dataframe
df_states = pd.DataFrame.from_dict(dict_states)
print (df_states)

##save dataframe dalam csv
df_states.to_csv('states.csv', index = False) #index false membuat nomor index hilang



##save file pada repository
#with open ('test.txt', 'w') as file:
#    file.write('data successfully scraped!')