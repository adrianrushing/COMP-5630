'''Adrian Rushing
    1/18/24
    COMP 5630
    ML
    '''

import numpy as np 
import matplotlib.pyplot as plt
from collections import Counter
import string
import cv2 


### PROBLEM 1 ###

# Opens the file to be read
# The with keyword makes it so the 
# file does not have to be explicitly closed
with open("test.txt") as text_file:
    # Makes all letters lowercase so 
    # they are all counted regardless of case
    file_contents = text_file.read().lower()

# Remove non-letter characters
file_contents = ''.join(filter(str.isalpha, file_contents))
# print(file_contents)
# Count the letters in the string and assign them to the dictionary 
letter_counts_dict = dict.fromkeys(string.ascii_lowercase, 0)
# Using the Collection framework count 
# the frequencies for all letters
letter_counts_dict.update(Counter(file_contents))

# Converts the dictionary directly to an array
letter_counts_array = np.array(list(letter_counts_dict.items()), dtype=[('letter', 'U1'), ('count', int)])

# Print out the histograms
# print(f"Dictionary: \n{letter_counts_dict}\n")
# print(f"NP: \n{letter_counts_array}\n")

# Get values for the x (letters) and y (counts) axis in lists
letters = list(letter_counts_dict.keys())
counts = list(letter_counts_dict.values())

total = sum(counts)
normalized_counts = [ count / total for count in counts]

'''
    Plotting the data for both graphs with plt.[method] 
    results in a window for each displaying.
'''

'''Add an if statement to switch between printing two windows
   and printing both plots on one'''

# Plot the normalized data
#Sets the size of the graph
plt.figure(figsize=(5,5))
# Sets the axes of the bar graph
plt.bar(letters, normalized_counts)
# Label the x axis
plt.xlabel('Letters')
# Label the y axss
plt.ylabel('Frequency')
# Title the graph
plt.title('Letter Frequencies (Normalized)')
# Display the graph
# plt.show()


# Plot the Unnormalized data

# Sets the size of the graph
plt.figure(figsize=(5,5))
# Sets the axes of the bar graph
plt.bar(letters, counts)
# Label the x axis
plt.xlabel('Letters')
# Label the y axis
plt.ylabel('Frequency')
# Title the graph
plt.title('Letter Frequencies (Unnormalized)')
# Display the graph
plt.show()

### PROBLEM 2 ###

# Reads in the image
img_input1 = cv2.imread('test.png')

#These are the max values for RGB
end_points = np.array([[255,0,0],[0,255,0],[0,0,255]])

# Iterates down the rows
for i in range(img_input1.shape[0]):
    # Iterates across the columns
    for j in range(img_input1.shape[1]):
        # Sets Pixel to a specifc point
        pixel = img_input1[i, j]
        # Calculates the distances for each pixel to each of the three points
        distances = [np.linalg.norm(pixel-point) for point in end_points]
        # Pulls the min value and stores it at [i,j]
        img_input1[i,j] = end_points[np.argmin(distances)]

# Write output image
cv2.imwrite('output1.png', img_input1)

# New image variable to maipulate
img_input2 = cv2.imread('test.png')

# Get the side lenghts of the image
x_length = img_input2.shape[0]
y_length = img_input2.shape[1]

# Calculate number of pixels needed to reach the middle 50
border_dist = int((x_length - 50) / 2)

# Start at the end of the border and iterate 50 px in both x and y'
# in range from 38-88
for i in range(border_dist- 1, x_length - border_dist):
    for j in range(border_dist - 1, y_length - border_dist):
        img_input2[i,j] = [0,0,0]

cv2.imwrite('output2.png', img_input2)\

### PROBLEM 3 ###

# Solving a system of equations with numPy
'''Problem statement:  
    You and a friend go to buy tacos. You get three soft tacos 
    and  three  burritos  and  your  total  bill  is  $11.25.  Your 
    friend's  bill  is  $10.00  for  four  soft  tacos  and  two 
    burritos. How much do soft tacos cost? How much do burritos 
    cost? 
'''
# Coefficient Array for taco orders
# Array: [Soft, burritos]
orders_array = np.array([[3, 3], [4, 2]])

# Price Array for total cost of orders
# Array: [your's, friend's]
order_price_array = np.array([11.25, 10.00])

# Solve the system
item_price_array = np.linalg.solve(orders_array, order_price_array)

#Print the items array 
print(item_price_array)

# Check if the solutions are correct 
print(np.allclose(np.dot(orders_array, item_price_array), order_price_array))