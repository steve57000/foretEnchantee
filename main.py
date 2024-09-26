from colorama import Fore, init

# Initialisation de colorama (nécessaire pour Windows)
init(autoreset=True)

print(Fore.MAGENTA + "Bienvenue dans la Forêt Enchantée.")


##############################################
### -------- Entrer dans la forêt -------- ###
##############################################

chemin = int(input(f"{Fore.CYAN}Deux chemins s'offrent à toi. Choisis {Fore.MAGENTA}1{Fore.RESET}{Fore.CYAN} pour le sentier sombre, ou {Fore.MAGENTA}2{Fore.RESET}{Fore.CYAN} pour le sentier éclairé : "))

if chemin == 1:
    print(Fore.MAGENTA + "Tu entends un bruit étrange.")
    action = int(input(f"Que fais-tu ? {Fore.BLUE}1 : T'arrêter pour écouter. {Fore.CYAN}2 : Continuer rapidement. "))
    if action == 1:
        print(Fore.RED + "C'était un piège ! Les brigands t'ont attrapé. Fin de l'aventure.")
        exit()
    elif action == 2:
        print(Fore.GREEN + "Tu as évité le danger et tu continues ta route.")
elif chemin == 2:
    print(Fore.MAGENTA + "Un loup-garou apparaît !")
    action = int(input(f"Que fais-tu ? 1 : {Fore.BLUE}Courir pour te cacher. {Fore.CYAN}2 : Te battre avec une épée trouvée par terre. "))
    if action == 1:
        print(Fore.RED + "Le loup-garou t'a rattrapé. Fin de l'aventure.")
        exit()
    elif action == 2:
        print(Fore.GREEN + "Tu as vaincu le loup-garou et continues ta route.")


##############################################
###---------- La rivière magique --------- ###
##############################################

print(Fore.MAGENTA + "Tu arrives devant une rivière, tu as deux possibilité.")
danger = int(
    input(f"Choisis {Fore.MAGENTA}1{Fore.RESET} pour traverser à la nage, ou {Fore.MAGENTA}2{Fore.RESET} pour suivre la rivière en espérant trouver un pont plus loin "))

if danger == 1:
    print(Fore.RED + "Mauvais choix. L'eau de la rivière est empoisonnée. Fin de l'aventure.")
    exit()
elif danger == 2:
    print(Fore.GREEN + "Bravo ! Tu trouves un pont après quelques minutes de marche.")


##############################################
###---------- Le pont maudit --------- ###
##############################################

print(Fore.MAGENTA + "Je suis léger comme une plume, mais personne ne peut me tenir longtemps. Qui suis-je ? ")
enigme = int(input(f" {Fore.BLUE}1 : Le souffle, {Fore.GREEN}2 : L'eau, {Fore.CYAN}3 : L'ombre "))

if enigme == 1:
    print(Fore.GREEN + "Félicitation ! La créature te laisse passer et tu continue ta quête.")
elif enigme == 2 or 3:
    print(Fore.RED + "Mauvaise réponse. La créature te jette dans la rivière et tu échoues.")
    exit()


##############################################
###---------- Sortie de la forêt --------- ###
##############################################

print(Fore.MAGENTA + "Après avoir traversé le pont, tu aperçois enfin la sortie de la forêt. Cependant, un dernier choix crucial s'impose :")
dernier_choix = int(input(f"Pour prendre un raccourci à travers un champ de fleurs toxiques {Fore.BLUE}tape 1{Fore.RESET}. Si tu veux suivre le sentier principal, plus long mais sûr, {Fore.CYAN}tape 2 "))

if dernier_choix == 1:
    print(Fore.RED + "Le champ de fleurs toxiques t'endort à jamais. Fin de l'aventure.")
    exit()
elif dernier_choix == 2:
    print(Fore.GREEN + "Félicitations ! Tu sors enfin de la forêt enchantée, sain et sauf.")
