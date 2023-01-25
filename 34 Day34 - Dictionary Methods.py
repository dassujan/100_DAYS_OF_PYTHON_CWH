ep1 = {122: 45, 123: 89, 567: 69, 670: 69}
ep2 = {222: 67, 566: 90}

# ep1.update(ep2)   # The update() method updates the value of the key provided to it if the item already exists in the dictionary, else it creates a new key-value pair.

# ep1.clear()   # The clear() method removes all the items from the list.

# ep1.pop(122)  # The pop() method removes the key-value pair whose key is passed as a parameter.

ep1.popitem()     # The popitem() method removes the last key-value pair from the dictionary.

del ep1[122]
# del ep1  # If key is not provided, then the del keyword will delete the dictionary entirely.

print(ep1) 