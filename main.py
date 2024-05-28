# List of space missions
space_missions = [
    {"name": "Apollo 11", "year": 1969, "success": True},
    {"name": "Apollo 13", "year": 1970, "success": False},
    {"name": "Voyager 1", "year": 1977, "success": True},
    {"name": "Mars Pathfinder", "year": 1996, "success": True},
    {"name": "Space Shuttle Challenger", "year": 1986, "success": False},
    {"name": "Hubble Space Telescope", "year": 1990, "success": True},
    {"name": "Mars Curiosity Rover", "year": 2012, "success": True},
    {"name": "Rosetta", "year": 2004, "success": True},
    {"name": "Cassini-Huygens", "year": 1997, "success": True},
    {"name": "SpaceX Falcon 9", "year": 2015, "success": True},
]

# Initialize counters
total_missions = 0
successful_missions = 0
missions_before_2000 = []

# Process the data
for mission in space_missions:
    # Count the total number of missions
    total_missions += 1
    
    # Count the number of successful missions
    if mission["success"]:
        successful_missions += 1
        
    # Identify and list all missions launched before the year 2000
    if mission["year"] < 2000:
        missions_before_2000.append(mission["name"])

# Calculate success rate
if total_missions > 0:
    success_rate = (successful_missions / total_missions) * 100
else:
    success_rate = 0

# Print the results
print(f"Total number of missions: {total_missions}")
print(f"Number of successful missions: {successful_missions}")
print(f"Success rate: {success_rate:.2f}%")
print("Missions launched before the year 2000:")
for mission in missions_before_2000:
    print(f"- {mission}")
