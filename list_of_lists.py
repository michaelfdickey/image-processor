"""
Create a list of lists using for-loop in Python
We can use for loop to create a list of lists in Python. We used the append() method inside the loop to add the element into the list to form a list of lists. See the code and output.
"""

#example 1
lists = []
# make list of lists
for i in range(2):
# append list
lists.append([])
for j in range(5):
lists[i].append(j)
# Display result
print(lists)



#example 2
height = 2
width = 5
image_copy = []

for index in range(height):
    print(index)
    image_copy.append([])
    
    for jax in range(width):
        image_copy[index].append(jax)