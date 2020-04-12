#!env/bin/python


from time import sleep
import locale
from consoledesigner.ConsoleDesingner import ConsoleDesingner, Colors

cd = ConsoleDesingner()
c = Colors



def escalonador(processes: list):
    """
        Verifica a prioridade de execucao dentrao da lista
        Reorganiza a lista conforme a prioridade
        Executa conforme priorizacao
    """
   
    cd.clear()
    cd.goto_xy(0, 0, c.GREEN + c.ITALIC, 'Lista dos processos')
    cd.goto_xy(2, 0, c.DARK_GRAY, '---------------------------')
    exec = [0,0,0,0,0,0,0,0] 
    t = 1
    for i, p in enumerate(processes):
        cd.goto_xy(3, t+2, c.YELLOW, p.__name__[-2:])
        t = t + 3
        # print(p.__name__[-2:])
        exec[int(p.__name__[-2:])-1] = p
        
    cd.goto_xy(4, 0, c.DARK_GRAY, '---------------------------')
    cd.goto_xy(5, 0, c.GREEN + c.ITALIC, 'Lista de execução conforme prioridade')
    cd.goto_xy(6, 0, c.DARK_GRAY, '---------------------------')
    t = 1
    for i, p in enumerate(exec):
        cd.goto_xy(7, t+2, c.YELLOW, p.__name__[-2:])
        t = t + 3

    cd.goto_xy(8, 0, c.DARK_GRAY, '---------------------------')
    
    # process_08()
    for _ in range(8):
        exec[7]()
        cd.goto_xy(2, 52, c.RED, '                           ')
        exec = exec[-1:] + exec[:-1] 
        t = 1
        for i, p in enumerate(exec):
            cd.goto_xy(7, t+2, c.YELLOW, p.__name__[-2:])
            t = t + 3
    
    exec = exec[-1:] + exec[:-1]
    t = 1
    for i, p in enumerate(exec):
        cd.goto_xy(7, t+2, c.YELLOW, p.__name__[-2:])
        t = t + 3 
    cd.goto_xy(9, 0, c.DARK_GRAY, 'Fim')


def process_01():
    a = 1
    b = 0 

    cd.goto_xy(1, 50, c.DARK_GRAY, '--Process 01---------------')
    cd.goto_xy(3, 50, c.DARK_GRAY, '---------------------------')
    for _ in range(1, 10):
        a, b = b, a + b
        cd.goto_xy(2, 52, c.RED, str(a))
        # print(a)
        sleep(0.20)

    

def process_02():
    a = 1
    b = 0 

    cd.goto_xy(1, 50, c.DARK_GRAY, '--Process 02---------------')
    cd.goto_xy(3, 50, c.DARK_GRAY, '---------------------------')
    for _ in range(1, 20):
        a, b = b, a + b
        cd.goto_xy(2, 52, c.RED, str(a))
        sleep(0.20)


def process_03():
    a = 1
    b = 0 

    cd.goto_xy(1, 50, c.DARK_GRAY, '--Process 03---------------')
    cd.goto_xy(3, 50, c.DARK_GRAY, '---------------------------')
    for _ in range(1, 30):
        a, b = b, a + b
        cd.goto_xy(2, 52, c.RED, str(a))
        sleep(0.20)


def process_04():
    a = 1
    b = 0 

    cd.goto_xy(1, 50, c.DARK_GRAY, '--Process 04---------------')
    cd.goto_xy(3, 50, c.DARK_GRAY, '---------------------------')
    for _ in range(1, 40):
        a, b = b, a + b
        cd.goto_xy(2, 52, c.RED, str(a))
        sleep(0.10)


def process_05():
    a = 1
    b = 0 

    cd.goto_xy(1, 50, c.DARK_GRAY, '--Process 05---------------')
    cd.goto_xy(3, 50, c.DARK_GRAY, '---------------------------')
    for _ in range(1, 50):
        a, b = b, a + b
        cd.goto_xy(2, 52, c.RED, str(a))
        sleep(0.10)


def process_06():
    a = 1
    b = 0 

    cd.goto_xy(1, 50, c.DARK_GRAY, '--Process 06---------------')
    cd.goto_xy(3, 50, c.DARK_GRAY, '---------------------------')
    for _ in range(1, 60):
        a, b = b, a + b
        cd.goto_xy(2, 52, c.RED, str(a))
        sleep(0.10)


def process_07():
    a = 1
    b = 0 

    cd.goto_xy(1, 50, c.DARK_GRAY, '--Process 07---------------')
    cd.goto_xy(3, 50, c.DARK_GRAY, '---------------------------')
    for _ in range(1, 70):
        a, b = b, a + b
        cd.goto_xy(2, 52, c.RED, str(a))
        sleep(0.10)


def process_08():
    a = 1
    b = 0 

    cd.goto_xy(1, 50, c.DARK_GRAY, '--Process 08---------------')
    cd.goto_xy(3, 50, c.DARK_GRAY, '---------------------------')
    for _ in range(1, 80):
        a, b = b, a + b
        cd.goto_xy(2, 52, c.RED, str(a))
        sleep(0.10)


process = []

process.append(process_03)
process.append(process_02)
process.append(process_01)
process.append(process_04)
process.append(process_08)
process.append(process_06)
process.append(process_07)
process.append(process_05)

escalonador(process)