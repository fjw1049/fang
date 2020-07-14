from readData import *


if __name__ == '__main__':
    print("我实在是太菜了。")
    path = "C:/Users/fangjianwen/Desktop/ft2020/ori_data/#1炉数据/B310090"  # 文件夹目录
    data_read(path)

    data_str = "C:/Users/fangjianwen/Desktop/ft2020/ori_data"

    generator = {}
    for path_i in os.listdir(data_str):
        print(path_i)
        generator_name = path_i[path_i.find("炉") - 1:path_i.find("炉") + 1]
        for path_j in os.listdir(data_str + "/" + path_i):
            print("\t" + path_j)
            generator[generator_name] = data_read(data_str + "/" + path_i + "/" + path_j)
