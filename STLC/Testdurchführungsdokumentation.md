# Testdurchführungsdokumentation – Market Mate (Neue Funktionen)

**Tester:** Natalya Weiß  
**Testdatum:** 01.06.2026 – 05.06.2026  
**Testumgebung:** https://grocerymate.masterschool.com/  
**Version:** 1.0 (Final)

---

## 1. Testübersicht

| Feature | Testfälle geplant | Ausgeführt | Bestanden | Fehlgeschlagen | Blockiert |
|---------|------------------|------------|-----------|----------------|-----------|
| Bewertungssystem | 14 | 14 | 8 | 6 | 0 |
| Altersverifikation | 8 | 8 | 2 | 6 | 0 |
| Versandkosten | 6 | 6 | 3 | 3 | 0 |
| **Gesamt** | **28** | **28** | **13** | **15** | **0** |

**Bestandsquote:** 46,4%

---

## 2. Testumgebung

| Komponente | Details |
|------------|---------|
| **Anwendung** | Grocery Mate WebShop |
| **URL** | https://grocerymate.masterschool.com/ |
| **Browser (getestet)** | Chrome 128.0.6613.138, Firefox 151.0.2, Brave 1.90.128 |
| **Betriebssysteme (getestet)** | Windows 11, macOS 15.4, Android 16 (Redmi Note 14 Pro) |
| **Testnutzer** | test1@test.de / AdminTest! |
| **Testzeitraum** | 02.06.2026 – 05.06.2026 |

---

## 3. Testausführungsdetails

### 3.1 Feature 1: Bewertungssystem für Produkte

| ID | Testfall | Ergebnis | Bug-Referenz |
|----|----------|----------|--------------|
| R-01 | Bewertung abgeben (gekauftes Produkt) | ✅ PASSED | – |
| R-02 | Bewertung bearbeiten | ✅ PASSED | – |
| R-03 | Bewertung löschen | ✅ PASSED | – |
| R-04 | Bewertung ohne Login versuchen | ✅ PASSED | – |
| R-05 | Nicht gekauftes Produkt bewerten | ✅ PASSED | – |
| R-06 | Zweite Bewertung für selbes Produkt | ✅ PASSED | – |
| R-07 | Textfeld optional (leer) | ✅ PASSED | – |
| R-08 | 500 Zeichen (Maximum) | ❌ FAILED | #003 |
| R-09 | 501 Zeichen (Überschreitung) | ✅ PASSED | – |
| R-10 | Anonymität (ausgeloggt) | ❌ FAILED | #005 |
| R-10b | Anonymität (anderer Nutzer) | ❌ FAILED | #005 |
| R-11 | Anonymität nach Ausloggen | ❌ FAILED | #005 |
| R-12 | Sterne 1-5 | ✅ PASSED | – |
| R-13 | 0 Sterne (keine Auswahl) | ❌ FAILED | #001 |
| R-14 | Cancel-Button Funktion | ❌ FAILED | #003 |

### 3.2 Feature 2: Altersverifikation für alkoholische Produkte

| ID | Testfall | Ergebnis | Bug-Referenz |
|----|----------|----------|--------------|
| A-01 | Nutzer mit 18 Jahren (genau an der Grenze) | ✅ PASSED | – |
| A-02 | Nutzer mit 17 Jahren (1 Tag unter 18) | ✅ PASSED | – |
| A-03 | Nicht eingeloggter Nutzer ruft Alkohol-Kategorie auf | ❌ FAILED | #007, #010 |
| A-04 | Direkter URL-Aufruf eines Alkohol-Produkts | ❌ FAILED | #010 |
| A-05 | Modal durch ESC schließen versuchen | ✅ PASSED | – |
| A-06 | Ungültiges Datumsformat (Buchstaben/Sonderzeichen) | ❌ FAILED | #021 |
| A-07 | Geburtsdatum nachträglich ändern | ❌ FAILED | #015, #016 |
| A-08 | Geburtsdatum leer lassen | ❌ FAILED | #006, #012 |

### 3.3 Feature 3: Versandkosten (20€ frei / 5€ Standard)

| ID | Testfall | Ergebnis | Bug-Referenz |
|----|----------|----------|--------------|
| V-01 | Warenkorbwert genau 20,00 € | ✅ PASSED | – |
| V-02 | Warenkorbwert 19,99 € (unter Freibetrag) | ✅ PASSED | – |
| V-03 | Warenkorbwert 20,01 € (über Freibetrag) | ✅ PASSED | – |
| V-04 | Versandaktualisierung nach Artikelentfernung | ❌ FAILED | #024 |
| V-05 | Versandaktualisierung nach Stückzahlreduzierung | ❌ FAILED | #024 |
| V-06 | Versandkosten werden nicht auf Mindestbestellwert angerechnet | ✅ PASSED | – |

---

## 4. Mobile Testing (Redmi Note 14 Pro, Android 16)

Zusätzlich zu den geplanten Testfällen wurden mobile Tests durchgeführt:

| ID | Befund | Ergebnis | Bug-Referenz |
|----|--------|----------|--------------|
| M-01 | Verzogenes Logo, abgeschnittene Produktbilder | ❌ FAILED | #028 |
| M-02 | Category-Seitenleiste nicht versteckbar | ❌ FAILED | #028 |
| M-03 | Favoritenmaske – kein Zurück zum Shop | ❌ FAILED | #029 |
| M-04 | Banner "Delicious Salad Everyday" fehlt | ❌ FAILED | #030 |
| M-05 | "Shop Now"-Links ohne Funktion | ❌ FAILED | #026 |

