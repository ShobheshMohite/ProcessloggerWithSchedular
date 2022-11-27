import psutil
import schedule
import time

def ProcessDisplay():

    listOfProcObjects = []

    # Iterate over the list
    for proc in psutil.process_iter():
       try:
           # Fetch process details as dict
           pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
           pinfo['vms'] = proc.memory_info().vms / (1024 * 1024)        #vitrual memory size in bytes
           
           # Append dict to list
           listOfProcObjects.append(pinfo)
       except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
           pass
           
    return listOfProcObjects

def main():
    print("*** Iterate over all running process and print process ID & Name ***")

    print('*** Create a list of all running processes ***')
    
    listOfProcessNames = ProcessDisplay()
    
    for elem in listOfProcessNames:
        print(elem)
    
    schedule.every(1).seconds.do(ProcessDisplay)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
   main()
