import csv

def create_csv_file(file, computers=100):
    with open(file, 'w', newline='') as csvfile:
        fieldnames = ['pc_name', 'ip']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for i in range(1, computers + 1):
            pc_name = f"P{i:03}"
            ip = f"172.30.2.{i}"
            writer.writerow({'pc_name': pc_name, 'ip': ip})

file = 'pc.csv'
create_csv_file(file)
print(f"Plik {file} został utworzony.")
