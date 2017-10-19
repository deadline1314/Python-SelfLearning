import csv

with open('example.csv') as csv_file:
    readCSV = csv.reader(csv_file, delimiter=',')
    print(csv_file)

    dates = []
    colors = []
    for row in readCSV:
        color = row[3]
        date = row[0]
        dates.append(date)
        colors.append(color)

    try:
        what_color = input('What color do you wish to know the date of?')

        if what_color in colors:
            coldex = colors.index(what_color)
            the_date = dates[coldex]
            print('The date of', what_color, 'is:', the_date)
        else:
            print('Color not found, or is not a color!')
    # except Exception, e:  python2
    except Exception as e:
        print(e)

    print('continuing')
