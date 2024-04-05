from scipy.stats import t
import pandas as pd
import pyarrow.feather as feather
import numpy as np
from scipy.stats import norm

late_shipments = feather.read_feather("late_shipments.feather")
print(late_shipments)

"""
H0 = The mean weight of shipments that weren't late is the same as the mean weight of shipments that were late.
HA = The mean weight of shipments that weren't late is LESS THAN the mean weight of shipments that were late.
"""
#----T-Tests-----
#Notice that we use groupby as we use a subdivision of the DataFrame.

# Sample means
xbar_yes = late_shipments[late_shipments["late"]=="Yes"].weight_kilograms.mean()
xbar_no = late_shipments[late_shipments["late"]=="No"].weight_kilograms.mean()

# Sample standard deviations
s_yes = late_shipments[late_shipments["late"]=="Yes"].weight_kilograms.std()
s_no = late_shipments[late_shipments["late"]=="No"].weight_kilograms.std()

# Number of elements of each group
n_yes = len(late_shipments[late_shipments["late"] == "Yes"])
n_no = len(late_shipments[late_shipments["late"] == "No"])

# Calculate the numerator of the test statistic
numerator = xbar_yes - xbar_no
# Calculate the denominator of the test statistic
denominator = np.sqrt(s_yes**2/n_yes + s_no**2/n_no)
# Calculate the test statistic
t_stat = numerator/denominator
# Print the test statistic
print(t_stat)

# Calculate the numerator of the test statistic
numerator = xbar_yes - xbar_no
# Calculate the denominator of the test statistic
denominator = np.sqrt(s_yes**2/n_yes + s_no**2/n_no)
# Calculate the test statistic
t_stat = numerator/denominator
# Print the test statistic
print(t_stat)

# Calculate the degrees of freedom
degrees_of_freedom = n_yes + n_no - 2

# Calculate the p-value from the test stat
p_value = t.cdf(t_stat,df= degrees_of_freedom)

# Print the p_value
print(p_value)
