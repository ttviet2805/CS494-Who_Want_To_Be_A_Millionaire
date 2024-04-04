import MenuClass
import pygame
import sys
import client

def main():
    for arg in sys.argv[1:]:
        print("Argument:", arg)
    
    serverIP = "10.124.4.169"
    port = 2828
    if(len(sys.argv) >= 2):
        serverIP = sys.argv[1]
    if(len(sys.argv) >= 3):
        port = int(sys.argv[2])
    
    clientSocket = client.ClientSocket()
    clientSocket.connectSocket(serverIP, port)

    # Init
    pygame.init()
    infoObject = pygame.display.Info()
    screenProportion = 3 / 4

    menuGame = MenuClass.Menu((infoObject.current_w * screenProportion, infoObject.current_h * screenProportion))
    menuGame.run(clientSocket)
    clientSocket.closeConnection()

if __name__ == "__main__":
    main()