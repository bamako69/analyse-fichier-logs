import time
import re
fichier = "/Users/benjamindemoutiez/Desktop/faux_auth.log"


def lectureloge(file):
    """
    fonction qui permet de lire un fichier  en temps réelle ici passer en parametre
    :param file: chemin vers le fichier
    :return: (strings) le fichier ligne par ligne
    """
    with open(file) as f:
        while True:
            line = f.readline()
            if line:
                print(line, end="")
            else:
                time.sleep(0.1)


def analyselog(error, file):
    """
   fonction qui permert d'anlyser un fichier a la recherhce de l'erreur voulu
   :param error: type d'erreur rechercher
   :param file: fichier que l'on souhaite analyser
   :return: les line ou il y a l'erreur
   """
    for line in file:
        if error in line:
            print(f"erreur a la ligne " + line)


#def AnalyseErreur(file):




def extract_ip(line):
    """
    Extrait l'adresse IP depuis une ligne de log SSH.
    """
    match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)
    if match:
        return match.group(1)
    return None