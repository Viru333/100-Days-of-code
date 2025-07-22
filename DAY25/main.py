# with open("weather_data.csv") as f:
#     Lines_list = f.readlines()
#     print(Lines_list)
#

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             t = int(row[1])
#             temperatures.append(t)
#
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
# print(data)
# print(type(data))

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)
# print(type(temp_list))

# average = data["temp"].mean()
# print(average)
#
# max_temp = data["temp"].max()
# print(max_temp)

# Get data in columns
# print(data["condition"])

# print(data.condition)

# Get data in rows

# monday = data[data.day == "Monday"]
# print(data[data.temp == max_temp])
# print(monday.condition)
# degree_c = monday.temp[0]
# degree_f = (9*degree_c)/5 + 32
# print(degree_f)


# Create a dataframes from scratch
# data_dict = {
#     "students": ["Any", "James", "Angela"],
#     "score": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

# fur_count = {
#     "fur color": [],
#     "squirrel count": [],
# }
#
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# fur_colors = data["Primary Fur Color"]
# fur_list = fur_colors.to_list()
# for fur in fur_list:
#     if fur == "":
#         continue
#     elif fur not in fur_count["fur color"]:
#         fur_count["fur color"].append(fur)
#         fur_count["squirrel count"].append(1)
#     else:
#         fur_count["squirrel count"][fur_count["fur color"].index(fur)] += 1
#
#
# fur_data = pandas.DataFrame(fur_count)
# fur_data.to_csv("squirrel_count.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrel_cnt = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrel_cnt = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_cnt = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel_cnt, cinnamon_squirrel_cnt, black_squirrel_cnt]
}

file = pandas.DataFrame(data_dict)
file.to_csv("squirrel_count.csv")