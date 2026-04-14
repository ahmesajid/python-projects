import psutil,os,time
from colorama import Fore,Style 

#THIS IS BASIC LEVEL CODE FOR ALERT  SYSTEM
#ONLY CONSOLE 
#GUI CAN BE INTEGRATED

try:
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        #RAM
        print("********\nRAM Memory\n********")
        mem=psutil.virtual_memory()
        print(f"Total memory : {Fore.GREEN}{mem.total/(1024**3):.2f} GB{Style.RESET_ALL}")
        print(f"Available memory :{Fore.GREEN} {mem.available/(1024**3):.2f} GB{Style.RESET_ALL}")
        print(f"Used memory : {Fore.GREEN}{mem.used/(1024**3):.2f} GB{Style.RESET_ALL}")

        #CPU / FOR INTERVAL ONE SEC 
        print("********\nCPU Usage\n********")
        cpu=psutil.cpu_percent(interval=0.3)
        if(cpu>90): #returns in percents
            print(f"{Fore.RED}CPU Alert:High Usage{Style.RESET_ALL}")
        print(f"{Fore.GREEN}{cpu} % {Style.RESET_ALL}")

        #DISK USAGE
        print("********\nDISK USAGE/MEMORY\n*******")
        disk=psutil.disk_usage('/')
        print(f"Total Storage : {disk.total/(1024**3):.2f} GB")
        print(f"Used Storage : {disk.used/(1024**3):.2f} GB")
        print(f"Free Storages : {disk.free/(1024**3):.2f} GB")

        #DISK PARTITIONS
        print("********\nDISK PARTITIONS\n*******")
        partitions= psutil.disk_partitions()
        for partition in partitions:
            print(partition)

        #CORES
        print("********\nCPU CORES\n*******")
        print(psutil.cpu_count()) 
        time.sleep(2)
except KeyboardInterrupt:
    print("***Exiting Monitor / Keyboard pressed!***")

