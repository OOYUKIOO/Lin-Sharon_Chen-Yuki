# Sharon Lin and Yuki Chen
# SoftDev1 PD8
# HW01 -- Divine your Destiny
# 2016-09-15

import csv, random
#dictionary
jobs = dict()
#variable to keep track of which percentile we are up to
percentile = 0.0
#read csv file
with open('occupations.csv','r') as csvfile:
    f = csv.reader(csvfile)
    for row in f:
        if row[0] != 'Job Class' and row[0] != 'Total':
            #add percentile of each job
            percentile += float(row[1])
            #make a list of percentage and percentile
            val = [float(row[1]),percentile]
            #jobs[row[0]] = float(row[1])
            jobs[row[0]] = val
#print(jobs)
def jobPicker():
    #generate random number within range (0,highest percentile)
    num = float(random.random()*percentile)
    #loop through dictionary
    for job in jobs:
        #if random number less than or equal to selected item's percentile, then choose this job
        if num <= jobs[job][1]:
            print(job)
            return

jobPicker()
