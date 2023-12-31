from datetime import datetime
import os


def get_time():
    now = datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_time


choice = input("Write a new diary [w]\nAppend an existing diary [a]\nRead previous diaries [r]\n").lower()

if choice == "w":
    name = input("Name of diary: ")
    f = open(f"Diary/{name}.txt", choice)
    lines = get_time() + "\n"
    lines += input("Enter content: ")
    f.write(lines)
    f.close()
else:
    current_directory = os.getcwd()
    folder_name = "Diary"
    directory_path = os.path.join(current_directory, folder_name)
    file_names = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
    print("List of diaries:")
    for file_name in file_names:
        print(file_name[:-4])
    name = input("Choose a diary: ")
    if f"{name}.txt" not in file_names:
        print("Invalid file name")
    elif choice == "a":
        f = open(f"Diary/{name}.txt", choice)
        lines = "\n" + get_time() + "\n"
        lines += input("Enter content: ")
        f.write(lines)
        f.close()
    else:
        f = open(f"Diary/{name}.txt", choice)
        print(f.read())
        f.close()