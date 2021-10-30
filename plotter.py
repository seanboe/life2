from os import pread
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

UPDATE_INTERVAL = 100
GRAPHED_POINTS  = 50

style.use('fivethirtyeight')

fig = plt.figure()
axis1 = fig.add_subplot(1, 1, 1)

def animate(i):
  graph_data = open('data_output.txt', 'r').read()
  lines = graph_data.split('\n')
  predator_line = []
  prey_line     = []
  cycles        = []

  for line in lines:
    if len(line) > 1:
      predator, prey, cycle = line.split(',')
      predator_line.append(float(predator))
      prey_line.append(float(prey))
      cycles.append(cycle)

  if len(predator_line) > GRAPHED_POINTS:
    predator_line = predator_line[-GRAPHED_POINTS:]
    prey_line = prey_line[-GRAPHED_POINTS:]
    cycles = cycles[-GRAPHED_POINTS:]

  axis1.clear()
  axis1.plot(cycles, predator_line, label="predators")
  axis1.plot(cycles, prey_line, label="prey")
  axis1.legend()

animate_graph = animation.FuncAnimation(fig, animate, interval = UPDATE_INTERVAL)
plt.show()