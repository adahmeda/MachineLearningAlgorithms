#this file deals with all the file management and data management that will be need in this machine learning project


#DATA SET DESCRIPTION
 

#ABSENSE(1) or presence(2) of heart disease
#	Class 	No. of Examples
# 	-----------------------
#	 1        150(55.56%)
#	 2        120(44.44%)


#NUMBER OF ATTRIBUTES
# STORE DATA IN CLASSES
#A1- age
#A2- sex
#A3- chest pain type
#A4 - resting blood pressure
#A5 - serum cholestoral in mg/dl
#A6 - fasting blood sugar >120mg/dl
#A7 - resting electrocardiographic results
#A8- maximum heart rate achieved
#A9- exercise induced angina
#A10- oldpeak = ST depression induced by exercise relative to rest
#A11 - the slope of the peak exercise ST segment
#A12- number of major vessels(0-3) colored by flourosopy
#A13 - thal: 3= normal; 6= fixed defect; 7 = reversable defect

#Attribute types:
#	real: A1, A4,A5,A8,A10, A12
#	ordered: A11
#	binary: A2, A6, A9
#	nominal: A7, A3, A13



#***********PART ONE: CREATING THE CLASS TO STORE THE DATA*********************




#class to store the data from the file

class HeartData():
	'class to store all data from heart.data.txt'
	dataCount=0
	def __init__(self,A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,A11,A12,A13, A14):
		self.A1=A1
		self.A2=A2
		self.A3=A3
		self.A4=A4
		self.A5=A5
		self.A6=A6
		self.A7=A7
		self.A8=A8
		self.A9=A9
		self.A10=A10
		self.A11=A11
		self.A12=A12
		self.A13=A13
		self.A14= A14
		HeartData.dataCount +=1

	
	def displayData(self):
		print("A1- age:", self.A1,"\n", "A2- sex: ", self.A2, "\n", "A3- chest pain type" , self.A3, "\n", "A4 - resting blood pressure", self.A4, "\n", "A5 - serum cholestoral in mg/dl", self.A5, "\n", "A6 - fasting blood sugar >120mg/dl", self.A6, "\n", "A7 - resting electrocardiographic results", self.A7, "\n", "A8- maximum heart rate achieved", self.A8, "\n", "A9- exercise induced angina", self.A9, "\n","A10- oldpeak = ST depression induced by exercise relative to rest", self.A10, "\n","A11 - the slope of the peak exercise ST segment", self.A11, "\n", "A12- number of major vessels(0-3) colored by flourosopy", self.A12, "\n", "A13 - thal: 3= normal; 6= fixed defect; 7 = reversable defect)", self.A13, "\n", "ABSENSE(1) or presence(2) of heart disease", self.A14, "\n")

		
	def displayCount(self):
		print("Total DataSet: ", HeartData.dataCount, "\n\n")

















#***************PART TWO: STORING THE DATA IN THE CLASS*****************************




#list that will hold a list of data of the type HeartData	
datalist=[] 
# file handle fh
fh = open('heart.data.txt')
count=0
while True:
    # read line
	line = fh.readline()
	#print(line)
	 # check if line is not empty
	if not line:
    		break

	 # the dataset is 270, this is done to prevent an out of index error
	if count==270:
		break
	# this separates the string( line) into a list using the white space.
	data=line.split() 

	#adding the data( which is an array of the characters separated by a whitespace into a list of the class HeartData called datalist)
	datalist.append(HeartData(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11], data[12], data[13]))  

	#datalist[count].displayData() 
	#datalist[count].displayCount()
	count +=1
	#print(count)
#closing the file
fh.close()








#PART THREE: SEPARATING THE TRAINING SET AND THE TESTING SET*************


#The training set will be 70% 
#The testing set will be 30%

trainingcount= 0.7* count
print(trainingcount)

trainingDataSet=[];
testingDataSet=[];


for(x) in range(int(trainingcount)):
	trainingDataSet.append(datalist[x])
	trainingDataSet[x].displayData()
	print(len(trainingDataSet))

z=0
for(y) in range(int(trainingcount), count):
	testingDataSet.append(datalist[y])
	testingDataSet[z].displayData()
	z+=1
	print(len(testingDataSet))






