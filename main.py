import sys
from proxmuxel import Proxmuxel

match sys.argv[1]:
    case "start":
        start_by = int(sys.argv[2])
        end_by = int(sys.argv[3])
        Proxmuxel.containers_range_start(start_by, end_by)
        
    case "stop":
        start_by = int(sys.argv[2])
        end_by = int(sys.argv[3])
        Proxmuxel.containers_range_stop(start_by, end_by)    

    case "bash":
        command = sys.argv[2]
        start_by = int(sys.argv[3])
        end_by = int(sys.argv[4])
        Proxmuxel.containers_range_runnig_bash(start_by, end_by, command)    
        
    case _:
        raise "Такой команды нет"    
        
print("Success")
