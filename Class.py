class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print self.sounds[i % len(self.sounds)],
        print ""

class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self):
        # Call the __init__ method of the parent class
        super(Bassist, self).__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super(Guitarist, self).__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print "Be with you in a moment"
        print "Twoning, sproing, splang"

class Drummer(Musician):
    def __init__(self):
        super(Drummer,self).__init__(["Bam","Bang","Class"])
    
    def count(self):
        print "1,2,3,4"
        
    def combust(self):
        print "I'm on fire"

class Band(Musician):
    def __init__(self, musicians_list = []):
        self.musicians_list = musicians_list
        
    def Add_Musician(self, musicians):
        self.musicians_list.append(musicians)
        
    def Fire_Musician(self, musicians):
        self.musicians_list.remove(musicians)
    
    def Tryout(self,musicians):
        print "1,2,3,4"
        print musicians.solo(self)

nigel = Guitarist()
nigel.solo(6)
print nigel.sounds
ourband = Band()
ourband.Add_Musician(nigel)
ourband.Tryout(nigel)