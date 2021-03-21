from time import time



# www = gen('леша')
def gen_filename():
    while True:
        pattern = 'file_{}.jpeg'
        t=int(time()*1000)
        yield pattern.format(str(t))


def gen1(name):
    for i in name:
        yield i


def gen2(n):
    for i in range(n):
        yield i


g1 = gen1('Alex')
g2 = gen2(4)

tasks = [g1,g2]
while tasks:
    task = tasks.pop(0)
    try:
        i = next(task) # yield вызывается каждый раз туда где  next()
        print(i)
        tasks.append(task)
    except StopIteration:
        pass
