import pandas as pd

str = "P0100401ZJA_DCS1AI_1JZA2145_20190618_20190619.txt"

path = "C:/Users/fangjianwen/Desktop/ft2020/ori_data/#1炉数据/B310090/#1炉给煤机E数据/P0100401ZJA_DCS1AI_1JZA2151_20190601_20190602.txt"

a = pd.DataFrame([[1,2], [3,4]], columns=["A", "B"])
b = pd.DataFrame([[5,6], [7,8]], columns=["A", "B"])
c = pd.DataFrame()

str = "给煤机E"

print(str[str.find("给煤机"):str.find("给煤机")+4])
