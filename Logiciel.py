class Medium:
    def __init__(self, titre, auteur, date):
        self.titre = titre  # Titre du média
        self.auteur = auteur  # Auteur du média
        self.date = date  # Date de parution du média
        self.est_preté = False  # Indique si le média est prêté ou non
        self.ami_prete = None  # Nom de l'ami à qui le média est prêté

    def marquer_comme_preté(self, ami):
        self.est_preté = True  # Marquer le média comme prêté
        self.ami_prete = ami  # Enregistrer le nom de l'ami

    def marquer_comme_rendu(self):
        self.est_preté = False  # Marquer le média comme non prêté
        self.ami_prete = None  # Effacer le nom de l'ami

    def __str__(self):
        return f"{self.titre} - {self.auteur}"  # Format d'affichage du média


class Livre(Medium):
    def __init__(self, titre, auteur, date, nb_pages, editeur):
        super().__init__(titre, auteur, date)
        self.nb_pages = nb_pages  # Nombre de pages du livre
        self.editeur = editeur  # Éditeur du livre

    def __str__(self):
        return f"Livre: {self.titre} - {self.auteur} ({self.nb_pages} pages, édité par {self.editeur})"


class CD(Medium):
    def __init__(self, titre, auteur, date, duree, nb_morceaux):
        super().__init__(titre, auteur, date)
        self.duree = duree  # Durée du CD en minutes
        self.nb_morceaux = nb_morceaux  # Nombre de morceaux sur le CD

    def __str__(self):
        return f"CD: {self.titre} - {self.auteur} ({self.duree} minutes, {self.nb_morceaux} morceaux)"


class DVD(Medium):
    def __init__(self, titre, auteur, date, duree):
        super().__init__(titre, auteur, date)
        self.duree = duree  # Durée du DVD en minutes

    def __str__(self):
        return f"DVD: {self.titre} - {self.auteur} ({self.duree} minutes)"


class ArticleMagazine(Medium):
    def __init__(self, titre, auteur, date, nom_magazine, numero_magazine, intervalle_pages):
        super().__init__(titre, auteur, date)
        self.nom_magazine = nom_magazine  # Nom du magazine
        self.numero_magazine = numero_magazine  # Numéro du magazine
        self.intervalle_pages = intervalle_pages  # Intervalle des pages de l'article

    def __str__(self):
        return f"Article de magazine: {self.titre} - {self.auteur} ({self.nom_magazine}, numéro {self.numero_magazine}, pages {self.intervalle_pages})"


class GestionMedias:
    def __init__(self):
        self.medias = []  # Liste des médias gérés

    def ajouter_media(self, media):
        self.medias.append(media)  # Ajouter un média à la liste

    # Méthode pour lister tous les médias
    def lister_medias(self):
        for media in self.medias:
            print(media)

    # Méthode pour lister les médias par un auteur spécifique
    def lister_medias_par_auteur(self, auteur):
        medias_par_auteur = []
        for media in self.medias:
            if media.auteur == auteur:
                medias_par_auteur.append(media)
        return medias_par_auteur

    # Méthode pour supprimer un média par titre et auteur
    def supprimer_media(self, titre, auteur):
        for media in self.medias:
            if media.titre == titre and media.auteur == auteur:
                self.medias.remove(media)
                break

    # Méthode pour supprimer tous les médias d'un auteur spécifique
    def supprimer_medias_par_auteur(self, auteur):
        medias_a_garder = []
        for media in self.medias:
            if media.auteur != auteur:
                medias_a_garder.append(media)
        self.medias = medias_a_garder

    # Méthode pour marquer un média comme prêté à un ami spécifique
    def noter_media_emprunte(self, titre, auteur, ami):
        for media in self.medias:
            if media.titre == titre and media.auteur == auteur:
                media.marquer_comme_preté(ami)
                break

    # Méthode pour compter le nombre de médias prêtés
    def compter_medias_pretes(self):
        count = 0
        for media in self.medias:
            if media.est_preté:
                count += 1
        return count

    # Méthode pour ajouter un média via le terminal
    def ajouter_media_terminal(self):
        type_media = input("Entrez le type de média (Livre, CD, DVD, Article de magazine) : ")
        titre = input("Entrez le titre du média : ")
        auteur = input("Entrez l'auteur du média : ")
        date = input("Entrez la date de parution du média : ")
        
        if type_media.lower() == "livre":
            nb_pages = input("Entrez le nombre de pages du livre : ")
            editeur = input("Entrez l'éditeur du livre : ")
            media = Livre(titre, auteur, date, nb_pages, editeur)
        elif type_media.lower() == "cd":
            duree = input("Entrez la durée du CD (en minutes) : ")
            nb_morceaux = input("Entrez le nombre de morceaux du CD : ")
            media = CD(titre, auteur, date, duree, nb_morceaux)
        elif type_media.lower() == "dvd":
            duree = input("Entrez la durée du DVD (en minutes) : ")
            media = DVD(titre, auteur, date, duree)
        elif type_media.lower() == "article de magazine":
            nom_magazine = input("Entrez le nom du magazine : ")
            numero_magazine = input("Entrez le numéro du magazine : ")
            intervalle_pages = input("Entrez l'intervalle des pages de l'article : ")
            media = ArticleMagazine(titre, auteur, date, nom_magazine, numero_magazine, intervalle_pages)
        else:
            print("Type de média non reconnu.")
            return
        
        self.medias.append(media)
        print(f"{type_media.capitalize()} ajouté avec succès.")

    # Méthode pour supprimer un média via le terminal
    def supprimer_media_terminal(self):
        auteur = input("Entrez l'auteur du média à supprimer : ")
        # Supprimer tous les médias de l'auteur
        confirmation = input("Voulez-vous supprimer tous les médias de cet auteur ? (oui/non) : ")
        if confirmation.lower() == "oui":
            self.supprimer_medias_par_auteur(auteur)
            print(f"Tous les médias de l'auteur '{auteur}' ont été supprimés.")
        # Supprimer le média spécifique
        else:
            titre = input("Entrez le titre du média à supprimer : ")
            self.supprimer_media(titre, auteur)
            print(f"Le média '{titre}' de l'auteur '{auteur}' a été supprimé avec succès.")
