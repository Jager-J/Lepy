# %%
# %%
# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import os
from pathlib import Path
import time
import json
import subprocess


 

hostName = ""
serverPort = 8080
noUSB=True
global usbcounter
usbcounter=0


processList=[]
#USB STICKS STATUS AND INFORMATION
class UsbStick:
    def __init__(self,folderpath,scanstatus,filecount,foldername):
        self.folderpath=folderpath
        self.scanstatus=scanstatus
        self.filecount=filecount
        self.foldername=foldername
        self.antivirus=""
        self.startedTime=""
        self.result=""
        self.pending=False
        

    def get_data(self):
        return {"name":self.folderpath,"status":self.scanstatus,"files":self.filecount}
    def scan_usb(self):
        global usbcounter 
        # folder path
        dir_path = self.folderpath
        count = 0
        print(usbcounter)
        # Iterate directory
        for path in os.listdir(dir_path):
        # check if current path is a file
            if os.path.isfile(os.path.join(dir_path, path)):
                count += 1
        self.filecount=count
        if self.filecount>2 and self.scanstatus=="nocheck" and usbcounter < 2:
            self.scanstatus="scanning"
            print("Started scan on: '"+self.folderpath+"'")
            usbcounter = usbcounter + 1
            print(usbcounter)
            result = subprocess.run(['clamscan', '--version'], stdout=subprocess.PIPE)
            self.antivirus=(""+result.stdout.decode('utf-8'))
            print(self.antivirus)
            self.startedTime=time.time
            f = open("/home/jagja870/clamscan."+self.foldername+".log", "w")
            proc_clamscan = subprocess.Popen(["clamscan",self.folderpath, "--recursive"],
                                                stdout = f,
                                                stderr = f)
            processList.append(proc_clamscan)
      
        elif self.filecount>2 and self.scanstatus=="nocheck":
             self.pending=True 

        elif self.filecount>2 and self.scanstatus=="scanning":
                f = open("/home/jagja870/clamscan."+self.foldername+".log", "r")

                #read whole file to a string
                file_data = f.read()
                print(file_data)
                self.result=file_data

                #close file
                f.close()
                if "SCAN SUMMARY" in file_data:
                    Lines = f.readlines()
                    for line in Lines:
                        #line by line filter out infected files
                        #insert infected files in a new list
                        break
                    self.scanstatus="finish"
                    usbcounter = usbcounter - 1
        elif self.filecount<2 and self.scanstatus=="scanning":
            print("USB has been removed while scanning!")
            self.scanstatus="nocheck"
            usbcounter = usbcounter - 1
            os.remove("/home/jagja870/clamscan."+self.foldername+".log")
        elif self.filecount==0 and self.scanstatus=="finish":
            self.scanstatus="nocheck"
            self.result=""
            self.startedTime=""
            self.antivirus=""
            os.remove("/home/jagja870/clamscan."+self.foldername+".log")


usbA=UsbStick("/USB/1","nocheck",2,"A")
usbB=UsbStick("/USB/2","nocheck",2,"B")
usbC=UsbStick("/USB/3","nocheck",2,"C")
usbD=UsbStick("/USB/4","nocheck",2,"D")

folders={usbA,usbB,usbC,usbD}

class MyServer(BaseHTTPRequestHandler):
     def do_GET(self):

        getPATH=self.path[1:]
        self.send_response(200)

        
        
      
        #open text file in read mode
        if len(getPATH) > 1:
            if os.path.exists(getPATH):
                text_file = open(getPATH, "r")
                if getPATH.endswith(".css"):
                    self.send_header("Content-type", "text/css")
                    data = text_file.read()
                elif getPATH.endswith(".html"):
                    self.send_header("Content-type", "text/html")
                    data = text_file.read()
                elif getPATH.endswith(".js"):
                    self.send_header("Content-type", "text/javascript")
                    data = text_file.read()
            else:
                if getPATH.endswith("getUsbList.json"):
                      self.send_header("Content-type", "application/json")
                      usbList=[]
                      for folder in folders:
                       folder.scan_usb()
                       content = {
                        "Name":folder.foldername,
                        "FileCount":folder.filecount,
                        "status":folder.scanstatus,
                        "antivirus":folder.antivirus,
                        "startTimestamp":folder.startedTime,
                        "result":folder.result,
                        "pending":folder.pending
                        }
                       usbList.append(content)
                      data=json.dumps(usbList,indent=4, sort_keys=True, default=str)

                  
                else:
                    self.send_header("Content-type", "text/html")
                    text_file = open("404.html", "r")  
                    data = text_file.read()  
        else:    
             text_file = open("index.html", "r")
             data = text_file.read()
        #read whole file to a string


     
        self.end_headers()

        #print(data)
        self.wfile.write(bytes(data,"utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")






# %%
