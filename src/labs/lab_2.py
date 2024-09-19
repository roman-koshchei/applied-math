import numpy as np
import matplotlib.pyplot as plt

def problem_4_3_13():
  # Avoid t=0 to prevent division by zero in sin(t)
  t = np.linspace(0.1, 2 * np.pi, 1000)  

  x = (1 + np.cos(t))**2
  y = np.cos(t) / (np.sin(t)**2)

  plt.figure(figsize=(10, 5))

  plt.plot(
    x, y, 
    color="green", 
    linestyle=":", 
    label=r'$y = \frac{\cos(t)}{\sin^2(t)},\ x = (1 + \cos(t))^2$'
  )
  
  plt.title('Parametric Plot of $y = \\frac{\\cos(t)}{\\sin^2(t)}$, $x = (1 + \\cos(t))^2$')
  plt.xlabel('x')
  plt.ylabel('y')
  plt.ylim(-10, 10)  # Set limits for y to better visualize the plot
  plt.axhline(0, color='black',linewidth=0.5, ls='--')
  plt.axvline(0, color='black',linewidth=0.5, ls='--')
  
  plt.grid()
  plt.legend()


def problem_2():
  # Define parameters
  a = 2
  b = -2

  # Define the range for theta
  theta = np.linspace(0, 2 * np.pi, 1000)

  # Calculate the radius p using the polar equation
  p = a / (1 + b * np.cos(theta))

  # Create the polar plot
  plt.figure(figsize=(8, 8))
  ax = plt.subplot(111, projection='polar')
  ax.plot(theta, p, label=r'$p = \frac{2}{1 - 2\cos(\theta)}$')

  # Set title and legend
  ax.set_title('Polar Curve of Second Order', va='bottom')
  ax.legend(loc='upper right')

  # Show the plot

def run():
  problem_4_3_13()
  problem_2()

  plt.show()

