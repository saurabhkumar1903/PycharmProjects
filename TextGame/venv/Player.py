import Weapon
class CPlayer:
    PlayerName = 'abc'
    Health = 20
    # AttackPower=3
    CurrentWeapon = Weapon.CWeapon('Hand',5)
    Has_Key = False

    def __init__(self, name, currentweapon, haskey):
        self.PlayerName = name
        self.CurrentWeapon = currentweapon
        self.Has_Key = haskey
        print('Initialized players')
    def getCurrentWeapon(self):
        return self.CurrentWeapon.WeaponName

x=CPlayer('raju',Weapon.CWeapon('saw',20),'false')
x=CPlayer