import os

"""
file_path= "files/file.txt"

if os.path.exists(file_path):
    print(f"File exists {file_path}")


else:
    print(f"File doesn't exist {file_path}")
"""
import json
import csv
txt_data = "ngr"

#txt_path = "output.txt"
txt_path = "output.csv"

"""
for x in range(50):
    with open(file=txt_path, mode="a") as file:
        file.write("\n" + txt_data)
        print(f"File written to {txt_path}")

"""
list={
    "name":"karel",
    "age":30,
    "gender":"male"

}

list_2D=[["name","age","gender"],
         ["karel","bro","ngr"],
         [15,25,42],
         ["male","femail","email"]]


with open(file=txt_path, mode="w",newline="") as file:
    writer = csv.writer(file)
    for row in list_2D:
        writer.writerow(row)

    print(f"File written to {txt_path}")
