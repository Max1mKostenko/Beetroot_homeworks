# import threading
#
#
# class Counter(threading.Thread):
#     counter = 0
#     rounds = 100000
#
#     def run(self) -> None:
#         for i in range(self.rounds):
#             self.counter += 1
#             print(self.counter)
#
#
# t1, t2 = threading.Thread(target=Counter.run()), threading.Thread(target=Counter.run())
# t1.start()
# t2.start()
#
# if __name__ == "__main__":
#     pass

import threading

counter = 0
rounds = 100000


class Counter(threading.Thread):
    def run(self):
        global counter
        for i in range(rounds):
            counter += 1
            print(counter)


t1, t2 = Counter(), Counter()
t1.run()
t2.run()
