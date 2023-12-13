import pandas as pd
import csv

dat = pd.read_csv('healthcare-dataset-stroke-data.csv').drop('id', axis=1).dropna()
#ganti male dan female
dat = dat.replace('Other', 0).replace('Male', 1).replace('Female', 2)
#ganti ever_married
dat = dat.replace('Yes', 1).replace('No', 0)
#ganti work
dat = dat.replace('children', 1).replace('Govt_job', 2).replace('Never_worked', 3).replace('Private', 4).replace('Self-employed', 5)
#ganti residence
dat = dat.replace('Urban', 1).replace('Rural', 2)
#ganti smoke status
dat = dat.replace('Unknown', 0).replace('formerly smoked', 1).replace('never smoked', 2).replace('smokes', 3)

dat.to_csv('data.csv')