# Password Manager

## Opis projektu

Password Manager to aplikacja napisana w Pythonie, wykorzystująca bibliotekę Tkinter do stworzenia prostego interfejsu graficznego. Umożliwia użytkownikom generowanie, przechowywanie i wyszukiwanie haseł w pliku JSON.

## Funkcjonalności

- **Generowanie haseł** – losowo generowane hasło zawierające co najmniej 8 liter, 2 cyfry i 2 znaki specjalne.
- **Zapis do pliku** – przechowywanie informacji o stronie, e-mailu oraz haśle w pliku `data.json`.
- **Wyszukiwanie haseł** – możliwość szybkiego znalezienia hasła dla danej strony.
- **Graficzny interfejs użytkownika** – oparty na Tkinterze, ułatwiający obsługę programu.

## Wymagania

- Python 3
- Biblioteki: Tkinter, json, random

## Instalacja i uruchomienie

1. Pobierz pliki projektu.
2. Upewnij się, że masz zainstalowanego Pythona.
3. Uruchom skrypt:
   ```sh
   python main.py
   ```

## Struktura pliku JSON

Dane są przechowywane w formacie JSON:
```json
{
    "example.com": {
        "email": "yourmail@gmail.com",
        "password": "generated_password"
    }
}
```

## Przykładowe użycie

- Wpisz nazwę strony.
- Podaj adres e-mail (domyślnie ustawiony w kodzie).
- Wygeneruj hasło lub wpisz własne.
- Kliknij "Add", aby zapisać dane.
- Użyj "Search", aby znaleźć zapisane hasło dla danej strony.



