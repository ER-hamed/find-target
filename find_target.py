#! /usr/bin/python3.6

from subprocess import getstatusoutput
from socket import socket
from _thread import start_new_thread
from time import sleep
from os import system, get_terminal_size
import platform

print('\033[1;31;40m')
if platform.system() == 'Linux':
    system('clear')
if platform.system() == 'Windows':
    system('cls')

port_list = [20, 21, 22, 23, 24, 25, 26, 53, 67, 68, 80, 88, 109, 110, 111, 137, 139, 143, 161, 162, 389, 443, 520,
             546, 547, 587, 902, 993, 995, 1433, 1434, 1701, 3306, 3389, 5431, 5666, 6129, 9050]

thread_number = 0
dic = {}
found = 0


def gen_ip(wb, we, xb, xe, yb, ye, zb, ze):
    list_ip = list()
    for a1 in range(int(wb), int(we) + 1):
        for a2 in range(int(xb), int(xe) + 1):
            for a3 in range(int(yb), int(ye) + 1):
                for a4 in range(int(zb), int(ze) + 1):
                    list_ip.append(str(a1) + '.' + str(a2) + '.' + str(a3) + '.' + str(a4))
    return list_ip


def test(target):
    dic[target] = ''
    global thread_number, found
    thread_number = thread_number + 1
    state = []
    if ping:
        if str(getstatusoutput('ping -c1 -w10 ' + target)[0]) == '0':
            state.append('ICMP')
        else:
            thread_number = thread_number - 1
            return
    for port in port_list:
        try:
            s = socket(2, 1)
            s.settimeout(delay)
            s.connect((target, port))
            state.append(port)
            s.close()
            continue
        except:
            continue
    dic[target] = state
    thread_number = thread_number - 1


begin = input('Begin: ')
end = input('End: ')
if end == '':
    end = begin

begin = begin.split('.')
end = end.split('.')

delay = input('Delay[5]: ')
if delay == '':
    delay = 5
else:
    delay = int(delay)

max_thread = input('Max thread[40]: ')
if max_thread == '':
    max_thread = 40
else:
    max_thread = int(max_thread)

ping = input('Check ICMP , press y or n [y]: ')
if ping == '' or ping == 'y':
    ping = True
else:
    ping = False

try:
    from pynput.keyboard import Controller

    if input('Do you want to change port list? [y or n]: ') == 'y':
        from pynput.keyboard import Controller

        keyboard = Controller()
        keyboard.type(str(port_list)[1:-1])
        port_list = input().split(' ')
except:
    pass

if platform.system() == 'Linux':
    system('clear')
if platform.system() == 'Windows':
    system('cls')

print('\nPress ctrl + c to end the process\n')
print('Delay: ' + str(delay))
print('Max thread: ' + str(max_thread))
print('Check ICMP: ' + str(ping) + '\n')

try:
    for ip in gen_ip(begin[0], end[0], begin[1], end[1], begin[2], end[2], begin[3], end[3]):
        while True:
            if thread_number <= max_thread:
                print('Scanning: ' + ip + '    Thread: ' + str(thread_number) + '    Found: ' + str(found) +
                      '       ', end='\r')
                start_new_thread(test, (ip,))
                sleep(0.2)
                break
            else:
                sleep(0.1)
                continue
    print('                                                       ', end='\r\n')
    while True:
        if thread_number == 0:
            break
        else:
            print('Thread ' + str(thread_number) + '     ', end='\r')
            sleep(0.2)
except KeyboardInterrupt:
    pass

if platform.system() == 'Linux':
    system('clear')
if platform.system() == 'Windows':
    system('cls')

print('-' * int(get_terminal_size().columns))
open('list_ip.txt', 'w').close()
file = open('list_ip.txt', 'a')
for item in dic:
    if not str(dic[item]) == '':
        print(str(item) + ' : ' + str(dic[item]))
        file.write(str(item) + ' : ' + str(dic[item]) + '\n')
exit()
