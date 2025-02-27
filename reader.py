import csv

def read_all(filename):
    fields = []
    rows = []
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        for row in csvreader:
            rows.append(row)
        return fields, rows

if __name__ == "__main__":
    print("This life is amazing")
    filename = 'colors.csv'
    fields, rows = read_all(filename)
    print(fields)
    for row in rows:
        # print(row)
        print(row[0])