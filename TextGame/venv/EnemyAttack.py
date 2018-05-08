import threading,random,time
class CEnemyAttack(threading.Thread) :
    def __init__(self,player):
        threading.Thread.__init__(self)
        self.player=player
        self.awake = False

    def run(self):
        while(self.player.Health>0):
           # print("Starting")
            self.player.Health=self.player.Health-random.randint(1,10)
            time.sleep(1000)
            self.awake = True
    def returnPlayerHealth(self):
        return self.player

    def is_sleeping(self):
        return not self.awake() and self.isAlive()  # You need to know also if you already started the thread

