import matplotlib.pyplot as plt

start = [400, 0, 300]

goal = [600, 200, 200]

steps = 10

path = []

for i in range(steps + 1):

    t = i / steps

    x = start[0] + t * (goal[0] - start[0])
    y = start[1] + t * (goal[1] - start[1])
    z = start[2] + t * (goal[2] - start[2])

    point = [x, y, z]

    path.append(point)

print(path)

x_values = [point[0] for point in path]
y_values = [point[1] for point in path]
z_values = [point[2] for point in path]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(x_values, y_values, z_values, marker="o")

ax.set_xlabel("X (mm)")
ax.set_ylabel("Y (mm)")
ax.set_zlabel("Z (mm)")

ax.set_title("Linear Path Planning")

plt.show()