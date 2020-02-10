import subprocess
import multiprocessing
import re
import time
import os
from multiprocessing import Process

def GetNewInfo(command, fileName):
    first_list = str(subprocess.check_output(command, shell=True), encoding="utf-8").split("\n")
    Dup_check_list = []
    while True:
        check_new_list = str(subprocess.check_output(command, shell=True), encoding="utf-8").split("\n")
        for item in check_new_list:
            if item in first_list:
                check_new_list.remove(item)
        
        for item in check_new_list:
            with open(fileName, "w+") as f:
                if item in Dup_check_list or item == "":
                    pass
                else:
                    f.write(item + "\n")
                    Dup_check_list.append(item)

def GetNewinfo_Size(file_path, write_path):
    file_size = os.path.getsize(file_path)
    file_size_compare = os.path.getsize(file_path)
    if file_size != file_size_compare:
        f = open(file_path, "rb")
        pointer1 = f.seek(file_size)
        pointer2 = f.seek(file_size_compare)

        f.seek(pointer1)
        data = str(f.read(pointer2-pointer1), encoding="utf-8")

        with open(write_path, "w+") as w:
            w.write(data)