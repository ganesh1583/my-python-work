def get_int(msg):
    while True:
        try:
            n = int(input(msg))
            return n
        except ValueError as ve:
            print("Invalid Input !!!")


def get_float(msg):
    while True:
        try:
            n = float(input(msg))
        except ValueError as ve:
            print("Invalid Input !!!")
        else:
            return n


def get_string(msg):
    while True:
        n = input(msg)
        if n.isalnum():
            return n
        else:
            print("Invalid Input !!!")


def get_bool(msg):
    while True:
        try:
            user_input = input(msg).strip().lower()
            if user_input in ('yes', 'y', 'true', 't', '1'):
                return True
            elif user_input in ('no', 'n', 'false', 'f', '0'):
                return False
            else:
                raise ValueError("Please enter 'yes' or 'no'.")
        except ValueError as e:
            print(e)


def create_file(msg):
    try:
        fname = input(msg)
        f = open(fname,"r")
    except FileExistsError:
        print("File already exists.")
    except PermissionError as pe:
        print("Permission denied !!!")
    except FileNotFoundError as fe:
        print("File directory not found !!!")
    except OSError as e:
        print("Disk Exhausted !!!")
    except ValueError as ve:
        print("File name contradicts conventions !!!")
    else:
        f.close()
        return fname


def get_data_for_csv(datatype,column_name):
    temp_list = list()
    if datatype == "int":
        temp_list.append(get_int(f"Enter {column_name} : "))
    elif datatype == 'str':
        temp_list.append(get_string(f"Enter {column_name} : "))
    elif datatype == 'float':
        temp_list.append(get_float(f"Enter {column_name} : "))
    elif datatype == 'bool':
        temp_list.append(get_bool(f"Enter {column_name} : "))
    return temp_list
