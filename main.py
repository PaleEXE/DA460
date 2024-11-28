#%%
# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
#%%
# Defining data for the dataframe
data = {
    'Basket': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P'],
    'Apples': [10, 20, 30, 56, 40, 40, 67, 47, 40, 4, 49, 52, 5, 56, 35, 45],
    'Bananas': [15, 6, 3, 45, 67, 44, 45, 11, 14, 18, 13, 12, 1, 34, 12, 12]
}

# Creating the dataframe
df = pd.DataFrame(data)

df
#%%
# Calculate the sums
sum_apples = df['Apples'].sum()
sum_bananas = df['Bananas'].sum()

# Create a bar chart
plt.bar(['Apples', 'Bananas'], [sum_apples, sum_bananas], color=['red', 'blue'])

# Set a title
plt.title('Comparison of total Apples and Bananas')

# Show the plot
plt.show()
