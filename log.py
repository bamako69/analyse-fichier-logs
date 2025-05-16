import time
import re
import smtplib
from email.message import EmailMessage
from collections import defaultdict

fichier = "/Users/benjamindemoutiez/Desktop/faux_auth.log"


def monitor_log(file, error_pattern):
    """
    fonction qui lit un fichier log a la recherche d'erreur et revoie l'IP qui a provoqué l'erreur
    :param file:fichier que l'on souhaite parcourir
    :param error_pattern: erreur que l'on souhaite detecter
    """
    regex = re.compile(error_pattern)
    with open(file) as f:
        while True:
            line = f.readline()
            if line:
                if regex.search(line):
                    ip = extract_ip(line)
                    print(f"[ALERTE] {line.strip()} — IP: {ip}")
                    return ip
            else:
                time.sleep(0.1)


def extract_ip(line):
    """
    fonction qi extrait l'ip de la ligne donné
    :param line: ligne ou on veux recupérer l'ip
    :return: l'ip de la ligne
    """
    match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)
    if match:
        return match.group(1)
    return None





def send_alert_email():
    """
    fonction qui envoye un mail depuis une adresse fixe vers une adresse fix
    """
    sender_email = "demoutiezbenjamin22@gmail.com"
    receiver_email = "mini.mamout@gmail.com"
    app_password = "gsai nxgu lwkl rwys"

    msg = EmailMessage()
    msg["Subject"] = "Alerte : activité suspecte détectée"
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg.set_content("Une IP a dépassé le seuil autorisé de tentatives de connexion.")

    # Connexion au serveur Gmail
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender_email, app_password)
        smtp.send_message(msg)
        print("Alerte envoyée avec succès !")



def intrusion(filepath, pattern="invalid user", threshold=5):
    regex = re.compile(pattern)
    ip_counter = defaultdict(int)

    with open(filepath) as f:
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.1)
                continue

            if regex.search(line):
                ip = extract_ip(line)
                if ip:
                    ip_counter[ip] += 1
                    print(f"[INFO] {ip} → {ip_counter[ip]} tentative(s)")

                    if ip_counter[ip] > threshold:
                        print(f"[ALERTE] L'IP {ip} a dépassé {threshold} tentatives !")
                        send_alert_email()

            if sum(ip_counter.values()) > 30:
                break

intrusion(fichier)