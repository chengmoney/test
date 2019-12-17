from time import sleep


class Clock(object):
    def __init__(self, hour, minute, second):
        self.second = second
        self.minute = minute
        self.hour = hour

    def run(self):
        self.second += 1
        if self.second == 60:
            self.second = 0
            self.minute += 1
            if self.minute == 60:
                self.minute = 0
                self.hour += 1
                if self.hour == 24:
                    self.hour = 0

    def show_time(self):
        print('{:02}:{:02}:{:02}'.format(self.hour, self.minute, self.second))


def main():
    clock = Clock(23, 59, 54)
    while True:
        clock.show_time()
        sleep(1)
        clock.run()


if __name__ == '__main__':
    main()

