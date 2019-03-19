class Recherche:

    # init
    def __init__(self, nomFichier):
        self.etat = 0
        self.tmp = ""
        self.fichier = open(nomFichier, "r")
        self.current_line = 0
        self.run()


    # premier état
    def etat_0(self, char):
        if char == "S":
            self.tmp = self.tmp + char
            self.etat = 1
        else:
            self.tmp = ""
            self.etat = 0

    # deuxième état
    def etat_1(self, char):
        if char >= "a" and char <= "z":
            self.tmp = self.tmp + char
            self.etat = 2
        else:
            self.etat_0(char)

    # troisième état
    def etat_2(self, char):
        if char >= "a" and char <= "z":
            self.tmp = self.tmp + char
            # le caractère égale o
            if char == "o":
                self.etat = 3
            else:
                # le caractère n'est pas o mais appartient à a-z
                self.etat = 2
        else:
            self.etat_0(char)

    # quatrième état
    def etat_3(self, char):
        if char >= "a" and char <= "z":
            self.tmp = self.tmp + char
            if char == "n":
                self.etat_4()
            else:
                self.etat = 3
        else:
            self.etat_0(char)

    # état final affichage du mot
    def etat_4(self):
        print("{} se trouve à la ligne : {}".format(self.tmp, self.current_line))

        self.tmp = ""
        self.etat = 0


    def run(self):
        for line in self.fichier:
            self.current_line = self.current_line + 1
            for char in line:
                if self.etat == 0:
                    self.etat_0(char)
                elif self.etat == 1:
                    self.etat_1(char)
                elif self.etat == 2:
                    self.etat_2(char)
                elif self.etat == 3:
                    self.etat_3(char)
                elif self.etat == 4:
                    self.etat_4(char)
                else: print("No match found")