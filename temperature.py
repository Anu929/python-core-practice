import matplotlib.pyplot as plt
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
temperature = []
print("Enter temperature for 7 days")
for i in range(7):
    temp = int(input(f"Enter temperature for {days[i]}: "))
    temperature.append(temp)
print("Temperature Data:", temperature)
plt.plot(days, temperature, marker='o')
plt.title("Weekly Temperature Trend")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.show()