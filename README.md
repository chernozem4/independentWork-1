Данный скрипт на python(psutil) написан с целью выполнения задания по самостоятельной работе 1 по теме "создания скрипта для вывода дерева процессов"
Запуск скрипта: 1) нажать на треугольник Run и запустить в Pycharm Professinal
                2) войти в Powershell от имени администратора, зайти в папку, где находится скрипт и запустить его команой python PorcessTree.py
Описание: Скрипт выводит процессы в виде дерева с отступами, с показанными именами процессов, PID, PPID. Рекурсивный обход процессов от PPID, обработка и ионорирование завершенных процессов
Требования: Python3.13
            pip install psutil- установить данную библиотеку для импортов

Пожелания: Здоровья, сил, терпения. Они вам понадабятся, как и мне, ибо за эти 3 дня я понял, что работать в ИБ морока и волокита, сравнимая разве что с программирование драйверов для ОС. Еще и не поможет никто, информацию приходится собирать по крупинкам из презентаций и документации
Пример вывода:
├─ csrss.exe (PID: 920, PPID: 908)
├─ wininit.exe (PID: 1064, PPID: 908)
│ ├─ services.exe (PID: 1136, PPID: 1064)
│ │ ├─ svchost.exe (PID: 1292, PPID: 1136)
│ │ │ ├─ WmiPrvSE.exe (PID: 4596, PPID: 1292)
│ │ │ ├─ unsecapp.exe (PID: 7384, PPID: 1292)
│ │ │ ├─ StartMenuExperienceHost.exe (PID: 9880, PPID: 1292)
│ │ │ ├─ SearchHost.exe (PID: 9812, PPID: 1292)
│ │ │ ├─ RuntimeBroker.exe (PID: 10480, PPID: 1292)
│ │ │ ├─ RuntimeBroker.exe (PID: 10564, PPID: 1292)
│ │ │ │ └─ powershell.exe (PID: 15952, PPID: 10564)
│ │ │ │          └─ conhost.exe (PID: 18364, PPID: 15952)
│ │ │ ├─ Widgets.exe (PID: 10708, PPID: 1292)
│ │ │ │ └─ msedgewebview2.exe (PID: 2268, PPID: 10708)
│ │ │ │          ├─ msedgewebview2.exe (PID: 2760, PPID: 2268)
│ │ │ │          ├─ msedgewebview2.exe (PID: 17332, PPID: 2268)
│ │ │ │          ├─ msedgewebview2.exe (PID: 17060, PPID: 2268)
│ │ │ │          ├─ msedgewebview2.exe (PID: 5332, PPID: 2268)
│ │ │ │          ├─ msedgewebview2.exe (PID: 6016, PPID: 2268)
│ │ │ │          └─ msedgewebview2.exe (PID: 7212, PPID: 2268)
│ │ │ ├─ WidgetService.exe (PID: 10936, PPID: 1292)
│ │ │ ├─ dllhost.exe (PID: 12080, PPID: 1292)
│ │ │ ├─ PhoneExperienceHost.exe (PID: 12544, PPID: 1292)
│ │ │ ├─ TextInputHost.exe (PID: 13092, PPID: 1292)
│ │ │ ├─ IGCC.exe (PID: 14580, PPID: 1292)
│ │ │ ├─ RuntimeBroker.exe (PID: 17172, PPID: 1292)
│ │ │ ├─ RuntimeBroker.exe (PID: 16628, PPID: 1292)
│ │ │ ├─ ShellExperienceHost.exe (PID: 6248, PPID: 1292)
│ │ │ ├─ RuntimeBroker.exe (PID: 5428, PPID: 1292)
│ │ │ ├─ ApplicationFrameHost.exe (PID: 7132, PPID: 1292)
│ │ │ ├─ SppExtComObj.Exe (PID: 1252, PPID: 1292)
│ │ │ ├─ dllhost.exe (PID: 7268, PPID: 1292)
│ │ │ ├─ SDXHelper.exe (PID: 14700, PPID: 1292)
│ │ │ ├─ FileCoAuth.exe (PID: 3252, PPID: 1292)
│ │ │ ├─ dllhost.exe (PID: 3588, PPID: 1292)
│ │ │ ├─ dllhost.exe (PID: 11200, PPID: 1292)
│ │ │ ├─ dllhost.exe (PID: 7632, PPID: 1292)