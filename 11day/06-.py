import os
pid = os.fork()
if pid == 0:
	print("子进程%d"%os.getpid())
else:
	print("父进程%d"%os.getpid())
