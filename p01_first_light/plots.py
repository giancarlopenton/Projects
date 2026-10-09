import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


def main():
  plot()


def plot():
  script_dir = Path(__file__).resolve().parent

  target_folder = script_dir / 'figures'

  target_folder.mkdir(parents=True, exist_ok=True)

  save_path = target_folder / 'trig.png'

  x_array = np.linspace((-2 * (np.pi)), (2 * (np.pi)), 1000)
  sin_array = np.sin(x_array)
  cos_array = np.cos(x_array)
  product_array = sin_array * cos_array

  fig, ax = plt.subplots(figsize=(7, 5))
  ax.plot(x_array, sin_array, label='sin', linestyle='solid')
  ax.plot(x_array, cos_array, label='cos', linestyle='dashed')
  ax.plot(x_array, product_array, label='product', linestyle='dotted')
  ax.axhline(0, color='red', linestyle='solid', linewidth=0.5)
  ax.set_title('Sin, Cos, and Product from -2π to 2π')
  ax.set_xlabel('x (Radians)')
  ax.set_ylabel('f(x)')
  ax.legend()

  fig.savefig(save_path)


if __name__ == '__main__':
  main()