names = set()
names.update(["Alice", "Bob", "Charlie", "David", "Eve"])
print("Original set:", names)

# Modify "David" to "Dan" (remove then add)
names.discard("David")
names.add("Dan")

# Delete "Bob" and "Eve"
names.discard("Bob")
names.discard("Eve")

print("Modified set:", names)
