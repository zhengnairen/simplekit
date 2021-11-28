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

def generate_version_number(prefix='v'):
	timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
	suffix = random.randint(1, 99)
	version_number = f'{prefix}{timestamp}{suffix:02d}'
	return version_number

def reload_module(name, verbose=0):
	v_list = []
	for k, v in sys.modules.items():
		if k.startswith(name):
			v_list.append(v)
	if verbose > 0:
		count_module = len(v_list)
		unit = 's' if count_module > 1 else ''
		print(f'reload {count_module} module{unit}')
	count_fail = 0
	module_list_fail = []
	for i, v in enumerate(v_list):
		if verbose == 2:
			try:
				v_path = ' from ' + '; '.join(v.__path__)
			except:
				v_path = ''
			print(f'[{i + 1}]: reload {v.__name__}{v_path}')
		try:
			importlib.reload(v)
		except:
			count_fail += 1
			if verbose == 2:
				module_list_fail.append(f'{v.__name__}{v_path}')
	if count_fail:
		if verbose > 0:
			unit = 's' if count_fail > 1 else ''
			print(f'{count_fail} module{unit} failed to reload')
		if verbose == 2:
			for i, v in enumerate(module_list_fail):
				print(f'[{i + 1}]: {v}')