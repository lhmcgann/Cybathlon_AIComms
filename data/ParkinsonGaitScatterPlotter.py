# ParkinsonGaitScatterPlotter
#
# Dimitri Charitou
# QL+_Cybathlon


import matplotlib.pyplot as plt
import csv

def main():
	#initialize lists to hold data
	leftFootForce100 = []
	leftFootForce200 = []
	leftFootForce300 = []
	leftFootForce400 = []
	leftFootForce500 = []
	leftFootForce600 = []

	rightFootForce100 = []
	rightFootForce200 = []
	rightFootForce300 = []
	rightFootForce400 = []
	rightFootForce500 = []
	rightFootForce600 = []

	#open data file
	with open('usable_input_data.csv','r') as csvFile:

		plots = csv.reader(csvFile, delimiter=',')
		#read data into 6 gait cycle lists which hold vectors (x=left foot force, y=right foot force)
		for column in plots:
			if (int(column[3]) == 100):
				leftFootForce100.append(float(column[1]))
				rightFootForce100.append(float(column[2]))

			elif (int(column[3]) == 200):
				leftFootForce200.append(float(column[1]))
				rightFootForce200.append(float(column[2]))

			elif (int(column[3]) == 300):
				leftFootForce300.append(float(column[1]))
				rightFootForce300.append(float(column[2]))

			elif (int(column[3]) == 400):
				leftFootForce400.append(float(column[1]))
				rightFootForce400.append(float(column[2]))

			if (int(column[3]) == 500):
				leftFootForce500.append(float(column[1]))
				rightFootForce500.append(float(column[2]))

			elif (int(column[3]) == 600):
				leftFootForce600.append(float(column[1]))
				rightFootForce600.append(float(column[2]))

	#set window size
	plt.figure(figsize=(15,6))

	#plot points by left and right foot forces
	plt.scatter(leftFootForce100, rightFootForce100, c='red')
	plt.scatter(leftFootForce200, rightFootForce200, c='green')

	#uncomment these lines for more data graphing
	plt.scatter(leftFootForce300, rightFootForce300, c='blue')
	plt.scatter(leftFootForce400, rightFootForce400, c='yellow')
	plt.scatter(leftFootForce500, rightFootForce500, c='orange')
	plt.scatter(leftFootForce600, rightFootForce600, c='purple')

	#set range for x axis (X axis is truncated for readability)
	plt.xlim([0.0, 50.0])

	plt.xlabel('Left Force (N)')
	plt.ylabel('Right Force (N)')
	plt.title('Gait in Parkinson\'s Disease')
	plt.legend()
	plt.show()

if __name__ == '__main__':
	main()
