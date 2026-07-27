# 🌱 Moje Oszczędności — tracker wpłat siostrzenicy

Prosta strona na GitHub Pages pokazująca:
- **Wpłaty siostrzenicy** — ile udało się odłożyć
- **Z dopłatą wujka (×2)** — za każdą złotówkę wujek dokłada drugą
- **Wartość inwestycji** — ile warte są jednostki ETF VWCE dziś

Cena ETF aktualizuje się automatycznie co piątek przez GitHub Actions.

---

## Jak dodać nową wpłatę

1. Otwórz plik `data.json` na GitHubie (kliknij ołówek do edycji)
2. Dopisz nową linijkę w tablicy `transactions`:

```json
{ "date": "2026-08-01", "deposit": 200, "buy_price_pln": 572.30, "units": 0.6990 }
```

| Pole | Co wpisać | Skąd wziąć |
|------|-----------|------------|
| `date` | Data wpłaty | Kalendarz |
| `deposit` | Kwota wpłaty siostrzenicy w PLN | Przelew |
| `buy_price_pln` | Cena 1 jednostki VWCE w PLN | Potwierdzenie transakcji u brokera |
| `units` | Ile jednostek kupiono | Potwierdzenie transakcji u brokera |

3. Kliknij "Commit changes"
4. Strona zaktualizuje się w ciągu minuty

**Ważne:** `units` to ile jednostek kupił broker za **podwojoną** kwotę (wpłata siostrzenicy + dopłata wujka).

---

## Automatyczna aktualizacja ceny

GitHub Actions uruchamia skrypt `scripts/fetch-price.py` co piątek o 18:00 CET.  
Skrypt pobiera:
- cenę VWCE.DE z Yahoo Finance (EUR)
- kurs EUR/PLN z API Narodowego Banku Polskiego
- oblicza cenę w PLN i zapisuje do `price.json`

Możesz też uruchomić aktualizację ręcznie:  
GitHub → Actions → "Aktualizacja ceny VWCE" → "Run workflow"

---

## Uruchomienie na GitHub Pages

1. Wrzuć to repo na GitHub
2. Settings → Pages → Source: "Deploy from a branch" → Branch: `main` → Folder: `/ (root)`
3. Poczekaj ~1 minutę — strona będzie dostępna pod `https://TWÓJ-USERNAME.github.io/NAZWA-REPO/`

---

## Struktura plików

```
├── index.html          ← strona (HTML + CSS + JS)
├── data.json           ← wpłaty (edytujesz ręcznie)
├── price.json          ← aktualna cena ETF (auto-aktualizowane)
├── scripts/
│   └── fetch-price.py  ← skrypt pobierający cenę
├── .github/
│   └── workflows/
│       └── update-price.yml  ← cron co piątek
└── README.md
```
