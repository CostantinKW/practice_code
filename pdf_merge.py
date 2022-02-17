#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：practice_code 
@File    ：pdf_merge.py
@IDE     ：PyCharm 
@Author  ：孔令伟
@Date    ：2/17/22 4:06 PM 
'''
import os
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger
import time


def GetileList(filedir):
    """
    :param filedir:
    :return: ["/root/workspace/practice_code/test_file/test.pdf"]
    """
    # 获取待合并的pdf文件路径列表
    file_list = [os.path.join(root, filespath) \
                 for root, dirs, files in os.walk(filedir) \
                 for filespath in files \
                 if str(filespath).endswith("pdf")]

    return file_list if file_list else []


def PdfMerge(file_dir, file_name):
    """
    :return:
    """
    try:
        file_list = GetileList(filedir=file_dir)
        # 开始pdf文件合并
        output = PdfFileWriter()
        for file_url in file_list:
            # 读取pdf文件内容
            input = PdfFileReader(open(file_url, "rb"))
            input_pagecount = input.getNumPages()
            # 分别将每一页内容合并至output
            for input_page in range(input_pagecount):
                output.addPage(input.getPage(input_page))

            output_stream = open(os.path.join(file_dir, file_name), "wb")
            output.write(output_stream)
            output_stream.close()

    except Exception as e:
        raise str(e)


def main():
    # 需要合并的pdf文件所处的文件夹路径
    target_dir = "/root/workspace/practice_code/test_file"
    # 合并后的pdf文件名称
    output_file_name = "output.pdf"
    print("开始合并路径{}下的pdf文件".format(target_dir))
    PdfMerge(target_dir, output_file_name)
    print("已合并内容至文件{}/{}".format(target_dir, output_file_name))


if __name__ == "__main__":
    time1 = time.time()
    main()
    time2 = time.time()
    seconds = time2 - time1
    print("耗时{}秒".format(seconds))
