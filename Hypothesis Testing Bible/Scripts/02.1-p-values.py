import pyarrow.feather as feather
import numpy as np
import pandas as pd
from scipy.stats import norm

late_shipments = feather.read_feather("late_shipments.feather")
print(late_shipments)
# Calculate the proportion of late shipments
late_prop_samp = (late_shipments["late"]=="Yes").mean()
# Print the results
print(late_prop_samp)

# Hypothesize that the proportion is 6%
late_prop_hyp = 0.06


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
    
# Calculate the standard error
std_error = np.std(late_shipments_boot_distn, ddof=1)
# Calculate the z-score of late_prop_samp
z_score = (late_prop_samp - late_prop_hyp)/std_error

#-----------------Calculating-p-value-------------------

# Calculate the p-value
p_value = 1 - norm.cdf(z_score,loc=0, scale=1)
                 
# Print the p-value
print(p_value) 