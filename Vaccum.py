import sys
class room:
    def _int_ (self):
        self.dirty = False
    def suck(self):
        self.dirty = False

A = room()
B = room()
A.dirty = input("Is room A dirty? Enter True/False: ").lower()=="true"
B.dirty = input("Is room B dirty? Enter True/False: ").lower()=="true"
vaccumpos= input("Is vaccum cleaner present in room A or B :")
if  A.dirty and  B.dirty and vaccumpos == "A":
    A.suck()
    print("cleaning room A")
    print("vaccum cleaner moving to room B")
    vaccumpos = "B"
    B.suck()
    print("cleaning room B")
    print("All rooms cleaned")
    sys.exit()

if  A.dirty and  B.dirty and vaccumpos == "B":
    B.suck()
    print("cleaning room B")
    print("vaccum cleaner moving to room A")
    vaccumpos = "A"
    A.suck()
    print("cleaning room A")
    print("All rooms cleaned")
    sys.exit()


if not A.dirty and not B.dirty and vaccumpos == "B" :
        print("Both rooms are already clean")
        sys.exit()
if not A.dirty and not B.dirty and vaccumpos == "A":
        print("Both rooms are already clean")
        sys.exit()
        
if  A.dirty and not B.dirty and vaccumpos == "A" :
    A.suck()
    print("cleaning room A")
    print("All rooms cleaned")
    sys.exit()

if  A.dirty and not B.dirty and vaccumpos == "B" :
    vaccumpos = "A"
    A.suck()
    print("cleaning room A")
    print("All rooms cleaned")
    sys.exit()
    
if  not A.dirty and  B.dirty and vaccumpos == "B" :
    B.suck()
    print("cleaning room B")
    print("All rooms cleaned")
    sys.exit()

if  not A.dirty and  B.dirty and vaccumpos == "A" :
    vaccumpos = "B"
    B.suck()
    print("cleaning room B")
    print("All rooms cleaned")
    sys.exit()
    
    
