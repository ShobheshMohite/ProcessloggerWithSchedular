import psutil

def ProcessDisplay():
    '''
    Get list of running process sorted by Memory Usage
    '''
    listOfProcObjects = []

    # Iterate over the list
    for proc in psutil.process_iter():      #taking photos

        try:
            # Fetch process details as dict
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
            
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

if __name__ == '__main__':
   main()
