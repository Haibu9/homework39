import threading
import time

class Knight(threading.Thread):
    enemies = 100

    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def war(self):
        day = 0
        while self.enemies > 0:
            time.sleep(1)
            day += 1
            self.enemies -= self.power
            print(f"{self.name} сражается {day}..., осталось {self.enemies} воинов.")
        print(f"{self.name} одержал победу спустя {day} дней(дня)!")


    def run(self):
        print(f"{self.name}, на нас напали!")
        self.war()


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()

first_knight.join()

if not first_knight.is_alive() and not second_knight.is_alive():
    print('Все битвы закончились!')
