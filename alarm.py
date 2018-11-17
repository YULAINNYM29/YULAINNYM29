from sound import set_volume, play
import datetime
import os

x = input("What time do you want to get up")
           
stop = False
while stop == False:
    rn = str(datetime.datetime.now().time())
    #print(rn)
    
    if rn > x:
        snz= input("Snooze?")
        set_volume(-30)
        play()
        i = False
        while i == False:
            snz= input("Snooze for real?")
            if snz == "no":
                print("ok")
                set_volume(-5)
                play()
                break
            else:
                snz == "yes"
                i = True
                stop = True
                break
              
  
        
                    
   
        
        
                
                
