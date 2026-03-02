import numpy as np
np.random.seed(101)
# Create dataset of 100 marine animals
weight = np.random.uniform(5, 500, 100)
length = np.random.uniform(30, 600, 100)
age = np.random.randint(1, 81, 100)
heart_rate = np.random.randint(20, 121, 100)
migration = np.random.uniform(0, 5000, 100)
marine_animals = np.column_stack((weight, length, age, heart_rate, migration))
print("Dataset Shape:", marine_animals.shape)
print("\nFirst 5 Records:\n", marine_animals[:5])
print("\nAverage Weight:", np.mean(weight))
print("Maximum Length:", np.max(length))
print("Minimum Age:", np.min(age))
print("Median Migration:", np.median(migration))
print("80th Percentile Heart Rate:", np.percentile(heart_rate, 80))
heavy_animals = weight > 200
print("Animals >200kg:", np.sum(heavy_animals))
old_animals = age > 50
print("Animals >50 years:", np.sum(old_animals))
high_hr = heart_rate > 100
print("High Heart Rate Count:", np.sum(high_hr))
sorted_age = np.sort(age)
print("Oldest 5 Ages:", sorted_age[-5:])

