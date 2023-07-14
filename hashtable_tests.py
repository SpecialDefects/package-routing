from hashtable import HashTable


h = HashTable(20)


h.insert(12, "Hello")

# key 12 exists, return true
test_one = h.search(12) == "Hello"

# key 11 does not exist, return true
test_two = h.search(11) is None

# key 43 does not exist, return true
test_three = h.search(43) is None

# update key 12 to "Bye"
h.insert(12, "Bye")

# key 12 has been updated to "Bye", return True
test_four = h.search(12) == "Bye"

# delete key 12
h.delete(12)

# key 12 has been deleted, return true
test_five = h.search(12) is None

print(test_one)
print(test_two)
print(test_three)
print(test_four)
print(test_five)


