
import torch

def main():
  print(get_device())

def get_device():
  return torch.device('cuda' if torch.cuda.is_available() else 'mps' if torch.backends.mps.is_available() else 'cpu')


if __name__ =='__main__':
  main()
