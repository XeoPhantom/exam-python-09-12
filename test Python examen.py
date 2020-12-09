from colorama import init
nit()
from colorama import Fore, Back, Style
import random
#consigne
def consigne():
	print("")
	print("Rouge = lettre présente dans le mot et à la bonne place        ")
	print("Jaune = lettre présente dans le mot, mais PAS à la bonne place ")
	print("Bleu = lettre pas présente dans le mot                         ")   
    print("mot en MAJUSCULE")
    print("Bonne chance")
	print("", end="")



def tourdujoueur(motdelavictoire)
	print(Style.RESET_ALL)
	motJoueur = input("ecriverun mot: ")
	if len(motJoueur) > 6:
		print("merci d'entrer un mot a 6 lettres")
	if len(motJoueur) < 6:
		print("merci d'entrer un mot a 6 lettres")
else

		for i in range(0,6):
			if motJoueur[i] == motdelavictoire[i])
				print(Back.RED + motJoueur[i], end="")
			else:
				print(Back.BLUE + motJoueur[i], end="")
	return motJoueur
       


       def testVictoire(motJoueur, motdelavictoire):
	if motJoueur == motdelavictoire
		victoire = True
	else:
		victoire = False
	return victoire

#main program
listeDeMot = ["ZOMBIE","STEREO","TENNIS","STRESS","RIVALE","INIQUE","JOKERS","GOUPIL","GROUPE","HASARD","FUSAIN","FRIMEE","MOJITO","NIPPON","OBSCUR","PUTAIN","FESSER","PARDON","PICOLO","OMBRES","PANZER","GOGOLS","PANTYS","AMOURS","AGAVES","BEMOLS","BOOGIE","ZOOMER","BOOMER","VIOQUE","VISSES","XIANGS","YAKUZA","DECIMA","ECHINE","NOIRES","OFFICE","ORGANE","LIBIDO","HUMIDE","JOUIEZ","ORGIES","PANTIN","SALOPE","SALIES","SCEAUX","TAXIES","VICHYS","WAKAME","PEKORA","BAMBOU","CAFTER","CANCEL","CHIMIO","EGORGE","FACIAL","EXPOSE","PNMRXY","ALBDMW","VPRDB","GAUCHE","HAUTIN","HOMMOS","HRIVNA","IMPECS","JEUDIS","KANAKS","LAXITE","MILICE","MIGNON","TOMATE","TOMMYS","TOMBER","TOMBER","TOMBAL","TOMANS","TOMIEN","DEGAGE","MEDUSE"]
motAlea = random.randint(0,9)
motdelavictoire = listeDeMot[motAlea]
tour = 1
victoire = False
consigne()


print(Style.RESET_ALL)

if victoire == False:
	print("j'ai mis 81 mots donc logiques que tu perds... et le mots était:  ", motdelavictoire)
if victoire == True:
	print("j'ai mis 81 mots donc logiques que tu gagnes...")
input()
