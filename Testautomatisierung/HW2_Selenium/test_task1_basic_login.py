# test_task1_basic_login.py
# Erstellt: 12.06.26 um 13:21
# Autor: natalya
# Projekt: QA-Portfolio

"""
## Aufgabe 1 (**Web-Automatisierung mit Selenium**)
Deine Aufgabe ist es, die folgenden Aktionen auf einer Demo-E-Commerce-Website zu automatisieren:

**URL:** https://www.saucedemo.com/

1. **Login-Automatisierung**
    Automatisiere den Login-Prozess für die Website mit den bereitgestellten Testzugangsdaten.
    
2. **Produkt-Such-Verifikation**
    Navigiere nach dem Login zur Produktseite und überprüfe das Vorhandensein bestimmter Produktnamen.
    

---

1. **Auf der Website einloggen**
    - Navigiere zu https://www.saucedemo.com/.
    - Finde und interagiere mit dem Login-Formular:
        - Gib den Benutzernamen ein: `standard_user`.
        - Gib das Passwort ein: `secret_sauce`.
        - Klicke auf die Schaltfläche **"Login"**.
    - Überprüfe, ob du dich erfolgreich eingeloggt hast, indem du den Seitentitel oder Elemente der Produktseite prüfst.
2. **Bestimmtes Produkt überprüfen**
    - Nachdem du dich eingeloggt hast, finde und überprüfe das Vorhandensein des folgenden Produkts:
        - Produktname: **"Sauce Labs Backpack"**.
    - Stelle sicher (assert), dass der Produktname auf der Seite angezeigt wird.
"""
