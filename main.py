from jbos1 import t24_stop
from jbos2 import jboss_down
from jbos3 import dbtool_up
from jbos4 import t24_start
from jbos5 import tafjee_start
import time

def main():
    username = "ORPUSER1"
    password = "P@Ssw0rd"
    keywords = "TS, I TSM"
    t24_stop(username, password, keywords)
    
    window_name = "Administrator:  JBoss BSGDEV"
    jboss_down(window_name)
    
    script_path1 = r"C:\Temenos\BSGDEV\DBTools.bat"
    script_path2 = r"C:\Temenos\BSGDEV\jBossBSGDEV.bat"
    dbtool_up(script_path1, script_path2)
    time.sleep(5)
    t24_start(username, password, keywords)
  
    
    keywords2 = "START.TSM"
    tafjee_start(keywords2)
    

if __name__ == "__main__":
    main()