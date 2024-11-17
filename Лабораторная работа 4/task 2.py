import csv
import json

csv_file = "input.csv"
json_file = "output.json"

def task() -> None:

    results = []
    with open(csv_file, newline="") as input_f:

        reader = csv.DictReader(input_f)

        for row in reader:
            results.append(json.dumps(row, indent=4))

    with open(json_file, "w") as output_f:
        output_f.write("[\n    ")
        output_f.write(",\n    ".join(results))
        output_f.write("\n]")

if __name__ == '__main__':

    task()

    with open(json_file) as output_f:
        for line in output_f:
            print(line, end="")
