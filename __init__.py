import signal
import sys

def _handler(signum, frame):
	raise RuntimeError

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