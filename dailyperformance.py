import matplotlib.pyplot as plt
days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
problems = []
print("Enter problems solved each day:")
for day in days:
    p = int(input(f"{day}: "))
    problems.append(p)
total = sum(problems)
max_problems = max(problems)
best_day = days[problems.index(max_problems)]
print("Total Problems Solved:", total)
print("Most Active Day:", best_day)
plt.figure(figsize=(14,8))
# Bar Chart
plt.subplot(2,3,1)
plt.bar(days, problems)
plt.title("Daily Problems Solved")
plt.xlabel("Day")
plt.ylabel("Problems")
# Line Chart
plt.subplot(2,3,2)
plt.plot(days, problems, marker='o')
plt.title("Weekly Coding Trend")
# Scatter Plot
plt.subplot(2,3,3)
plt.scatter(days, problems)
plt.title("Coding Activity Scatter")
# Pie Chart
plt.subplot(2,3,4)
plt.pie(problems, labels=days, autopct='%1.1f%%')
plt.title("Contribution by Day")
# Horizontal Bar Chart
plt.subplot(2,3,5)
plt.barh(days, problems)
plt.title("Horizontal Comparison")
plt.tight_layout()
plt.show()