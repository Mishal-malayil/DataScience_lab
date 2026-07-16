import matplotlib.pyplot as plt

# Data
products = ['Product A', 'Product B', 'Product C', 'Product D']
inventory = [45, 88, 21, 63]

# Create figure
plt.figure(figsize=(8, 5))

# Create bar chart
plt.bar(products, inventory, color='teal', edgecolor='black', width=0.6)

# Add title and labels
plt.title('Current Stock Inventory Level', fontsize=14)
plt.xlabel('Product Catalog', fontsize=12)
plt.ylabel('Units Available', fontsize=12)

# Display the chart
plt.show()