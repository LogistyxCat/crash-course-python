#! python3

brother1 = {
    'first_name': 'kiernan',
    'last_name': 'scott',
    'age': 18,
    'city': 'lacey'
}

for key,value in (brother1.items()):
    print("\nKey: " + key)
    print("Value: " + str(value).title())
