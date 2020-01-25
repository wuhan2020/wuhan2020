#coding=utf-8
# 代码使用csvvalidator作为检查工具，repo链接：https://github.com/alimanfoo/csvvalidator
# 使用exe或可执行文件，可以通过pyinstaller  -F csv_checker.py生成
# vscode插件可以查看csv表格效果

import os
import sys
import csv
from pathlib import Path
from csvvalidator import *


# 验证数据，并打印问题。
# 待检测文件夹，repo根目录
directory = Path("./")  # FIXME: 可以此处修改，如果生成可执行文件，直接设为当前路径最好
# 所有csv文件，假设根目录下的csv都需要检测
csv_files = list(directory.glob("*.csv"))
for file_name in csv_files:
    # validate the data and write problems to stdout
    with open(file_name, encoding="utf-8") as csvfile:
        # 根据csv首行判断该文件检查条目
        head = csvfile.readline().strip()
        titles = head.split(',')
        field_names = [o.strip() for o in titles]    # 去首行不规范空格

        # 构建 检测器
        validator = CSVValidator(tuple(field_names))

        # 添加检查项，列长度
        validator.add_record_length_check('EX0', '记录条目长度不正确')

        # 按条目添加检查项，目前没有实际意义，因为都是字符串
        # TODO: 如果有需要检查是否数字等特殊需求，可以再add_value_check中特别指定
        count = 0
        for item in field_names:
            validator.add_value_check(item, str, 'EX'+str(count), '确认数据类型')

        # 读文件并检查
        data = csv.reader(csvfile, delimiter=',')
        problems = validator.validate(data)

        # 打印报告
        print("\r\n检查文件：", file_name.name, '**************************************')
        write_problems(problems, sys.stdout)

        # TODO: 后期如果需要自动判断，可以通过判断problems项的长度，0表示有误
        if len(problems) > 0:
            print('**************************************', file_name.name, "有问题")  # TODO： 添加需要的步骤
            os.system('pause')
        else:
            print('**************************************', file_name.name, "没问题")
            os.system('pause')

os.system('pause')  # 怕exe一闪而过