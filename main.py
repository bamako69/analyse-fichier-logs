#!/usr/bin/env python3

import argparse
from logwatcher.analyse import intrusion

def main():
    parser = argparse.ArgumentParser(description="Détection d'intrusion SSH via logs.")
    parser.add_argument("-f", "--file", required=True, help="Chemin vers le fichier de log")
    parser.add_argument("-t", "--threshold", type=int, default=5, help="Seuil de tentatives avant alerte")

    args = parser.parse_args()

    print(f" Analyse du fichier : {args.file}")
    print(f" Seuil : {args.threshold}")
    intrusion(args.file, threshold=args.threshold)

if __name__ == "__main__":
    main()
