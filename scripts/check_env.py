import importlib

packages = [
    "numpy",
    "scipy",
    "pandas",
    "matplotlib",
    "astropy",
    "torch",
    "segmentation_models_pytorch",
]

for pkg in packages:
    mod = importlib.import_module(pkg)
    print(f"{pkg}: OK")

try:
    import AegeanTools
    print("AegeanTools: OK")
except Exception as e:
    print("AegeanTools: FAILED")
    print(e)

import torch
print("Torch version:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())