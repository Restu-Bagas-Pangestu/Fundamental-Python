import pandas as pd

state = ['California', 'Texas', 'Florida','New York']
population =  [39613493, 29730311,21944577,19299981]

dict_states = {'States':state,'Population':population}

df_states = pd.DataFrame.from_dict(dict_states)
print (df_states)

#save file pada repository
#with open ('test.txt', 'w') as file:
#    file.write('data successfully scraped!')