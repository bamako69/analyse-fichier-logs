import re

def extract_ip(line):
    """
    Extrait l'IP depuis une ligne de log.
    """
    match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)
    if match:
        return match.group(1)
    return None