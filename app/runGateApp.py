# ~*~ coding: utf-8 ~*~
#!/usr/bin/env/ python

import siteTransact


def main():
   """
       Automated checkin for the BRC gate crew.
   """
   print "WELCOME STARFIGHTER\n[+] Starting Main"

    # Setup the connection object, name it, connect
   babalooey = siteTransact.Connection('babalooey',
                                        'https://www.babalooey.com/login.php')
 
   scheduleResponse=babalooey.send_get("https://www.babalooey.com/dept/1/myschedule")
   print scheduleResponse.content 

 
    # Session is left intact, now we only need to post 
#    for elem in pollDevices.poll:
#        babalooey.send_post(elem)
 

   


if __name__=="__main__":
    main()
