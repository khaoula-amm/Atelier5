#partie1
#exercice1
class Vecteur2D:

  def __init__(self, a=0, b=0):
   self.x = a # initialisation de x et y, attributs d'instance
   self.y = b

v1 = Vecteur2D()
print(" un constructeur sans parametre ")
print(v1.x, v1.y)

v2 = Vecteur2D(2,6)
print(" une instance parametrique ")
print(v2.x, v2.y)

#exercice2
class Vecteur2D:

  #Constructeur avec parametres par defaut.
   def __init__(self, a=0, b=0):
    self.x = a 
    self.y = b
    #Addition vectorielle.
   def __add__(self, autre):
     return Vecteur2D(self.x+autre.x, self.y+autre.y)
     #Affichage d'un Vecteur2D.
   def __str__(self):
      return "Vecteur({:g}, {:g})".format(self.x, self.y)

v1, v2 = Vecteur2D(1, 0), Vecteur2D(2, 4)
print("le vecteur1 est:")
print(v1)
print("le vecteur1 est:")
print(v2)
print("l'addition du vecteur1 et 2 est:")
print(v1 + v2)

#exercice3
class Rectangle:
    #un constructeur par defaut
   def __init__(self, longueur=8, largeur=4):
     self.lon = longueur
     self.lar = largeur
     self.nom = "rectangle"
     #la surface d'un rectangle.
   def surface(self):
      return self.lon*self.lar
      #Affichage des caracteristiques d'un rectangle.
   def __str__(self):
       return ("\nLe {} a du longeur {} et du largeur  {} sa surface est: {}"
             .format(self.nom, self.lon, self.lar, self.surface()))

#classe des carres (herite de Rectangle)
class Carre(Rectangle):
    #Constructeur par defaut
    def __init__(self, a=10):
     Rectangle.__init__(self, a, a)
     self.nom = "carre" 

if __name__ == '__main__':
  r = Rectangle(10,2)
  print(r)
  c = Carre()
  print(c)
  #exercice4
class Point:
#"""classe des points du plan."""
   def __init__(self, a=0.0, b=0.0):
#"Initialisation avec valeurs par defaut"
    self.px = float(a)
    self.py = float(b)
class Segment:
#classe composite utilisant la classe Point
   def __init__(self, x1, y1, x2, y2):
    self.orig = Point(x1, y1)
    self.extrem = Point(x2, y2)
#Representation d'un objet segment
   def __str__(self):
    return ("Segment : [({:g}, {:g}), ({:g}, {:g})]"
      .format(self.orig.px, self.orig.py, self.extrem.px, self.extrem.py))
if __name__ == '__main__':
  s = Segment(1, 2, 3, 4)
  print(s)
#partie2
class Etudiant:
      def __init__(self, nom, prenom , age, CNE, moyenne):
               self.n = nom
               self.p = prenom
               self.a = age
               self.c = CNE
               self.m = moyenne
     # creating list
listEtud = []
# appending instances to list
E1 = Etudiant('chemicha','ob',20,'P123',18)
E2 = Etudiant('Natacha','kh',21,'P234',19)
E3 = Etudiant('sahraoui','Md',19,'P245',13)
listEtud.append(E1)
listEtud.append(E2)
listEtud.append(E3)
#la liste avant tri
for Etud in listEtud:
  print( Etud.n, Etud.p, Etud.a, Etud.c, Etud.m)
#la liste trier par age
print("**la liste trier par age**\n")
listEtud.sort(key=lambda x: x.a)
for Etud in listEtud:
     print( "Etudiant( ",Etud.n ,Etud.p,Etud.a,Etud.c,Etud.m,")" )
#la liste trier par moyenne
print("**la liste trier par moyenne**\n")
listEtud.sort(key=lambda x: x.m)
for Etud in listEtud:
     print( "Etudiant( ",Etud.n ,Etud.p,Etud.a,Etud.c,Etud.m,")" )
#partie3
class Module:

    __nom = 0
    __volume_horaire = 0
    __semestre = ""
    ListMatiere = []
    def _init_(self, nom="", volume_horaire=0, semestre=""):
        self.__nom = nom
        self.__volume_horaire = volume_horaire
        self.__semestre = semestre

    def display(self):
        print(self._nom,  self.volume_horaire, self._semestre)
class Matiere:

    __nom = 0
    __pourcentage = 0
    module = Module()
    ListeAnnesAcademique = []
    def _init_(self, nom="", pourcentage=0):
        self.__nom = nom
        self.__pourcentage = pourcentage

    def display(self):
        print(self._nom, self._pourcentage)

class Utilisateur:

    _nom = ""
    _email = ""
    _mot_de_passe = ""
    _genre = ""
    _age = 0

    def _init_(self, nom="", email="", mot_de_passe="", genre="", age=0):
        self._nom = nom
        self._email = email
        self._mot_de_passe = mot_de_passe
        self._genre = genre
        self._age = age

    def display(self):
        print(self._nom, self._email, self._mot_de_passe,  self._genre,  self._age)


class Professeur(Utilisateur):

    __ppr = 0
    __grade = ""
    module = Module()
    ListeMatieres = []
    ListeAnnesAcademique = []

    def _init_(self, nom="", email="", mot_de_passe="", genre="", age=0, ppr=0, grade=""):
        super()._init_(self, nom, email, mot_de_passe, genre, age)
        self.__ppr = ppr
        self.__grade = grade

    def display(self):
        print(self._ppr, self._grade)

class Annee_Academique:

    __anne = ""
    Listetudiant = []
    Listematiesre = []
    Listeprofesseur = []

    def _init_(self, anne=""):
        self.__anne = anne

    def display(self):
        print(self.__anne)


class Etudiant(Utilisateur):

    __code_massar = ""
    ListAnneAcademique = []

    def _init_(self, nom="", email="", mot_de_passe="", genre="", age=0, code_massar=""):
        super()._init_(nom, email, mot_de_passe, genre, age)
        self.__code_massar = code_massar

    def display(self):
        print(self.__code_massar)