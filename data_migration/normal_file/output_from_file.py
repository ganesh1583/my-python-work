import os.path


def get_data_from_file():
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
        else:
            f = open(path,"r")
            data = f.read()
            print(data)
            f.close()
            break
