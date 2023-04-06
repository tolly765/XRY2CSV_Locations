import csv
from itertools import chain
import os

file = "PBZ2"
locationFile = open(f"./Locations/{file}.txt")
parse = True
lineList = []
uncleanList = []

# Prepare CSV
os.remove(f"./Output/{file}_out.csv")
out_csv = open(f"./Output/{file}_out.csv", "w", newline='')
writer = csv.writer(out_csv)
header = ['Longitude', 'Latitude', 'Altitude', 'GPS Time']
writer.writerow(header)


for line in locationFile:
    # print(line)
    if '---------------------------------------------------------------' in line:
        print(lineList)
        try:
            csvRow = [lineList[2], lineList[4], lineList[6], lineList[8]]
            # print(csvRow)
            writer.writerow(csvRow)
        except IndexError:
            csvRow = [lineList[2], lineList[4], lineList[6]]
            # print(csvRow)
            writer.writerow(csvRow)
        # Clear the lists for next iteration
        lineList.clear()
        uncleanList.clear()
        # break
    elif line == '\n':
        pass
    else:
        sline = line.strip()
        formLine = sline.replace('\t\t', ': ')
        formLine = formLine.split(': ')
        uncleanList.append(formLine)
        lineList = list(chain.from_iterable(uncleanList))
        # print("Appended")

out_csv.close()
