import matplotlib.pyplot as plt
<<<<<<< HEAD

# Data
products = ['Product A', 'Product B', 'Product C', 'Product D']
inventory = [45, 88, 21, 63]

# Create figure
plt.figure(figsize=(8, 5))

# Create bar chart
plt.bar(products, inventory, color='teal', edgecolor='black', width=0.6)

# Add title and labels
=======
products = ['Product A', 'Product B', 'Product C', 'Product D']
inventory = [45, 88, 21, 63]

plt.figure(figsize=(8, 5))

plt.bar(products, inventory, color='teal', edgecolor='black', width=0.6)

>>>>>>> 24c6e87 (Created)
plt.title('Current Stock Inventory Level', fontsize=14)
plt.xlabel('Product Catalog', fontsize=12)
plt.ylabel('Units Available', fontsize=12)

<<<<<<< HEAD
# Display the chart
plt.show()
=======
plt.show()
>>>>>>> 24c6e87 (Created)
