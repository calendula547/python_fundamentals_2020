file_path = input().split("\\")
for name in file_path:
    if "." in name:
        file_full_name = name.split(".")
        print(f"File name: {file_full_name[0]}")
        print(f"File extension: {file_full_name[1]}")
