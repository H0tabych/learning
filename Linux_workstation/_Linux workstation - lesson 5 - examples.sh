####################################################### Разбор ДЗ
# 1. Потоки ввода/вывода. Создать файл, используя команду echo. Используя команду cat, прочитать содержимое каталога etc, ошибки перенаправить в отдельный файл.

# создадим файл 
echo > file1

# прочитаем содержимое каталога /etc и перенаправим ошибки в файл errors
cat /etc/* 2>errors


# 2. Конвейер (pipeline). Использовать команду cut на вывод длинного списка каталога, чтобы отобразить только права доступа к файлам. Затем отправить в конвейере этот вывод на sort и uniq, чтобы отфильтровать все повторяющиеся строки.

# вариант решения с учетом того, что права занимают первые 10 символов в выводе команды ls -l
ls -l | cut -b -10 | sort | uniq

# вариант решения с учетом того, что права занимают первую колонку до пробела
ls -l | cut -f 1 -d ' ' | sort -u

# вариант решения утилитой awk
ls -l | awk '{print $1}' | sort | uniq


# 3. Управление процессами. Изменить конфигурационный файл службы SSH: /etc/ssh/sshd_config, отключив аутентификацию по паролю PasswordAuthentication no. Выполните рестарт службы systemctl restart sshd (service sshd restart), верните аутентификацию по паролю, выполните reload службы systemctl reload sshd (services sshd reload). В чём различие между действиями restart и reload? Создайте файл при помощи команды cat > file_name, напишите текст и завершите комбинацией ctrl+d. Какой сигнал передадим процессу?

# подключимся по SSH протоколу
ssh student@192.168.56.107

# правим конфиги службы SSH (отключим авторизацию по паролю)
sudo nano /etc/ssh/sshd_config

# рестартуем службу SSH
systemctl restart sshd

# вместо перезапуска службы sshd мы просто перезагрузим конфиги
systemctl reload sshd

	Разница между reload и restart
o	service reload - PID сохраняется (перечитываются настройки), 
o	service restart - PID меняется (stop + start)


# создадим файл командой cat
# завершим ввод без перевода каретки на новую строку клавишей Ctrl+d
cat > f1
1
2
3
4 Ctrl+d

	По нажатию ^d передается символ End Of File (EOF) для обозначения завершения ввода.
	По нажатию ^c передается сигнал завершения работы команды cat


# 4. Сигналы процессам. Запустите mc. Используя ps, найдите PID процесса, завершите процесс, передав ему сигнал 9.

# откроем новый терминал и там запустим Midnight Commander
mc

# найдем процесс mc
ps aux | grep mc

# прибьем процесс с сигналом 9 (строго, без возможности сохранить данные)
kill -s 9 30779


#################################################### Структура каталогов Linux
# посмотрим только папки (ключ -d) верхнего уровня (ключ -L 1)
tree -L 1 -d /

#################################################### inode
# посмотрим свободное место на диске (колонка «Использовано»)
df

# посмотрим свободные inodes (колонка «IИспользовано»)
df -hi


#################################################### Ссылки
# выведем содержимое папки вместе с inodes (ключик -i)
ls -li
	в первой колонке номера inode

# создадим файл
echo hi all > original_file

# создадим жесткую ссылку на него
ln original_file hardlink

# создадим мягкую ссылку на него
ln -s original_file softlink


#################################################### Права в Linux
# Команда chmod
# Предоставить другим пользователям права на запись в файл header.txt
chmod o+w header.txt

# Можно менять несколько прав для ряда категорий
chmod go-rw header.txt

# Другие варианты работы с правами
chmod u+w,g+r header.txt
chmod -rw header.txt
chmod u=rwx,g=wr,o=r header.txt

# задание прав триадами цифр
•	0: (000) No permission.
•	1: (001) Execute permission.
•	2: (010) Write permission.
•	3: (011) Write and execute permissions.
•	4: (100) Read permission.
•	5: (101) Read and execute permissions.
•	6: (110) Read and write permissions.
•	7: (111) Read, write, and execute permissions.
chmod 770 header.txt
# ключ -R для задания рекурсивного изменения прав
chmod 777 -R ~/lesson3

# Изменяем владельца файла
sudo chown user1 header.txt
 

# Sticky bit нужен для запрета удаления файлов всем, кроме владельца
chmod +t filename


# установить флаг SUID
chmod u+s filename

# снять флаг SUID
chmod u-s filename


# установить флаг SGID 
chmod g+s filename

# снять флаг SGID
chmod g-s filename


#################################################### Права в Linux
# Команда chown
# Изменяет владельцев файла или папки, а также группу владельцев

# сменим владельца файла f1
sudo chown user2 f1

# сменим группу владельцев 
sudo chown :dev_team f1

# сменим одновременно владельца и группу владельцев
sudo chown student:student –R .

