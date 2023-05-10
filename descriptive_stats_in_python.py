#for operations
import numpy as np
import pandas as pd

#for plotting
import matplotlib.pyplot as plt

#for reading the file
education_districtwise = pd.read_csv('education_districtwise.csv')

#for taking an initial look at the dataframe
education_districtwise.head(10)

#for getting the descriptive statistics for the Overall Literacy column
education_districtwise['OVERALL_LI'].describe()

#for getting the descriptive statistics for the Stat Name Column, ie, it works on 
#categorical values
education_districtwise['STATNAME'].describe()

#for calculating the Range of the Overall Literacy Rate Column
range_overall_li = education_districtwise['OVERALL_LI'].max() - education_districtwise['OVERALL_LI'].min()
range_overall_li


