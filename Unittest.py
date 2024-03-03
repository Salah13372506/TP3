import unittest
from Logiciel import *

class TestMediums(unittest.TestCase):
    def test_livre(self):
        livre = Livre("Titre Livre", "Auteur Livre", "2024", 200, "Éditeur Livre")
        self.assertEqual(str(livre), "Livre: Titre Livre - Auteur Livre (200 pages, édité par Éditeur Livre)")

    def test_cd(self):
        cd = CD("Titre CD", "Auteur CD", "2024", 60, 10)
        self.assertEqual(str(cd), "CD: Titre CD - Auteur CD (60 minutes, 10 morceaux)")

    def test_dvd(self):
        dvd = DVD("Titre DVD", "Auteur DVD", "2024", 120)
        self.assertEqual(str(dvd), "DVD: Titre DVD - Auteur DVD (120 minutes)")

    def test_article_magazine(self):
        article = ArticleMagazine("Titre Article", "Auteur Article", "2024", "Magazine Test", 1, "10-15")
        self.assertEqual(str(article), "Article de magazine: Titre Article - Auteur Article (Magazine Test, numéro 1, pages 10-15)")

    def test_marquer_comme_preté(self):
        medium = Medium("Titre Medium", "Auteur Medium", "2024")
        medium.marquer_comme_preté("Ami")
        self.assertTrue(medium.est_preté)
        self.assertEqual(medium.ami_prete, "Ami")

    def test_marquer_comme_rendu(self):
        medium = Medium("Titre Medium", "Auteur Medium", "2024")
        medium.marquer_comme_preté("Ami")
        medium.marquer_comme_rendu()
        self.assertFalse(medium.est_preté)
        self.assertIsNone(medium.ami_prete)


class TestGestionMedias(unittest.TestCase):
    def setUp(self):
        self.gestion_medias = GestionMedias()

    def test_ajouter_media(self):
        livre = Livre("Titre Livre", "Auteur Livre", "2024", 200, "Éditeur Livre")
        self.gestion_medias.ajouter_media(livre)
        self.assertIn(livre, self.gestion_medias.medias)

    def test_lister_medias_par_auteur(self):
        livre = Livre("Titre Livre", "Auteur Livre", "2024", 200, "Éditeur Livre")
        self.gestion_medias.ajouter_media(livre)
        medias_auteur_livre = self.gestion_medias.lister_medias_par_auteur("Auteur Livre")
        self.assertIn(livre, medias_auteur_livre)

    def test_supprimer_media(self):
        livre = Livre("Titre Livre", "Auteur Livre", "2024", 200, "Éditeur Livre")
        self.gestion_medias.ajouter_media(livre)
        self.gestion_medias.supprimer_media("Titre Livre", "Auteur Livre")
        self.assertNotIn(livre, self.gestion_medias.medias)

    def test_supprimer_medias_par_auteur(self):
        livre = Livre("Titre Livre", "Auteur Livre", "2024", 200, "Éditeur Livre")
        cd = CD("Titre CD", "Auteur CD", 2024, 60, 10)
        self.gestion_medias.ajouter_media(livre)
        self.gestion_medias.ajouter_media(cd)
        self.gestion_medias.supprimer_medias_par_auteur("Auteur Livre")
        self.assertNotIn(livre, self.gestion_medias.medias)
        self.assertIn(cd, self.gestion_medias.medias)

    def test_noter_media_emprunte(self):
        livre = Livre("Titre Livre", "Auteur Livre", "2024", 200, "Éditeur Livre")
        self.gestion_medias.ajouter_media(livre)
        self.gestion_medias.noter_media_emprunte("Titre Livre", "Auteur Livre", "Ami")
        self.assertTrue(livre.est_preté)

    def test_compter_medias_pretes(self):
        livre = Livre("Titre Livre", "Auteur Livre", "2024", 200, "Éditeur Livre")
        cd = CD("Titre CD", "Auteur CD", 2024, 60, 10)
        self.gestion_medias.ajouter_media(livre)
        self.gestion_medias.ajouter_media(cd)
        self.gestion_medias.noter_media_emprunte("Titre Livre", "Auteur Livre", "Ami")
        self.assertEqual(self.gestion_medias.compter_medias_pretes(), 1)

if __name__ == "__main__":
    unittest.main()
