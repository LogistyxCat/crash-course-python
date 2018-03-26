#! python3

squares = []

#for value in range(1,11):
    #squares.append(value**2)

#print(squares)

# Same as above, but one line!
squares = [value**2 for value in range(1,11)]
print(squares)
