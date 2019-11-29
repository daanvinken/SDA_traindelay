import csv

with open('../data/vertrektijden.csv') as source_file:
    with open('../data/vertrektijden_unquoted.csv', 'w') as dest_file:
        reader = csv.reader(source_file, delimiter=";")
        writer = csv.writer(dest_file)

        for row in reader:
            writer.writerow(list(row))

with open('../data/vertrektijden.csv') as source_file:
    with open('../data/vertragingen.csv', 'w') as dest_file:
        reader = csv.reader(source_file, delimiter=";")
        writer = csv.writer(dest_file)

        for row in reader:
            if (row[7] != '0'):
                writer.writerow(list(row))

with open('../data/vertrektijden.csv') as source_file:
    with open('../data/geenvertragingen.csv', 'w') as dest_file:
        reader = csv.reader(source_file, delimiter=";")
        writer = csv.writer(dest_file)

        for row in reader:
            if (row[7] == '0'):
                writer.writerow(list(row))
