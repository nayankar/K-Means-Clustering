import sys
import string
import re
import json
import itertools
import collections
import glob
import os
import itertools
from decimal import *
import math

charset = []
linelist = []
seplinelist = []
iseplinelist = []
ilinelist =[]
icharset = []
euclid=[]
eucliddic={}
newcharset=[]

dataFileName = str(sys.argv[1])
k = int(sys.argv[2])
iterate = int(sys.argv[3])
initialPoints = str(sys.argv[4])



afinnfile = open(sys.argv[1])
for line in afinnfile:

	line = line.strip()
	if line.rstrip():
		linelist = line.split(",")
		#print linelist
		for key in linelist:
			if key.translate(None, string.punctuation).isalpha():
				seplinelist.append(key)
			else:
				seplinelist.append(float(key))
				
		charset.append(seplinelist)
		seplinelist =[]

ifinnfile = open(sys.argv[4])
for line in ifinnfile:

	line = line.strip()
	if line.rstrip():
		ilinelist = line.split(",")
		#print linelist
		for key in ilinelist:
			if key.translate(None, string.punctuation).isalpha():
				iseplinelist.append(key)
			else:
				iseplinelist.append(float(key))

		icharset.append(iseplinelist)
		iseplinelist =[]		

outloop=0
while(outloop <= iterate):
	outloop+=1
	euclid=[]
	eucliddic={}
	for key in icharset:
		eucliddic[key[4]]=[]

	#print"------"
	#print eucliddic
	
	#print icharset
	for i in charset:
		for j in icharset:
			#print i,j
			dist =  math.sqrt((i[0] - j[0])**2 + (i[1] - j[1])**2 + (i[2] - j[2])**2 + (i[3] - j[3])**2)
			euclid.append(dist)
		#print euclid
		#print euclid.index(min(euclid))
		#print icharset[euclid.index(min(euclid))][4]
		eucliddic[icharset[euclid.index(min(euclid))][4]].append(i)
		#print"-------------"
		euclid =[]	
	
	icharset=[]
	for clust in eucliddic:
		#print"cluster",clust
		sum1=0
		sum2=0
		sum3=0
		sum4=0
		count=0
		maxcountdic ={}
		for key in eucliddic[clust]:
			#print key
			count+=1
			sum1+=key[0]
			sum2+=key[1]
			sum3+=key[2]
			sum4+=key[3]
			if key[4] in maxcountdic:
				maxcountdic[key[4]] += 1
			else:
				maxcountdic[key[4]] = 1
		maxi = 0
		for value in maxcountdic:
			if maxcountdic[value] > maxi:
				maxi = maxcountdic[value]
				label = value	

		icharset.append([sum1/count,sum2/count,sum3/count,sum4/count,label])	

	if outloop == iterate:
		countinner=0
		for clust in sorted(eucliddic):
			print"Cluster",clust
			for key in eucliddic[clust]:
				print key
				if key[4]!= clust:
					countinner +=1
			print" "
		print "Number of points assigned to wrong cluster:"
		print countinner
				

		#print icharset		
	#print"-------"
	
