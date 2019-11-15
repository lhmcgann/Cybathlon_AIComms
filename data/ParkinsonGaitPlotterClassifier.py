import matplotlib.pyplot as plt
import csv

def main():
    #initialize lists to hold data
    data = []
    limit = 2
    slopes = []
    #open data file
    with open('JuPt01_06_csv.csv','r') as csvFile:

        plots = csv.reader(csvFile, delimiter=',')
        #read data into memory
        i = 0
        stage = 1
        for column in plots:
            time = float(column[0])
            left = float(column[1])
            right = float(column[2])
            if time != 0:
                slopes.append(left/time)
                if i > 1:
                    if abs(slopes[i-1] - slopes[i-2]) > limit:
                        if stage == 5:
                            stage = 1
                        stage += 1
                data.append([time, left, right, stage])
            i += 1

    for line in data:
        print(line)
    
if __name__ == '__main__':
    main()
