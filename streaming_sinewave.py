# importing libraries
import numpy as np
import time
import matplotlib.pyplot as plt

# creating initial data values
# of x and y
x = np.linspace(0, 10, 100)
y = np.sin(x)

# to run GUI event loop
plt.ion()

# here we are creating sub plots
fig, ax = plt.subplots()
line1, = ax.plot(x, y)

# setting title
plt.title("Streaming Sinewave", fontsize=20)

# setting x-axis label and y-axis label
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Loop
for i in range(50):
    # creating new Y values
    new_y = np.sin(x-0.5*i)
    
    # updating data values
    line1.set_xdata(x)
    line1.set_ydata(new_y)
    
    # drawing updated values
    fig.canvas.draw()
    
    # This will run the GUI event
    # loop until all UI events
    # currently waiting have been processed
    fig.canvas.flush_events()

    time.sleep(0.1)
