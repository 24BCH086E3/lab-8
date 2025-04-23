names = {"Alice", "Andrew", "Bob", "Ben", "Angela", "Bella"}
set_A = {name for name in names if name.startswith("A")}
set_B = {name for name in names if name.startswith("B")}

print("Names starting with A:", set_A)
print("Names starting with B:", set_B)
