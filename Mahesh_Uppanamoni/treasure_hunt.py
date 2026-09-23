print("TREASURE HUNT")
treasure_bag = [] 
treasure_bag.append("gold coin")
treasure_bag.append("silver coin")
treasure_bag.append("ruby")
treasure_bag.append("pearl")
print("\n1. Initial Treasure Bag:", treasure_bag)

rare_treasures = ("diamond", "magic ring") 
print("Rare Treasures:", rare_treasures)

#Add rare treasures to bag. Tuples can't be added directly, so convert to list
treasure_bag.extend(list(rare_treasures))
print("Bag after adding rare treasures:", treasure_bag)

treasure_bag.remove("silver coin") 
print("\n3. After removing 'silver coin':", treasure_bag)

ruby_index = treasure_bag.index("ruby")
treasure_bag[ruby_index] = "emerald"
print("After replacing 'ruby' with 'emerald':", treasure_bag)

gold_count= treasure_bag.count("gold coin")
print("\n4. Number of 'gold coin':", gold_count)

treasure_bag.sort() #sort A to Z
print("Sorted Bag:", treasure_bag)

treasure_bag.reverse() #reverse order
print("Reversed Bag:", treasure_bag)


if "magic ring" in treasure_bag:
    print("\n5. 'magic ring' exists in the bag!!! ")
else:
    print("'magic ring' not found ")

emerald_position = treasure_bag.index("emerald") # finds first position
print("Position of 'emerald':", emerald_position)


mid = len(treasure_bag) // 2 
my_share = treasure_bag[:mid] 
friend_share = treasure_bag[mid:] 
print("\n6. My Share:", my_share)
print("Friend's Share:", friend_share)


islands = ("island_1", "island_2", "island_3") 
print("\n7. Treasure Map:")
for island in islands:
    print(f"Searching {island} for treasures...")


print("\n8. FINAL CHALLENGE - INTERACTIVE GAME")
game_bag = ["gold coin", "silver coin", "ruby", "pearl"] + list(rare_treasures)
print("Starting Bag:", game_bag)

#Ask user to add treasure
add_item = input("Enter a treasure to ADD: ")
game_bag.append(add_item)
print("Bag after adding:", game_bag)

#Ask user to remove treasure
remove_item = input("Enter a treasure to REMOVE: ")
if remove_item in game_bag:
    game_bag.remove(remove_item)
    print("Bag after removing:", game_bag)
else:
    print(f"{remove_item} not found in bag!")

print("\nFinal Bag:", game_bag)
print(" GAME OVER ")
