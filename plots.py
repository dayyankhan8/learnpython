import matplotlib.pyplot as pt
x_list = [2019,2020,2021,2022,2023]
y_list = [12000,16000,17500,25000,31000]

pt.bar(x_list,y_list)
pt.xlabel("years")
pt.ylabel("No.of cases")
pt.show()