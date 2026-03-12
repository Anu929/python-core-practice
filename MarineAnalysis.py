import matplotlib.pyplot as plt
import numpy as np
days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
fish = []
turtle = []
dolphin = []
depth = []
temperature = []
print("Enter Marine Observation Data for 7 Days\n")
for d in days:
    print("\nDay:", d)
    fish.append(int(input("Fish sightings: ")))
    turtle.append(int(input("Turtle sightings: ")))
    dolphin.append(int(input("Dolphin sightings: ")))
    depth.append(int(input("Water depth (m): ")))
    temperature.append(int(input("Water temperature (C): ")))
total_species = np.array(fish) + np.array(turtle) + np.array(dolphin)
fig, ax = plt.subplots(3,2)
ax[0,0].plot(days, fish, marker='o')
ax[0,0].set_title("Fish Sightings Trend")
ax[0,1].bar(days, turtle)
ax[0,1].set_title("Turtle Sightings")
ax[1,0].scatter(depth, fish)
ax[1,0].set_title("Depth vs Fish Sightings")
ax[1,1].plot(days, temperature, marker='o')
ax[1,1].set_title("Water Temperature Trend")
ax[2,0].pie(
    [sum(fish), sum(turtle), sum(dolphin)],
    labels=["Fish","Turtle","Dolphin"],
    autopct='%1.1f%%'
)
ax[2,0].set_title("Species Distribution")
ax[2,1].hist(total_species)
ax[2,1].set_title("Total Marine Sightings Frequency")
plt.tight_layout()
plt.show()
print("\nMarine Observation Summary")
print("Total Fish Sightings:", sum(fish))
print("Total Turtle Sightings:", sum(turtle))
print("Total Dolphin Sightings:", sum(dolphin))
print("Average Daily Sightings:", np.mean(total_species))