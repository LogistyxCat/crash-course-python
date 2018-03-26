#! python3

names = ['nolan','nury','sabastian','kiernan']
print("Good afternoon, " + names[0].title() + ".")
print("Good afternoon, " + names[1].title() + ".")
print("Good afternoon, " + names[2].title() + ".")
print("Good afternoon, " + names[3].title() + ".")
print()

print("Original: \n" + str(names) + "\n")
names.append('charles')
print("Appending: \n" + str(names) + "\n")
names.insert(0, 'chris')
print("Inserting: \n" + str(names) + "\n")
del names[1]
print("Deleting: \n" + str(names) + "\n")
