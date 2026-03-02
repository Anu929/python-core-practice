import numpy as np
# Create 2D array
marks = np.array([
    [80, 75, 90],
    [60, 70, 65],
    [85, 95, 88]
])
print("Marks Matrix:\n", marks)
print("\nShape:", marks.shape)
print("\nTotal Marks:", np.sum(marks))
print("\nStudent-wise Total:", np.sum(marks, axis=1))
print("\nSubject-wise Total:", np.sum(marks, axis=0))
print("\nAverage Marks:", np.mean(marks))
print("Maximum Mark:", np.max(marks))
print("Minimum Mark:", np.min(marks))
new_marks = marks + 5
print("\nAfter Adding 5 Marks:\n", new_marks)
increased_marks = marks * 1.10
print("\nAfter 10% Increase:\n", increased_marks)
print("\nTranspose:\n", marks.T)
result = np.dot(marks, marks.T)
print("\nMatrix Multiplication:\n", result)