---

## 5. Zusammenfassung der gefundenen Bugs

| Bug # | Titel | Priorität | Feature |
|-------|-------|-----------|---------|
| #001 | 500 Zeichen abgelehnt + 0 Sterne akzeptiert | 🟠 Medium | Bewertung |
| #002 | Keine Zeichenlimit-Prüfung beim Bearbeiten | 🟡 Low | Bewertung |
| #003 | Cancel-Button ohne Funktion | 🟡 Low | Bewertung |
| #004 | Exponentialdarstellung – keine Stückzahlbegrenzung | 🔴 Critical | Warenkorb |
| #005 | Keine Anonymisierung (DSGVO) | 🟠 Medium | Bewertung |
| #006 | Alkohol-Zugriff nach Ausloggen möglich | 🔴 Critical | Altersverifikation |
| #007 | Direkter URL-Zugriff ohne Altersprüfung | 🔴 Critical | Altersverifikation |
| #008 | Berechtigungsleck – Bewertung pro Produkt gesperrt | 🟠 Medium | Bewertung |
| #009 | Session-Überschneidung zwischen Tabs | 🟠 Medium | Session |
| #010 | Session bleibt, Altersprüfung wiederholt | 🔴 Critical | Altersverifikation |
| #011 | Tippfehler "Alocohol" | 🟡 Low | Kosmetik |
| #012 | Keine rechtssichere Altersprüfung | 🔴 Critical | Altersverifikation |
| #013 | Keine Bestellhistorie | 🟠 Medium | Bestellung |
| #014 | Geburtsdatum nicht änderbar | 🟠 Medium | Altersverifikation |
| #015 | Kein Benutzerprofil (DSGVO) | 🔴 Critical | Benutzerkonto |
| #016 | Fehlende rechtliche Seiten | 🔴 Critical | Rechtlich |
| #017 | Keine visuelle Rückmeldung bei Favoriten | 🟡 Low | Favoriten |
| #018 | Favoriten-Status in Kachelansicht nicht sichtbar | 🟡 Low | Favoriten |
| #019 | Pop-up-Feedback bei Favoriten nicht korrekt | 🟡 Low | Favoriten |
| #020 | Pflichtfelder nicht markiert | 🟡 Low | UX |
| #021 | Buchstaben/Sonderzeichen im Geburtsdatum | 🟠 Medium | Altersverifikation |
| #022 | Keine Warenkorb-Funktion auf Detailseite | 🟠 Medium | Warenkorb |
| #023 | Keine Sanitization – Injection-Angriffe | 🔴 Critical | Sicherheit |
| #024 | Versandaktualisierung fehlerhaft (finanzielle Ausnutzung) | 🔴 Critical | Versand |
| #025 | Keine Passwort-Sichtbarkeit bei Registrierung/Login | 🟠 Medium | Login |
| #026 | "Shop Now"-Links ohne Funktion | 🟡 Low | Kosmetik |
| #027 | Lange Session → Warenkorb/Favoriten fehlschlagen | 🟠 Medium | Session |
| #028 | Mobile Layout-Probleme | 🟡 Low | Mobile |
| #029 | Mobile – kein Zurück aus Favoriten | 🟠 Medium | Mobile |
| #030 | Mobile – Banner fehlen + Links tot | 🟡 Low | Mobile |

**Gesamt:** 30 Bugs (10 Critical, 10 Medium, 10 Low)

---

## 6. Risiken & Empfehlungen

### Kritische Risiken (Showstopper für Go-Live)

| Bug | Risiko | Handlungsempfehlung |
|-----|--------|---------------------|
| #004 | Wirtschaftlicher Schaden durch Millionenbestellungen | Maximale Stückzahl einführen |
| #006, #007, #010 | Umgehung der Altersverifikation | Serverseitige Prüfungen implementieren |
| #015, #016 | DSGVO-Verstöße (Bußgeld bis 20 Mio. €) | Benutzerprofil + rechtliche Seiten einfügen |
| #023 | Injection-Angriffe möglich (XSS, SQL) | Eingabevalidierung + Sanitization einbauen |
| #024 | Finanzielle Ausnutzung des Versands | Versandaktualisierung bei jeder Warenkorb-Änderung |

### Empfehlung an den Product Owner

> **Der Webshop kann in der aktuellen Form nicht live gehen.**  
> 10 kritische Bugs (davon 4 mit rechtlichen und finanziellen Risiken) müssen vor einem Go-Live behoben werden.  
> Besonders dringlich: DSGVO-Verstöße (#015, #016) und Sicherheitslücken (#004, #006, #007, #010, #023, #024).

---

## 7. Anhänge

- **Testdaten:** test1@test.de / AdminTest!
- **Issues:** https://github.com/uniquebughuntress/portfolio/issues ( #3 – #30 )
- **Screenshots:** In den jeweiligen Issues enthalten
- **Testprotokolle:** Siehe Testfallentwurf_v2.md

---

## Versionshistorie

| Version | Datum | Änderungen |
|---------|-------|------------|
| **1.0** | **2026-06-05** | **Finale Version nach vollständiger Testdurchführung mit 28 Testfällen und 30 gefundenen Bugs** |
