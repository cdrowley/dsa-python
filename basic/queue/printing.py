from random import randrange
from que import Queue


class Task:
    def __init__(self, timestamp: int) -> None:
        self.timestamp = timestamp
        self.pages = randrange(1, 21)

    def getStamp(self) -> int:
        return self.timestamp

    def getPages(self) -> int:
        return self.pages

    def waitTime(self, currentTime: int) -> int:
        return currentTime - self.timestamp


class Printer:
    def __init__(self, pagesPerMinute: int) -> None:
        self.ppm = pagesPerMinute
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self) -> None:
        if self.currentTask != None:
            self.timeRemaining -= 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self) -> bool:
        return True if self.currentTask != None else False

    def startNext(self, newtask: Task) -> None:
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60 / self.ppm


def simulation(numSeconds, pagesPerMinute):
    def newPrintTask():
        return True if randrange(1, 181) == 180 else False

    printer = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingTimes = []

    for currentSecond in range(numSeconds):
        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)

        if (not printer.busy()) and (not printQueue.isEmpty()):
            nextTask = printQueue.dequeue()
            waitingTimes.append(nextTask.waitTime(currentSecond))
            printer.startNext(nextTask)

        printer.tick()

    averageWait = sum(waitingTimes) / len(waitingTimes)
    print(
        f"Average Wait {averageWait: .2f} seconds. {printQueue.size()} tasks remaining."
    )


for _ in range(10):
    simulation(3600, 60)