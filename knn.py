#importing dependancies


#for matrix algebra
import numpy as np

#for data manipulation
import pandas as pd

from scipy.spatial import distance

from collections import defaultdict




class knearestneighbour():
	# pass the whole training array and its corresponding solutions, the test data , its corresponding solution
	distances=[]
	


	def __init__(self):
		self.k=13
		self.trainingset = defaultdict(list)	
		self.trainingsolutions = defaultdict(list)
		
	def datasets(self,trainingset, trainingsolutions, testingdata, testingsolution):
		self.trainingset=trainingset
		print()
		self.trainingsolutions=trainingsolutions
		self.testingdata=testingdata
		self.testingsolution=testingsolution

	

	def findingEuclideanDistance(self):
		t=[]
		q=len(trainingset)
		for (x) in range(q):
			#print("X",x)
			a=self.trainingset[x]
			#print("A:",a)
			b=self.testingdata
			#print("B:", b)
			c=distance.euclidean(a,b)
			#print(c)
			t.append(c)
		#print("T", t)
		#print("T length", len(t))
			

		return t
		#print("SORTED DISTANCES:", self.distances)

	
	def kmeans(self):
		#p=[]
		p=self.findingEuclideanDistance()
		#sort the distances in ascending order
		#print (p)
		#sort and get indices of sorted array
		z=np.argsort(p)

		#x=z[2]	
		#print("Z:0", x)
		#map each k distance to its index
		
		count1=0
		count2=0
		
		for(x) in range(self.k):
			if(self.trainingsolutions[x]==1):
				count1 +=1
			if(self.trainingsolutions[x]==2):
				count2 +=1
			#print(count1, count2)
			
		if(count1>count2):
			solution=1
		else:
			solution=2
		#print(solution)
		return solution	

			
			


#set seed to be random
#np.random.seed(1345)


#load the data using pandas
heartdata=pd.read_csv("heart.csv",header=None)

#drop the column with the solution
dataset=heartdata.drop(heartdata.columns[13], axis=1)

#all solutions
solutions=heartdata[heartdata.columns[13:14]]



knn=knearestneighbour()
#print("TRAINING SET")
#print(dataset.head())

#this is the training set
trainset=dataset[0:189]
trainsolutions=solutions[0:189]

#this is the training set solutions

#these are the solutions set
testset= dataset[189:269]
testsolutions=solutions[189:269]
#print(testingsolutions)



#CONVERTING DATAFRAME TO ARRAY

trainingset =trainset.values
trainingsolutions=trainsolutions.values

testingset=testset.values
testingsolutions=testsolutions.values
b=testingsolutions[0]
print(b)
r=len(testingset)
accuratenum=0
for(x) in range(r):
	a=testingset[x]
	b=testingsolutions[x]
	#print("X:", b)
	knn.datasets(trainingset, trainingsolutions,a,b)
	solution=knn.kmeans()
	print("TRAINING SET: ", x)
	print("teacher:",b)
	print("student:",solution )
	if(b==solution):
		accuratenum += 1


accuracy=accuratenum/r*100
print("ACCURACCY PERCENTAGE", accuracy)




