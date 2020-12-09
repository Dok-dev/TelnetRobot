#!/usr/bin/env python
# import sys
import telnetlib


tn = telnetlib.Telnet("192.168.17.31", 23) #подключаемся к узлу

tn.read_until(b"LocalHost login:") # отлавливаем приглашение, которое заканчивается "Router  >"
tn.write(b"root\n") # вводим команду (Обратить внимание на \r)

tn.read_until(b"Password:") #отлавливаем приглашение с вводом пароля
tn.write(b"xc3511\n") # вставляем пароль (Обратить внимание на \r)

tn.read_until(b"#") #отлавливаем приглашение, информирующее о входе в систему
tn.write(b"cat /mnt/mtd/Log/Log\n") # выполняем команду (вывод лога)
s=b''
s = tn.read_until(b"#") # считываем результат до определенного слова
# print(s)

if s.find(b'[ZeroBitrate]') != -1:
    tn.write(b"cat /dev/null > /mnt/mtd/Log/Log\n")  # очищаем лог
    tn.read_until(b"#")  # отлавливаем приглашение
    tn.write(b"reboot\n")  # выполняем команду перезагрузки
    tn.read_until(b"0++++++++++++++")  # отлавливаем сообщение о перезагрузке
    print('Camera rebooted')
else:
    print('Camera OK')

tn.close(); #закрываем сессию
