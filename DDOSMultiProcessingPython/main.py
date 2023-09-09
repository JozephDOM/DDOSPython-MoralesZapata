#main

import logging
import time
import multiprocessing
import requests

###################################################

page: str = 'http://127.0.0.1:8090/autenticarUsuario?usuario=User&clave=Admin'

###################################################

def multiProcesing_func(app, i):
    try:
        data = requests.get(page, verify=False)
        print('i {200} status {0}, time {1}'.format(data.status_code, data.elapsed.total_seconds() , i))
    
    except Exception as e:
        print(e)
        
        
    
def demon(page, i):
    name = multiprocessing.current_process().name
    print(name, 'Starting')
    multiProcesing_func(page, i)
    print(name, 'Exiting')
    

###################################################

if __name__ == '__main__' :
    startTime = time.time()
    process = []
    while True:
        i = 10
        p = multiprocessing.Process(target=demon, args=(page, i))
        process.append(p)
        p.start()    
        p.join()
            
    
    