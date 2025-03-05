import csv
import json

def read_all_csv(filename):
    fields = []
    rows = []
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        for row in csvreader:
            rows.append(row)
        return fields, rows

def read_all_json(filename):
    with open(filename, 'r') as json_file:
        return json.load(json_file)

def make_json(filename):
    import random
    dic = {f"Member {i}": random.randint(1, 1000) for i in range(10)}
    with open(filename,'w') as json_file:
        json.dump(dic, json_file)
    return dic

if __name__ == "__main__":
    print("This life is amazing")
    filename = 'colors.csv'
    fields, rows = read_all_csv(filename)
    print(fields)
    for row in rows:
        # print(row)
        print(row[0])

    # make_json('weapons.json')
    # print(read_all_json('weapons.json'))

    weapon = read_all_json('weapon_template.json')
    print(weapon)
    # color = rows[0][0]
    # print()
