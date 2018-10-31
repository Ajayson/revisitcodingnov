elements={}
wholearray=[]
pair=0
continueloop= 'yes'
#while loop to read in value till user enter <Done>
while (continueloop=='yes'):
		elementnumber =input('Enter <Done> to finish the array. Enter your number/str --> \n') 
		if (elementnumber == 'Done'):
			continueloop='No'
		else:
			wholearray.append(elementnumber)	#taking backup of the elements user entered
			try:
				elements[elementnumber] = elements[elementnumber]+1
				pair=pair+1
				del elements[elementnumber]
			except KeyError as e:
				elements[elementnumber]=1
print ('number of pairs = ',pair)
print (wholearray)