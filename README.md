# Introduction

Simplekit is a Python library to make programming simple.

# Quick start

## Exit current program if the user press ENTER

```python
from time import sleep
from tqdm import tqdm
import simplekit as sk

while True:
	for i in tqdm(range(100), desc='Working'):
		sleep(0.1)
	sk.exit_on_enter(timeout=10)
```

## Reload modules by name

```python
import numpy
import simplekit as sk

sk.reload_module('numpy', verbose=2)
```