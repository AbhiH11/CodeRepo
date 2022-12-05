import csv
import matplotlib.pyplot as plt  

# filename = 'Data/sitka_weather_07-2018_simple.csv'
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#     # print(header_row)
#     # for index,column_header in enumerate(header_row):
#     # # for index,column_header in header_row:
#     #     print(index,column_header)

#     highs = []
#     for row in reader:
#         high = int(row[5])
#         highs.append(high)
# print(highs)

# # plot the high temperatures
# plt.style.use('seaborn')
# fig,ax = plt.subplots()
# ax.plot(highs, c ='red')

# # format plots
# plt.title("Daily temperatures, july 2018",fontsize = 24)
# plt.xlabel('',fontsize = 16)
# plt.ylabel("Temperature (F)",fontsize = 16)
# plt.tick_params(axis='both',which = 'major', lablesize = 16)

# plt.show()

from datetime import datetime

first_date = datetime.strptime('2022-12-04', '%Y-%m-%d')
print(first_date)