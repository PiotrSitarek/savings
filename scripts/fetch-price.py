#!/usr/bin/env python3
import json
import urllib.request
from datetime import datetime, timezone

def get_eur_pln_rate():
    url = "https://api.nbp.pl/api/exchangerates/rates/a/eur/?format=json"
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        data = json.loads(resp.read().decode())
    return float(data["rates"][0]["mid"])

def get_vwce_price_eur():
    url = "https://query1.finance.yahoo.com/v8/finance/chart/VWCE.DE?range=5d&interval=1d"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0", "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        data = json.loads(resp.read().decode())
    closes = data["chart"]["result"][0]["indicators"]["quote"][0]["close"]
    for c in reversed(closes):
        if c is not None:
            return round(c, 2)
    raise ValueError("Brak ceny")

def main():
    eur_pln = get_eur_pln_rate()
    price_eur = get_vwce_price_eur()
    price_pln = round(price_eur * eur_pln, 2)
    result = {
        "etf_price_eur": price_eur,
        "eur_pln_rate": eur_pln,
        "etf_price_pln": price_pln,
        "updated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    }
    with open("price.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(f"OK: VWCE = {price_eur} EUR = {price_pln} PLN")

if __name__ == "__main__":
    main()
