import os.path


def add_data_to_existing_normal_file():
    while True:
        try:
            path = input("Enter existing file name : ")
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
            f = open(path, "a")
            L = list(input("Enter data below : \n"))
            if input("Do you want to submit : ").lower() in ("yes","1",True,"YES","y","Y"):
                f.writelines(L)
            else:
                SL = list(input("Enter data below : \n"))
                f.writelines(L + SL)
            f.close()
            break


def add_data_to_new_normal_file():
    try:
        path = input("Enter new file name : ")
    except OSError as e:
        print("Disk Exhausted !!!")
    except ValueError as ve:
        print("File name contradicts conventions !!!")
    except Exception as e:
        print("Exception : ", e)
    else:
        f = open(path, "w")
        L = list(input("Enter data below : \n"))
        if input("Do you want to submit (yes/no) : ").lower() in ("yes","1",True,"YES","y","Y"):
            f.writelines(L)
        else:
            SL = list(input("Enter data below : \n"))
            f.writelines(L + SL)
        f.close()
