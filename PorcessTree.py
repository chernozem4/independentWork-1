import psutil
#написана функция для построения дерева процессов в терминале. Изначальная ошибка заключалась в out = '', которая была написана в get_processes_tree,
#в функции proc- есть объект psutil, булево значение проверяет истинно ли тот факт, что процесс истинный последний дочерний, парентаут- просто чтобы красиво выводить
#
def get_process_tree(proc, bolean=True, parentout=''):
    try:
        ppid = proc.ppid()
#если написать proc.ppid то нам выдаст текст
# csrss.exe (PID: 920, PPID: <bound method Process.ppid of psutil.Process(pid=920, name='csrss.exe', status='running', started='09:51:56')>)
#├─ wininit.exe (PID: 1064, PPID: <bound method Process.ppid of psutil.Process(pid=1064, name='wininit.exe', status='running', started='09:51:58')>)
#так быть не должно, поэому пишем ppid = proc.ppid, так как это индентификатор родительского процесса, без него нам просто не выдаст его, а просто выдаст текст, который был сверху
        print(f"{parentout}{'└─ ' if bolean else '├─ '}{proc.name()} (PID: {proc.pid}, PPID: {ppid})")
        child = proc.children()
        #ошибка заключалась в child, 1. count - 1 сбрасывал ошибку до нуля, из-за чего был конфликт в коде
        #написал цикл, потому что это легкий способ пройтись по всему списку процессов, а фор вместо вайла хорош тем, что можно задать определенное значение от куда и до куда он должен пройти
        #enumerate - это встроенная функция в Python, которая позволяет легко перебирать элементы списка вместе с их индексами.
        #last_child- последний дочерний процесс, из цикла отнимаем 1, проверяем, является ли он последним
        for i, child1 in enumerate(child):

            last_child = (child1 == child[-1])
            #для того чтобы понятней формировать древо необходим vetka, так как если процесс окажется последним, то его просто выдвинет через 2 пробела, если нет, то просто добавится палочка.
            vetka = parentout + ('         ' if bolean else '│ ')
            #ошибка в child1, по ошибке написал child, из-за чего он брал только 1 процесс, а не все
            get_process_tree(child1, last_child, vetka)
    #NoSuchProcess написан здесь, чтобы все работало "по-человечески". Если процесс завершился, то нам просто выдаст ошибку и дерево дальше не пойдет
    #
    except (psutil.NoSuchProcess):
        pass
#функция собирает данные из функции get_processes_tree и собирает их в вид, чтобы мы могли посмотреть на нее
def main_process():
    # Собираем все процессы в словарь, часть процесса psutil.process_iter метод внутри в psutil, который и собирает всю информацию, а вот чтобы он собрал нужен цикл for, который перебирает процессы внутри итера и создается словарь
    all_processes = {process.pid: process for process in psutil.process_iter()}
    # перебираем все процессы и создаем список из данных корневых процессов предыдущей строки. Однако, если процесс уже сам является корневым, то просто добавляем его в список, если нет, оставляем в словаре
    main_processes_spisok = [process1 for process1 in all_processes.values()if process1.ppid() not in all_processes]
    # перебираем все корневые процессы из main_process_spisok,
    for i, korn_process in enumerate(main_processes_spisok):
        # также как и last_child, с помощью булеана перебираем список и проверяем, является процесс последним для завершения списка.
        last_main_process = (korn_process == main_processes_spisok[-1])
        #вызываем функцию get_process_tree, передавая их функции
        get_process_tree(korn_process, last_main_process)
#вызов функции main_process

if __name__ == '__main__':
    main_process()
