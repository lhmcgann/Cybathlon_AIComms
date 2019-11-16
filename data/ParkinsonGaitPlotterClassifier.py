import matplotlib.pyplot as plt
import csv

def main():
    #initialize lists to hold data
    data = []
    limit = 5
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
            if time != 0: # ignore first irrelevant line
                if i > 1: # wait for two data points

                    # gets change in force for left and right foot 
                    leftDiff = left - data[i-2][1]
                    rightDiff = right - data[i-2][2]
                    slopes.append([leftDiff, rightDiff]) # append to list to compare to later

                    # booleans if the change is over the limit (True if Rising or Falling quickly)
                    MAG_COND_LEFT = abs(slopes[i-2][0]) > limit 
                    MAG_COND_RIGHT = abs(slopes[i-2][1]) > limit  
                    
                    # State Machine
                    if stage == 1: # right increasing force > left
                        if not MAG_COND_LEFT: # checks for when left foot is in air
                            stage = 2
                    elif stage == 2: # right const force
                        if MAG_COND_LEFT and MAG_COND_RIGHT: # checks if both feet are changing
                            stage = 3
                    elif stage == 3: # right decreasing force > left
                        if left > right: # checks for when left force overtakes right force
                            stage = 4
                    elif stage == 4: # right decreasing force < left
                        if not MAG_COND_RIGHT: # checks for when right foot is in air
                            stage = 5
                    elif stage == 5: # right no force
                        if MAG_COND_RIGHT and MAG_COND_LEFT: # checks for when both feet are changing
                            stage = 6
                    elif stage == 6: # right increasing force < left
                        if left < right: # checks for when right force overtakes left 
                            stage = 1
                data.append([time, left, right, stage*100]) # stage multipied by 100 for visibility on graphs
            i += 1
    
    # write to output file
    with open('output.csv','w', newline="") as result_file:
        wr = csv.writer(result_file)
        wr.writerows(data)
    
if __name__ == '__main__':
    main()
