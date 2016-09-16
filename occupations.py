import csv
import random

jobs = dict()

job_list = []

with open('occupations.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if (row[0] != 'Job Class') and (row[0] != 'Total'):
            jobs[row[0]] = float(row[1])

for job in jobs:
    for a in range(int(jobs.get(job)*10)):
        job_list.append(job)

print(random.choice(job_list))
print(random.choice(job_list))
print(random.choice(job_list))
        
