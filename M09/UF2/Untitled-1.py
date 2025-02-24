from multiprocessing import Process, Queue
def funcio(q):
    if q.empty():
        print ("Cua buida")
    while not q.empty():
        a = q.get()
        a[0] = a[0] + 1
        print (a)

if __name__ == '__main__':
    q = Queue()
    #omplo la cua amb 3 elements
    q.put([7])
    q.put([10])
    q.put([15])


    #mostro els elements de la cua
    ''' for n in range(3):
        print (q.get())
    '''
    #ara cridem un procés que anirà mirant el que hi ha a la cua, li suma un numero i ho mostra per pantalla
    
    p = Process(target=funcio, args=(q,))
    p.start()
    p.join()   
