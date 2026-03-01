import matplotlib.pyplot as plt

students = ["A", "B", "C", "D", "E", "F"]
marks = [50, 60, 70, 80, 90, 100]  # BOTH STUDENTS AND MARKS ARE SAME IN COUNT
# Line Chart
plt.plot(students, marks)
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Line Chart Visualization")
plt.show()
