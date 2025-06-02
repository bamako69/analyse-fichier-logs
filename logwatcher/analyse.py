import re
import time
from logwatcher.utils import extract_ip
from logwatcher.ip_tracker import IPTracker
from logwatcher.alerting import send_alert_email

def intrusion(filepath, pattern="invalid user", threshold=5):
    regex = re.compile(pattern)
    tracker = IPTracker(threshold=threshold)

    with open(filepath) as f:
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.1)
                continue

            if regex.search(line):
                ip = extract_ip(line)
                if ip:
                    tracker.ajouter(ip)
                    if tracker.est_suspecte(ip):
                        print(f"[ALERTE] L'IP {ip} a dépassé {threshold} tentatives !")
                        send_alert_email(ip)

            if sum(tracker.counter.values()) > 30:
                break
