


#importing dependancies


#for matrix algebra
import numpy as np

#for data manipulation
import pandas as pd



#WEIGHTS/ NODE CLASS
class NeuralNetwork():

	def __init__(self):
		self.inputSize=2
		self.outputSize= 1
		self.hiddenSize= 2
		self.learningrate=0.9
		#WEIGHT INITIALIZATION
		self.W1=np.random.randn(self.hiddenSize, self.inputSize)
		self.W2=np.random.randn(self.outputSize, self.hiddenSize)


	def foward(self, arrayDataset):
		#input of hidden layer
		self.z=np.dot(arrayDataset, self.W1)



		#output of hidden layer
		self.z2= self.sigmoid(self.z)


		#print("Z2::",self.z2)
		#input of output layer
		self.z3=np.dot(self.W2, self.z2.T)


		#output of output layer
		output= self.sigmoid(self.z3)


		#print("Z3::",self.z3)
		#print("OUTPUT foward::", output)
		return output



	def sigmoid(self,s):
		res =  1/(1 + (np.exp(-(s))))
		#print("res sig", res)
		return res

	def sigmoidPrime(self, s):
		#reverse of sigmoid
		res= s*(1-s)
		return res

	def backward(self, datasetArray, teacherSolutions, output):
		print("TEACHER:", teacherSolutions)
		print("STUDENT:", output)
		W=np.subtract(teacherSolutions, output)
		#print("W:",W)
		d=(teacherSolutions- output)* self.sigmoidPrime(output)
		#print("d:", d)

		e= np.dot(d,self.W2)

		#print("e:",e)
		
		
		
		dstar=e*output*(1-output)
		x1=np.dot(dstar, e)
		
			
		changeW1=self.learningrate*(x1)
		changeW2=self.learningrate *d*self.z2
		


		#print("NEW WEIGHTS CHANGE 1::", changeW1)
		#print("NEW WEIGHTS CHANGE 2::", changeW2)
		self.W1 =changeW1 + self.W1
		self.W2 =changeW2 + self.W2

		#print("NEW WEIGHTS 1::", self.W1)
		#print("NEW WEIGHTS 2::", self.W2)

	def train(self, datasetArray, teacherSolutions):
		output= self.foward(datasetArray)
		self.backward(datasetArray, teacherSolutions, output)








trainingsetArray= [[0, 0],[0,1],[1,0],[1,1]]
predicted_Results =[[0],[1],[1],[1]]

print("TRAINING DATA SET:")
print(trainingsetArray)
nn=NeuralNetwork()
output=[]
for (x) in range(6000):
	

	#print("/n/n")
	print("ITERATION:", x)
	#print("/n/n")
	#print("ACTUALTEACHER RESULTS")
	for(y) in range(4):
		print(predicted_Results[y])
		nn.foward(trainingsetArray[y])
		print("NEURAL NETWORK RESULTS FOR DATA  ", y)
		#print(output[y])
		#error= np.mean(np.square(teacherValuesArray[x]- predicted_Results[x]))
		#print("ERROR:", error)
		nn.train(trainingsetArray[y], predicted_Results[y])	
		











