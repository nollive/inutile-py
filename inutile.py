## Script inutile pour assouvir ma curiosité vis à vis du petit "easter egg" laissé dans le "The Password Security Checker" de Estatis Inc. (disponible à l'adresse https://inutile.club/estatis/password-security-checker/ (lien valide le 20/03/2024)
## ce script est inutile, c'est un peu le serpent qui se mort la queue...

import requests
from bs4 import BeautifulSoup

def get_h2_texts(password, count):
    url = "https://inutile.club/estatis/password-security-checker/index.php"
    data = {
        "password": password,
        "count": str(count)
    }

    # requête post pour récuperer les précieuses informations
    response = requests.post(url, data=data)

    # on utilise bs comme scraper
    soup = BeautifulSoup(response.text, 'html.parser')

    # notre graal se trouve dans une balise h2
    h2_tags = soup.find_all('h2', text=True)
    # mais attention, on ne veut pas recuperer les balises h2 inutile... (pas très élegant mais je suis impatient
    h2_texts = [tag.text.strip() for tag in h2_tags if "Enterprise products" not in tag.text and "Terms and conditions" not in tag.text]

    return h2_texts

print("Le script inutile tourne en continu...")

count = 1

while True: #miam
    password = "inutile"  # autant choisir un mot de passe inspiré pour plus de sécurité

    h2_texts = get_h2_texts(password, count)
    
    # Un petit print console pour voir comment ça évolue
    print(f"Contenu des balises h2 ({count}e requête) :")
    for text in h2_texts:
        print(text)

    # on immortalise ça dans un fichier texte
    with open("h2_contents.txt", "a") as file:
        file.write(f"Contenu des balises h2 ({count}e requête) :\n")
        for text in h2_texts:
            file.write(text + "\n")
        file.write("\n")

    count += 1  # +1 requête inutile

