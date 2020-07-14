import os
import pandas as pd


def data_read(data_path):
    """
    :param data_path: file need to read
    :return:
    """
    files = os.listdir(data_path)  # 得到文件夹下的所有文件名称

    coal_machine = {}
    for coal_machine_path in files:  # 遍历文件夹
        if "给煤机" in coal_machine_path:
            print("正在读取 " + coal_machine_path + " 数据。")

            coal_machine_files = os.listdir(data_path + "/" + coal_machine_path)

            one_coal_machine_pd = pd.DataFrame()  # 单台数据存储到一个DateFrame里面。
            for coal_machine_file in coal_machine_files:
                one_file_pd = read_data_from_file(data_path + "/" + coal_machine_path + "/" + coal_machine_file)
                one_coal_machine_pd = pd.concat([one_file_pd, one_coal_machine_pd])

            machine_name = coal_machine_path[coal_machine_path.find("给煤机"):coal_machine_path.find("给煤机")+4]
            coal_machine[machine_name] = one_coal_machine_pd

    return coal_machine


def read_data_from_file(file_path):
    """
    :param file_path: the file which need to read by line
    :return: file line DataFrame
    """
    file_lines = list()

    file = open(file_path)
    for line in file:
        file_lines.append([line.split()[0] + ' ' + line.split()[1], line.split()[2]])
    file.close()

    file_lines_pd = pd.DataFrame(file_lines, columns=['DateTime', 'coal_value'])
    file_lines_pd['DateTime'] = pd.to_datetime(file_lines_pd['DateTime'], format='%Y-%m-%d %H:%M:%S')
    file_lines_pd.sort_values("DateTime", inplace=True)

    return file_lines_pd
