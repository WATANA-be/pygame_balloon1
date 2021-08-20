class Character:
    def __init__(self,name):
        self.name = name
    def show_profile(self):
        prifile = '名前{0}種族:Character'.format(self.name) 

class Monster(Character):#(Character)はCharacterクラスを継承するという意味！(継承)
    pass

chara_a = Character('キャラA')
print(chara_a.name)

monster_a = Monster('モンスターA')
#print(monster_a.name)
monster_a.show_profile
