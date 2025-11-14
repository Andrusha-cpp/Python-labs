import matplotlib.pyplot as plt

python = [
    [0,0,0,1,1,1,1,1,1,1,0,0,0],
    [0,0,0,1,0,1,1,1,1,1,0,0,0],
    [0,0,0,1,1,1,1,1,1,1,0,0,0],
    [0,0,0,0,0,0,1,1,1,1,2,2,2],
    [1,1,1,1,1,1,1,1,1,1,2,2,2],
    [1,1,1,1,1,1,1,1,1,1,2,2,2],
    [1,1,1,2,2,2,2,2,2,2,2,2,2],
    [1,1,1,2,2,2,2,2,2,2,2,2,2],
    [1,1,1,2,2,2,2,0,0,0,0,0,0],
    [0,0,0,2,2,2,2,2,2,2,0,0,0],
    [0,0,0,2,2,2,2,2,0,2,0,0,0],
    [0,0,0,2,2,2,2,2,2,2,0,0,0],
]

colors = {0:'white', 1:'#306998', 2:'#FFD43B'}

fig, ax = plt.subplots()
for y, row in enumerate(python):
    for x, val in enumerate(row):
        ax.add_patch(plt.Rectangle((x, len(python)-y-1), 1, 1, color=colors[val]))

ax.set_aspect('equal')
ax.set_xlim(0, len(python[0]))
ax.set_ylim(0, len(python))
ax.axis('off')
plt.show()