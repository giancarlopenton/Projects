
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import torch



def main():
  numpy_seed = np.random.default_rng(100)
  torch_seed = torch.manual_seed(100)
  trig_plot()
  dtype_comparison()
  precision_plot()
  memory_test()
  noise_data()

def trig_plot():

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

  fig.savefig(create_path_png('trig'))


def dtype_comparison():

  all_close32, max_diff32 = compare_sin(np.float32, torch.float32)
  print(f"float 32 | allclose: {all_close32} | max difference: {max_diff32}")
  all_close64, max_diff64 = compare_sin(np.float64, torch.float64)
  print(f"float 64 | allclose: {all_close64} | max difference: {max_diff64}")

def compare_sin(numpy_dtype, torch_dtype):
  x_array = np.linspace((-2 * (np.pi)), (2 * (np.pi)), 1000, dtype=numpy_dtype)
  x_tensor = torch.linspace((-2 * (np.pi)), (2 * (np.pi)), 1000, dtype=torch_dtype)

  x_tensor_sin = torch.sin(x_tensor)
  x_array_sin = np.sin(x_array)

  x_tensor_sin = x_tensor_sin.detach().cpu().numpy()

  return np.allclose(x_array_sin, x_tensor_sin), np.max(np.abs(x_tensor_sin - x_array_sin))


def precision_plot():

  x_array64, error = compute_error()

  fig, ax = plt.subplots(figsize=(7, 5))
  ax.scatter(x_array64, error, s=8, color='purple', label='sin(32) - sin(64)')
  ax.set_yscale('log')
  ax.axhline(np.finfo(np.float32).eps, label='float32 machine epsilon', color='red')
  ax.set_title('How far float32 sin is from float64 sin')
  ax.set_xlabel('x (Radians)')
  ax.set_ylabel('Error')
  ax.legend(loc='lower left')


  fig.savefig(create_path_png('precision'))

def compute_error():
  x_array32 = np.linspace((-2 * (np.pi)), (2 * (np.pi)), 1000, dtype=np.float32)
  x_array_sin32 = np.sin(x_array32)
  x_array64 = np.linspace((-2 * (np.pi)), (2 * (np.pi)), 1000, dtype=np.float64)
  x_array_sin64 = np.sin(x_array64)

  error = np.abs(x_array_sin32 - x_array_sin64)

  return x_array64, error

def memory_test():
  array = np.array([98, 99, 100])
  shared_memory = torch.from_numpy(array)
  independent_memory = torch.tensor(array) 
  before = array[0]
  array[0] = 500
  print(f'from_numpy | before: {before}| after changing array: {shared_memory[0]}')
  print(f'torch.tensor | before: {before} | after changing array: {independent_memory[0]}')
  


def noise_data():
  x = torch.linspace(0, 10, 200)
  tensor_1d = torch.randn(200)
  noise = tensor_1d * 1.5
  y = 2 * x + 1 + noise
  y_true = 2 * x + 1

  fig, ax = plt.subplots(figsize=(7,5))
  ax.scatter(x, y, alpha=0.5, label='data')
  ax.set_xlabel('Input')
  ax.set_ylabel('Output')
  ax.set_title('Noise Data')
  ax.plot(x, y_true, label='true line (y= 2x + 1)', color='red')
  ax.legend()

  fig.savefig(create_path_png('noise_data'))

def create_path_png(name):  
  script_dir = Path(__file__).resolve().parent

  target_folder = script_dir / 'figures'

  target_folder.mkdir(parents=True, exist_ok=True)

  save_path = target_folder / f'{name}.png'

  return save_path

if __name__ == '__main__':
  main()