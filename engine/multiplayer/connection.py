import threading
import socket
import engine.train
import time

HEADER = 2
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "00"
SERVER = "192.168.1.45"
ADDR = (SERVER, PORT)

class connection():
    def __init__(self,trains,camera):
        self.trains=trains
        self.cPos=(0,0)
        self.camera=camera
        #Starting the connection
        print("[INFO] Starting the connection to server ", SERVER, ":", str(PORT))
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(ADDR)
        #Starting 2 threads, 1st for Data reciving and the other for the data sending like coords
        reciveData=threading.Thread(target=self.recive)
        reciveData.start()
        sendData=threading.Thread(target=self.sendCords)
        sendData.start()


    def updatePos(self,cPos):
        self.cPos=cPos
    
    def recive(self):
        print("[INFO] Reciving data...")
        while True:
            #First this method identify the type of data that server are sending
            data_id=self.client.recv(HEADER).decode(FORMAT)
            if data_id:
                #Player data like coords, username...
                if data_id=="01":
                    playerID=self.client.recv(2).decode(FORMAT)
                    if playerID in self.trains:
                        xpos=self.client.recv(6).decode(FORMAT)
                        ypos=self.client.recv(6).decode(FORMAT)
                        self.trains[playerID].updateCords(int(xpos))
                    #If the player not exists we add them to the user dict
                    else:
                        self.trains[playerID]=engine.train.TrainObject("Train",["objects","complete_train.png"],-500,100)
                        xpos=self.client.recv(6).decode(FORMAT)
                        ypos=self.client.recv(6).decode(FORMAT)
                        self.trains[playerID].updateCords(int(xpos))
    def sendCords(self):
        while True:
            #Sending data id
            send_length = str("01").encode(FORMAT)
            self.client.send(send_length)
            #Sending data
            xpos = "0"*(6-len(str(self.camera.getCords()[0])))+str(self.camera.getCords()[0])
            xpos= xpos.encode(FORMAT)
            self.client.send(xpos)
            ypos = str("654321").encode(FORMAT)
            self.client.send(ypos)
            time.sleep(0.01)