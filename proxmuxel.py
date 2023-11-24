import os

class Proxmuxel:   
    def containers_range_start(start_by: int, end_by: int):
        os.system(f"pct start {i}")
        
    def containers_range_stop(start_by: int, end_by: int):    
        for i in range(start_by, end_by+1):
            print(i)
            os.system(f"pct stop {i}")
    
    def containers_range_runnig_bash(start_by: int, end_by: int, command: str):    
        for i in range(start_by, end_by+1):
            print(i)
            os.system(f"pct exec {i} {command}")
            