import matplotlib.pyplot as plt
import csv

def main():
    #initialize lists to hold data
    time = []
    leftFootForce = []
    rightFootForce = []
    stage = []

    #open data file
    with open('output.csv','r') as csvFile:

        plots = csv.reader(csvFile, delimiter=',')
        #read data into memory
        for column in plots:
            time.append(float(column[0]))
            leftFootForce.append(float(column[1]))
            rightFootForce.append(float(column[2]))
            stage.append(float(column[3]))

    #set window size
    plt.figure(figsize=(15,6))
    #plot left foot force by x
    plt.plot(time, leftFootForce, color='blue', label='Left Foot')
    #plot right foot force by y
    plt.plot(time, rightFootForce, color='red', label='Right Foot')
    #plot stage 
    plt.plot(time, stage,color='green', label='Stage')
    #set range for x axis (X axis is truncated for readability)
    plt.xlim([0.0, 30.0])
    
    plt.xlabel('Time (seconds)')
    plt.ylabel('Force (N)')
    plt.title('Gait in Parkinson\'s Disease')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()
