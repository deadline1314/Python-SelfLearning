import csv

with open('example.csv') as csv_file:
    readCSV = csv.reader(csv_file, delimiter=',')
    print(csv_file)

    dates = []
    colors = []
    for row in readCSV:
        print(row)
        print(row[0])
        print(row[0], row[1])
        color = row[3]
        date = row[0]

        dates.append(date)
        colors.append(color)

    what_color = input('What color do you wish to know the date of?')
    coldex = colors.index(what_color)

    the_date = dates[coldex]

    print('The date of', what_color, 'is:', the_date)
