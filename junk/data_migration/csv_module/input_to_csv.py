import csv
import os
from csv import *

from myio.basic_inputs import get_int, get_data_for_csv, get_string


def input_to_new_csv_file():
    try:
        path = input("Enter new csv file name : ")
        f = open(path, "w", newline="")
    except OSError as e:
        print("Disk Exhausted !!!")
    except ValueError as ve:
        print("File name contradicts conventions !!!")
    except Exception as e:
        print("Exception : ", e)
    else:
        column_names = list()
        row_data = list()
        datatypes = dict()
        w = writer(f)
        n = get_int("Enter total no of columns : ")
        print("Enter columns name one by one : ")

        for i in range(n):
            column_names.append(input("Enter column name : "))
            datatypes[column_names[i]] = input(f"Enter data type for {column_names[i]} (int/str/float/bool/NULL) : ")
        print(datatypes)
        w.writerow(column_names)

        m = get_int("Enter total no of rows : ")
        for i in range(m):
            for j in range(n):
                temp_L = get_data_for_csv(datatypes[column_names[j]], column_names[j])
                row_data = row_data + temp_L
            w.writerow(row_data)
            row_data.clear()

        f.close()


def input_to_existing_csv_file():
    while True:
        try:
            path = input("Enter existing file name : ")
            if os.path.exists(path):
                pass
            else:
                print("File", path.split("/")[-1], "does not exist !!!")
                continue
        except FileNotFoundError as fe:
            print("File Not Found:", fe)
        except PermissionError as pe:
            print("Permission denied:", pe)
        except io.UnsupportedOperation as v:
            print("Error bro")
        except Exception as e:
            print("Exception : ",e)
        else:
            with open(path, "r") as f:
                data = f.readline()
            datatypes = dict()
            column_names = data.split(",")
            row_data = list()
            column_names[-1] = column_names[-1][:-1:]

            for i in range(len(column_names)):
                datatypes[column_names[i]] = get_string(f"Enter datatype for {column_names[i]} : ")
            f = open(path, "a")
            w = writer(f)
            m = get_int("Enter total no of rows : ")
            for i in range(m):
                for j in range(len(column_names)):
                    temp_L = get_data_for_csv(datatypes[column_names[j]], column_names[j])
                    row_data = row_data + temp_L
                w.writerow(row_data)
                row_data.clear()

            f.close()
            break
