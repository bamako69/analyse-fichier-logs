from collections import defaultdict

class IPTracker:
    def __init__(self, threshold=5):
        self.threshold = threshold
        self.counter = defaultdict(int)

    def ajouter(self, ip):
        self.counter[ip] += 1
        print(f"[INFO] {ip} → {self.counter[ip]} tentative(s)")
        return self.counter[ip]

    def est_suspecte(self, ip):
        return self.counter[ip] > self.threshold