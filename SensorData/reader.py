# -*- coding: cp1252 -*-
import numpy as np

global nano
nano = 1000000000

def concurrance(arr1, arr2):
	print "Counting matches"
	count = 0
	spotsA1 = []
	spotsA2 = []
	equivalents = []
	for x in range(len(arr1)):
		for y in range(len(arr2)):
			if arr1[x] == arr2[y]:
				count+=1
				spotsA1.append(x*1.0)
				spotsA2.append(y*1.0)
				equivalents.append(arr1[x])
				break
	print count
	print equivalents
	print spotsA1
	print spotsA2
	countPercentages(equivalents, spotsA2, spotsA1)
	
				
def countPercentages(a,b,c):
	for x in range(len(a)):
		if b[x] != 0.0:
			print "Kohdassa %fs ero lähetetyn ja vastaanotetun datan välillä on %f prosenttia" %(a[x]/nano, (b[x]-c[x])/b[x]*100)

def main():
	data = np.loadtxt("Acc_arrivals.txt")
	data[:,1]*=nano 
	
	real = np.loadtxt("Acc_departures.txt")
	real1 = real[:,3]
	data1 = data[:,1]
	print data1
	print data1.shape
	# print data1.tolist()
	print"\n"
	print real1
	print real1.shape
	
	
	concurrance(data1.tolist(), real1.tolist())
	
if __name__ == "__main__":
	main()