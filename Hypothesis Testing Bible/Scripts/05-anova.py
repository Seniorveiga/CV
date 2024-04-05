from scipy.stats import t
import pandas as pd
import pyarrow.feather as feather
import numpy as np
import seaborn as sns
import pingouin
import matplotlib.pyplot as plt

late_shipments = feather.read_feather("late_shipments.feather")
print(late_shipments)

# Calculate the mean pack_price for each shipment_mode
xbar_pack_by_mode = late_shipments.groupby("shipment_mode")['pack_price'].mean()
# Calculate the standard deviation of the pack_price for each shipment_mode
s_pack_by_mode = late_shipments.groupby("shipment_mode")['pack_price'].std()
# Boxplot of shipment_mode vs. pack_price
sns.boxplot(x = "pack_price", y = "shipment_mode", data = late_shipments)
plt.show()

# Run an ANOVA for pack_price across shipment_mode
anova_results = pingouin.anova( data = late_shipments, dv = "pack_price", between = "shipment_mode")

# Print anova_results
print(anova_results)

# Modify the pairwise t-tests to use Bonferroni p-value adjustment
pairwise_results = pingouin.pairwise_tests(data=late_shipments, 
                                           dv="pack_price",
                                           between="shipment_mode",
                                           padjust="none")

# Print pairwise_results
print(pairwise_results)

# Importante: Siempre hay que usar una modificación de Padjust, por ejemplo "bonf", sino pueden colarse falsos positivos.

# Modify the pairwise t-tests to use Bonferroni p-value adjustment
pairwise_results = pingouin.pairwise_tests(data=late_shipments, 
                                           dv="pack_price",
                                           between="shipment_mode",
                                           padjust="bonf")

# Print pairwise_results
print(pairwise_results)