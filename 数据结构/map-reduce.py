from threading import Thread

class Cal(object):
    def __init__(self, start, end):
        self.result = 0
        self.start = start
        self.end = end

    def map(self):
         for i in range(self.start, self.end):
            self.result += i

    def reduce(self, other):
         self.reduce += other.result


def generate_worker(data):
    for index in range(1, len(data)):
        cal = Cal(data[index - 1], data[index])
        yield cal


def generate_threads(workers):
    for worker in workers:
        thread = Thread(target=worker.map)
        thread.start()
        yield thread


def main():
    data = [item for item in range(1, 22, 10)]

    workers = list(generate_worker(data))
    threads = list(generate_threads(workers))

    for thread in threads:
        thread.join()

    start = workers[0]
    for worker in workers[1:]:
        start.reduce(worker)

    assert start.result == 5050


if __name__ == "__main__":
    main()

