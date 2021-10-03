# ------------- extracting data from csv using CSV package -----------
#
# import csv
#
# with open('day25/weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     data_list = []
#     temperature = []
#     for rows in data:
#         data_list.append(rows)
#         try:
#             temperature.append(int(rows[1]))
#         except:
#             pass
#     print(temperature)

# -------------- using pandas -----------------
import pandas as pd

data = pd.read_csv('day25/weather_data.csv')
temp_list = data['temp'].to_list()
# print(temp_list)

# ------------ finding mean temp --------------
# method 1
# avg = sum(temp_list)/len(temp_list)
# print(avg)

# method 2
# print(data['temp'].mean())
#
# # ------------ finding max -----------
# print(data['temp'].max())

# --------------- getting row elements ----------
# print(data[data.day == 'Monday'])

# day = data[data.day == 'Monday']
# print(int(day.temp) * 1.8 + 32)  # temperature in F


# ------------- creating data frame from python ------------
data_dict = {
    'student_name': ['Satyam', 'Smritu', 'Sallu'],
    'scores': [99,67,45]
}

my_data = pd.DataFrame(data_dict)
print(my_data)
# my_data.to_csv("day25/marks.csv")






