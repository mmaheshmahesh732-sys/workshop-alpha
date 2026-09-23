print("PYTHON KINGDOM MANAGEMENT")
kingdom = {
    "king": "Arthur",
    "castle": "Camelot",
    "gold": 500,
    "army": ["knight", "archer", "catapult"]
}
print("\n1. Initial Kingdom:", kingdom)


print("\n2. Name of King:", kingdom["king"])
print("Army List:", kingdom["army"])
print("Queen:", kingdom.get("queen")) # returns None safely


kingdom["gold"] += 250 # Increase gold by 250
kingdom["queen"] = "Guinevere" # Add new key
kingdom["castle"] = "New Camelot" # Change castle name
kingdom["dragon"] = True # Add dragon
print("\n3. After Updates:", kingdom)


kingdom["army"].remove("catapult") 
gold_taken = kingdom.pop("gold")
print("\n4. Gold taken:", gold_taken)
del kingdom["queen"] # Delete queen key
print("After Deleting:", kingdom)


print("\n5. Does 'gold' exist?", "gold" in kingdom)
print("All Keys:", kingdom.keys())
print("All Values:", kingdom.values())
print("All Items:", kingdom.items())


kingdom["villages"] = {
    "v1": {"population": 120, "crops": ["wheat", "barley"]},
    "v2": {"population": 80, "crops": ["rice"]},
    "v3": {"population": 200, "crops": ["wheat", "corn"]}
}
print("\n6. Population of v2:", kingdom["villages"]["v2"]["population"])
kingdom["villages"]["v1"]["crops"].append("sugarcane") # Add crop
kingdom["villages"]["v3"]["population"] += 50 # Increase population
print("After Village Updates:", kingdom["villages"])


print("\n7. Loop through Kingdom:")
for key, value in kingdom.items():
    print(f"{key} : {value}")

print("\nLoop through Villages:")
for v_name, v_data in kingdom["villages"].items():
    print(f"Village {v_name} has {v_data['population']} people and grows {v_data['crops']}")


army_stats = {
    "knight": 50,
    "archer": 30,
    "dragon": 300
}
army_stats["archer"] += 10 # Increase strength
print("\n8. Army Stats:", army_stats)
strongest = max(army_stats, key=army_stats.get) # Find strongest
print("Strongest Unit:", strongest)
del army_stats["knight"] # Remove knight
print("After removing knight:", army_stats)


kingdom["gold"] = kingdom.get("gold", 0) + 200 
kingdom["villages"]["v1"]["population"] -= 20 
kingdom["army"].remove("archer")
army_stats["dragon"] -= 50
kingdom["alliance"] = "Northern Empire" 
print("\n9. After Kingdom Events:", kingdom)


print("\n10. FINAL INTERACTIVE CHALLENGE")

soldier = input("Enter new soldier name: ")
strength = int(input("Enter soldier strength: "))
army_stats[soldier] = strength
print("Updated Army Stats:", army_stats)

v_name = input("Enter new village name e.g. v4: ")
pop = int(input("Enter population: "))
crops = input("Enter crops separated by comma: ").split(",")
kingdom["villages"][v_name] = {"population": pop, "crops": crops}
print("Updated Villages:", kingdom["villages"])


remove_v = input("Enter village to remove e.g. v2: ")
del kingdom["villages"][remove_v]
print("Final Kingdom:", kingdom)

print("KINGDOM MANAGEMENT COMPLETE")
