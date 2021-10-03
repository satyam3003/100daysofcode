import pandas as pd
data = pd.read_csv("day25/squiral_data_analysis/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

my_data = data.pivot_table(index=['Primary Fur Color'], aggfunc='size').to_dict()
color_list = [], number_list = []
for item in my_data:
    color_list.append(item)
    number_list.append(my_data[item])
final_dict = {
    "color": color_list,
    'count': number_list
}
df = pd.DataFrame(final_dict)
df.to_csv('day25/squiral_data_analysis/squiral_data.csv')
