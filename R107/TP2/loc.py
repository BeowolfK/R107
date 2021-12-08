#!/usr/bin/env python3

"""
Calcul du meilleur choix selon les entrees utilisateur sur la distance a parcourir ainsi que la durée de la location
"""

def main():
    """La fonction calcule le choix optimal pour la location en fonction de la durée de location et du kilométrage"""
    voiture = {
        "essence" : {
            'location' : 40,
            'kilometrage' : 0.15
            },
        "diesel" : {
            'location' : 50,
            'kilometrage' : 0.10
            }
        }
    jour = int(input('Pour combien de jour souhaitez vous louer votre voiture? '))
    dist = int(input('Pour combien de kilometre souhaitez vous louer votre voiture? '))
    essence = jour * voiture["essence"]["location"] + dist * voiture["essence"]["kilometrage"]
    diesel = jour * voiture["diesel"]["location"] + dist * voiture["diesel"]["kilometrage"]
    print(f"Avec un véhicule à essence : {essence}")
    print(f"Avec un véhicule diesel : {diesel}")
    print("Véhicule à essence conseillé" if essence < diesel else "Véhicule diesel conseillé")

if __name__ == '__main__':
    main()