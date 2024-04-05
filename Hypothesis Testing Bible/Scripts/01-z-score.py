import pyarrow.feather as feather
import numpy as np
import pandas as pd

"""
Since variables have arbitrary ranges and units, we need to standardize them. 
For example, a hypothesis test that gave different answers if the variables were
 in Euros instead of US dollars would be of little value. Standardization avoids that.

One standardized value of interest in a hypothesis test is called a z-score. 
To calculate it, you need three numbers: the sample statistic (point estimate),
 the hypothesized statistic, and the standard error of the statistic (estimated from the bootstrap distribution)
"""

late_shipments = feather.read_feather("late_shipments.feather")
print(late_shipments)
# Calculate the proportion of late shipments
late_prop_samp = (late_shipments["late"]=="Yes").mean()
# Print the results
print(late_prop_samp)

#--------------------------BootStrap-Sampling------------------

late_shipments['late'] = late_shipments['late'].map({'Yes': 1, 'No': 0})

#-----Looping----------

late_shipments_boot_distn = []
for i in range(1000):
    late_shipments_boot_distn.append(
        np.mean(
            late_shipments.sample(frac=1,replace = True)["late"]
    )
)
    
# Hypothesize that the proportion is 6%
late_prop_hyp = 0.06
# Calculate the standard error
std_error = np.std(late_shipments_boot_distn, ddof=1)
# Find z-score of late_prop_samp
z_score = (late_prop_samp - late_prop_hyp) / std_error
# Print z_score
print(z_score)

"""
We are asking if the proportion of late shipments is BIGGER THAN 6% so it is a right tailed hyphothesis testing.
"""