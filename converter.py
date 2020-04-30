import csv
import sys

if len(sys.argv) != 2:
    print('Please provide the csv file in the command line.')
    exit()

with open(sys.argv[1]) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    day_label_tmp = ''
    day_total_tmp = 0

    for row in csv_reader:
        if line_count == 0:
            line_count += 1
            continue

        if day_label_tmp == '' or day_label_tmp == row[0]:
            day_label_tmp = row[0]
        else:
            print('%s - %s' % (day_label_tmp, day_total_tmp))
            day_label_tmp = row[0]
            day_total_tmp = 0

        time_splitted = row[6].split(':')
        day_total_tmp += round(float(time_splitted[0]) + (float(time_splitted[1]) / 60), 2)

        line_count += 1
    
    print('%s - %s' % (day_label_tmp, day_total_tmp))