from scipy.stats import t
import pandas as pd
import pyarrow.feather as feather
import numpy as np
from scipy.stats import norm
import pingouin
import matplotlib.pyplot as plt

sample_dem_data = feather.read_feather("dem_votes_potus_12_16.feather")
print(sample_dem_data.head())
"""
Daring pairing! If you have repeated observations of something, then those observations form pairs.

Here, you'll look at the proportion of county-level votes for the Democratic candidate in 2012 and 2016, sample_dem_data. 
Since the counties are the same in both years, these samples are paired. 
The columns containing the samples are dem_percent_12 and dem_percent_16.
"""

# Calculate the differences from 2012 to 2016
sample_dem_data['diff'] = sample_dem_data['dem_percent_12'] - sample_dem_data['dem_percent_16']

# Find the mean of the diff column
xbar_diff = sample_dem_data['diff'].mean()

# Find the standard deviation of the diff column
s_diff = sample_dem_data['diff'].std()

# Plot a histogram of diff with 20 bins
sample_dem_data['diff'].hist(bins = 20)
plt.show()



# Calculate the differences from 2012 to 2016
sample_dem_data['diff'] = sample_dem_data['dem_percent_12'] - sample_dem_data['dem_percent_16']
# Find the mean of the diff column
xbar_diff = sample_dem_data['diff'].mean()
# Find the standard deviation of the diff column
s_diff = sample_dem_data['diff'].std()
# Plot a histogram of diff with 20 bins
sample_dem_data['diff'].hist(bins = 20)
plt.show()

#-----------------------------NON-PAIRED-T-TEST-------------------------------
# Conduct a t-test on diff
test_results = pingouin.ttest(x=sample_dem_data['diff'], 
                              y=0, 
                              alternative="two-sided")

#------------------------------PAIRED-T-TEST----------------------------------

# Conduct a paired t-test on dem_percent_12 and dem_percent_16
paired_test_results = pingouin.ttest(x=sample_dem_data['dem_percent_12'], 
                                     y=sample_dem_data['dem_percent_16'],
                                     paired=True,
                                     alternative="two-sided")
                              
# Print the paired test results
print(paired_test_results)