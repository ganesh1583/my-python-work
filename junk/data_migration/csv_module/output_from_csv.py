import csv
import os


def get_data_from_csv_file():
    while True:
        try:
            path = input("Enter file name : ")
            if os.path.exists(path):
                pass
            else:
                print("File", path.split("/")[-1], "does not exist !!!")
                continue
        except FileNotFoundError as fe:
            print("File Not Found")
        except PermissionError as pe:
            print("Permission denied !!!")
        except Exception as e:
            print("Exception : ",e)
        else:
            """
            with open(path,"r") as f:
                column_names = f.readline()
            column_names = column_names.split(",")
            column_names[-1] = column_names[-1][:-1:]
            """
            f = open(path,"r")
            w = csv.reader(f)
            for data in w:
                print(data)
            f.close()
            break
