from .function import _handler
import importlib
import signal
import sys

def exit_on_enter(timeout=5):
	signal.signal(signal.SIGALRM, _handler)
	print(f'Press ENTER in {timeout} seconds to exit')
	enter = None
	signal.alarm(timeout)
	try:
		enter = input()
	except RuntimeError:
		pass
	if enter is not None:
		sys.exit(0)
	signal.alarm(0)

def reload_module(name, verbose=0):
	v_list = []
	for k, v in sys.modules.items():
		if k.startswith(name):
			v_list.append(v)
	if verbose == 1:
		count_module = len(v_list)
		unit = 's' if count_module > 1 else ''
		print(f'reload {count_module} module{unit}')
	for i, v in enumerate(v_list):
		if verbose == 2:
			v_path = '; '.join(v.__path__)
			print(f'[{i + 1}]: reload {v.__name__} from {v_path}')
		importlib.reload(v)