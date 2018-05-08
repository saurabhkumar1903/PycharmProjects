import Weapon,Player,Enemy,EnemyAttack
class Driver :
    PlayerName=''
    PlayerStats=0
    spyder =0

    def __init__(self):
        print('Welcome to my world...! Enter Your Name to continue!')
        self.PlayerName=input('Enter a name')
        self.playerStats=Player.CPlayer(self.PlayerName,Weapon.CWeapon('null',0),'false')
        self.spyder = Enemy.CEnemy()
    def runAgain(self):
        playagain=input('enter y or Y to Play again!')
        if(playagain=='y'or playagain=='Y'):
            self.spyder.Health=40
            self.spyder.IsAlive=True
            Driver.chooseDoor(self)

    def chooseDoor(self):

        self.playerStats.Health = 20
        self.playerStats = Player.CPlayer(self.PlayerName, Weapon.CWeapon('Hand', 5),self.playerStats.Has_Key)
        while(self.playerStats.Health>0 ):
            chdoor=int(input('You see 2 doors !....1st Red 2nd Blue which one do you enter....?'))

            if(chdoor==2) :
                print('Welcome to Blue door! you see a weapon cache...');
                chweapon=1
                while(chweapon!=0) :
                    chweapon=int(input('Press 1 to pickup a knife '+'\nPress 2to Pickup the Sword'+'\nPress 3 to pick up the key!'+'\nPress 0 to exit Blue Door'))
                    if(chweapon==1):
                        self.playerStats=Player.CPlayer(self.PlayerName,Weapon.CWeapon('Knife',10),self.playerStats.Has_Key)
                    elif(chweapon==2):
                        self.playerStats = Player.CPlayer(self.PlayerName,Weapon.CWeapon('Sword',12),self.playerStats.Has_Key)
                    elif(chweapon==3):
                        self.playerStats=Player.CPlayer(self.PlayerName,self.playerStats.CurrentWeapon,True)
                    elif(chweapon==0):
                        print('You are Out of the Blue Door!')
                        print(self.playerStats.CurrentWeapon.WeaponName)
                        print(self.playerStats.Has_Key)
                        break

            if(chdoor==1) :
                print('Welcome to Red Door! Be Ready for your Doom...')
                if(self.spyder.IsAlive==False):
                   print('Seems lIke the Evil Spyder is dead...Voila!')
                   Driver.AfterEnemyDeath(self)
                chfight=int(input('You see a giant Spyder What do you want to Do?'+'\nPress 1 to Fight' +'\nPress 2 to Flee'))
                if(chfight==1):

                    while(self.playerStats.Health>0 and self.spyder.Health>0) :

                        print('your health:',self.playerStats.Health,'\tSpyder Health:',self.spyder.Health)

                        chattack = int(input('Press 1 to attack with hand '+'\nPress 2 to attack with your weapon'+'\nPress 3 to defend\n'))

                        t1=EnemyAttack.CEnemyAttack(self.playerStats)
                        t1.start()

                        #print('After startttttt\n')
                        self.playerStats=t1.returnPlayerHealth()

                        if(chattack==2):
                            print('current weapon',self.playerStats.CurrentWeapon.WeaponName)
                            if(self.playerStats.CurrentWeapon.WeaponName=='Hand'):
                                print('you don\'t have any weapon you can only fight with your fist\n')
                            else :
                                self.spyder.Health=self.spyder.Health-self.playerStats.CurrentWeapon.AttackPower
                            #    print('############', self.spyder.Health)
                        elif(chattack==3):
                            if(t1.is_sleeping==False):
                                t1.returnPlayerHealth().Health+=2
                        elif(chattack==1) :
                            self.spyder.Health = self.spyder.Health - 5
                           # print('############',self.spyder.Health)
                        self.playerStats=t1.returnPlayerHealth()

                    if (self.spyder.Health <= 0):
                        print('congratulations!',self.playerStats.PlayerName,'Won!')
                        self.spyder.IsAlive=False
                        Driver.AfterEnemyDeath(self)
                        exit(0)
                    if (self.playerStats.Health <= 0):
                        print('Player Died!...Game Over!\n')
                        Driver.runAgain(self);
                elif(chfight==2):
                    print('Fleeing to Safety...! You should probably go back in blue door and pick up some weapons\n')

    def AfterEnemyDeath(self):
        chdoor=2
        print('key status:',self.playerStats.Has_Key)
        while(chdoor!=1):
            chdoor = int(input('There is a door Press 1 to unlock it and Exit the World of Doom.'))
            if(chdoor==1):
                if(self.playerStats.Has_Key==True) :
                    print('Bye Bye You\'re free')
                    exit(0)
                else :
                    print('You forgot something in the Blue room Go and check Blue Room Again')
                    Driver.chooseDoor(self)
                    Driver.AfterEnemyDeath(self)
            else :
                print('Press 1 to unlock the Door and Exit the World of Doom.')




x=Driver();
x.chooseDoor()