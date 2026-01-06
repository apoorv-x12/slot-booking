from multiprocessing import Process

def heavy_compute():
    total = 0
    for i in range(10_000_000):
        total += i

def run_analytics():
    p = Process(target=heavy_compute)
    p.start()
