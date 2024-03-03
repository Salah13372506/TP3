from Logiciel import *


if __name__ == "__main__":
    gestion_medias = GestionMedias()
    while True:
        choix = input("Que voulez-vous faire ? (ajouter / lister / supprimer) : ")
        if choix.lower() == "ajouter":
            gestion_medias.ajouter_media_terminal()
        elif choix.lower() == "lister":
            gestion_medias.lister_medias()
        elif choix.lower() == "supprimer":
            gestion_medias.supprimer_media_terminal()
        elif choix.lower() == "quitter":
            break
        else:
            print("Choix non reconnu. Veuillez réessayer.")