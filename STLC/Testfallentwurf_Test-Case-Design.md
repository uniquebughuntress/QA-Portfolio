# Test Case Design (Testfallentwurf) – Market Mate (Neue Funktionen)

## Testentwurfstechniken (verwendet)
- **Äquivalenzklassenbildung (EP)** – für gültige/ungültige Eingaben
- **Grenzwertanalyse (BVA)** – für Altersgrenze (18), Versandkostenfreibetrag (50,00€), Textlängen
- **Fehlerermessen (Error Guessing)** – für Umgehungsversuche (ESC, direkte URLs)
- **Anwendungsfalltest (Use Case)** – für typische Nutzerpfade

---

## Feature 1: Bewertungssystem für Produkte

### Testfälle

| ID | Testfall | Testtechnik | Eingabe | Erwartetes Ergebnis | Automatisierung |
|----|----------|-------------|---------|---------------------|-----------------|
| R-01 | Bewertung abgeben als eingeloggter Nutzer mit gekauftem Produkt | Use Case Test | Login → gekauftes Produkt → 4 Sterne auswählen → Kommentar "Gut" → "Send" | Bewertung erscheint in der Liste oben, Durchschnittsbewertung und Anzahl der Bewertungen aktualisiert sich| ✅ Ja |
| R-02 | Bewertung ändern (bearbeiten) | Use Case Test | Eingeloggt → bereits bewertetes Produkt aufrufen → "Edit" → Sterne von 4 auf 5 ändern → Text ändern → "Save Changes" | Bewertung wird aktualisiert (kein zweiter Eintrag)| ✅ Ja |
| R-03 | Bewertung löschen | Use Case Test | Eingeloggt → eigene Bewertung → "Delete" → Bestätigung "OK" | Bewertung verschwindet aus UI, Durchschnitt und Anzahl der Bewertungen wird neu berechnet, keine Fehlermeldung | ✅ Ja |
| R-04 | Bewertung ohne Login versuchen | Error Guessing | **Vorbedingung:** Browser im privaten Modus. Altersprüfung mit 01.01.2000 bestehen → beliebiges Produkt (nicht gekauft) → kein Login | Bewertungs-UI vollständig ausgeblendet, Hinweistext "You need to buy this product to tell us your opinion!" sichtbar | ✅ Ja |
| R-05 | Als eingeloggter Nutzer Produkt bewerten, das nicht gekauft wurde | Äquivalenzklassenbildung (EP) | Eingeloggt → Produkt ohne Kaufhistorie aufrufen | Bewertungsfeld nicht sichtbar, Hinweistext "You need to buy this product to tell us your opinion!" | ✅ Ja |
| R-06 | Zweite Bewertung für selbes Produkt | Error Guessing | Eingeloggt → bereits bewertetes Produkt → erneut Bewertung versuchen | Bewertungsfeld durch "You have already reviewed this product" ersetzt. Nur Buttons "Edit" und "Delete" in abgegebener Bewertung vorhanden | ✅ Ja |
| R-07 | Textfeld ist optional | Äquivalenzklassenbildung (EP) | Eingeloggt, gekauftes Produkt → 5 Sterne auswählen → Textfeld leer → "Send" | Bewertung wird gespeichert, Kommentar ist leer/null, 5 Sterne werden angezeigt | ✅ Ja |
| R-08 | Text auf 500 Zeichen begrenzt (Maximum)| Grenzwertanalyse (BVA) | Text mit genau 500 Zeichen | Bewertung wird akzeptiert | ✅ Ja |
| R-09 | Text mit 501 Zeichen (Überschreitung des Limits laut Anforderung) | Grenzwertanalyse (BVA) | 501 Zeichen eingeben → "Send" | Fehlermeldung "Maximal 500 Zeichen erlaubt" | ✅ Ja |
| R-10 | Anonymität für nicht eingeloggte Besucher | Error Guessing | Nutzer A (eingeloggt) gibt Bewertung ab → Nicht eingeloggter Besucher ruft Produkt auf | Name wird durch "Kunde" ersetzt | ✅ Ja |
| R-10b | Sichtbarkeit für andere eingeloggte Nutzer | Error Guessing | Nutzer A bewertet → Nutzer B (eingeloggt) ruft selbes Produkt auf | Bewertung von A ist für B unter "Kunde" sichtbar| ❌ Manuell |
| R-11 | Anonymität nach Ausloggen | Error Guessing | Nutzer A bewertet → loggt aus → ruft Produkt erneut auf (nicht eingeloggt) | Name wird durch "Kunde" ersetzt (anonymisiert) | ✅ Ja |
| R-12 | Sterne-Bewertung mit gültigen Werten (1,2,3,4,5) | Äquivalenzklassenbildung (EP) | Eingeloggt, gekauftes Produkt → jeweils 1,2,3,4, 5 Sterne auswählen → jeweils "Save Changes" bzw. "Send" | Jede Bewertung wird akzeptiert, die entsprechende Sternzahl wird gespeichert und angezeigt | ✅ Ja |
| R-13 | Sterne-Bewertung ohne Auswahl (0 Sterne) | Grenzwertanalyse (BVA) – untere Grenze | Eingeloggt, gekauftes Produkt → **keinen** Stern auswählen → "Send" | Fehlermeldung: "Invalid input for the field 'Rating'. Please check your input." | ✅ Ja |

---

## Zusammenfassung – Feature 1

| Feature | Anzahl Testfälle | Automatisierbar | Manuell |
|---------|-----------------|-----------------|---------|
| Bewertungssystem | **14** | **13** | **1** |

**Automatisierungsquote:** ~93%

**Automatisierungsbegründung:**  
Hohe Wiederholrate, Regression relevant. R-10b erfordert zwei parallele Nutzer-Sessions mit visueller UI-Prüfung und wird daher manuell ausgeführt.

---

## Feature 2: Altersverifikation für alkoholische Produkte

### Testfälle (mindestens 3 pro Feature, hier 8)

| ID | Testfall | Testtechnik | Eingabe | Erwartetes Ergebnis | Automatisierung |
|----|----------|-------------|---------|---------------------|-----------------|
| A-01 | Nutzer mit 18 Jahren (genau an der Grenze) | Grenzwertanalyse (BVA) | Geburtsdatum = Heute - 18 Jahre | Zugriff auf Alkohol-Kategorie gewährt | **Ja** (Grenzwert) |
| A-02 | Nutzer mit 17 Jahren (1 Tag unter 18) | Grenzwertanalyse (BVA) | Geburtsdatum = Heute - 18 Jahre + 1 Tag | Meldung "Sie sind unter 18", Kategorie gesperrt | **Ja** (Grenzwert) |
| A-03 | Nicht eingeloggter Nutzer ruft Alkohol-Kategorie auf | Fehlerermessen | Nicht eingeloggt → Kategorie Alkohol | Meldung "Bitte loggen Sie sich ein" | **Ja** (Sicherheit) |
| A-04 | Direkter URL-Aufruf eines Alkohol-Produkts ohne Verifikation | Sicherheitstest | URL direkt eingeben: /products/wein-123 | Meldung "Zugriff verweigert" oder Weiterleitung | **Ja** (Sicherheit) |
| A-05 | Modal durch ESC schließen versuchen | Fehlerermessen | Modal offen → ESC-Taste drücken | Modal bleibt geöffnet, keine Umgehung | **Nein** (UI-interaktiv) |
| A-06 | Ungültiges Datumsformat (31.13.2000) | Äquivalenzklasse | Eingabe: 31-13-2000 | Fehlermeldung "Ungültiges Datum. Format TT-MM-JJJJ" | **Ja** (Validierung) |
| A-07 | Geburtsdatum nachträglich im Profil ändern (von 17 auf 18) | Anwendungsfalltest | Profil: Ändere Geburtstag von <18 auf 18+ | Alkohol-Kategorie wird sofort freigeschaltet | **Ja** (Dynamik) |
| A-08 | Geburtsdatum leer lassen | Fehlerermessen | Feld leer → Speichern | Fehlermeldung "Geburtsdatum erforderlich" | **Ja** (Pflichtfeld) |

**Automatisierungsbegründung:** Grenzwert- und Sicherheitstests ideal für Automatisierung (wiederholbar, schnell). ESC-Test manuell wegen UI-Interaktion.

---

## Feature 3: Versandkosten (geänderte Regeln)

### Testfälle (mindestens 3 pro Feature, hier 8)

| ID | Testfall | Testtechnik | Eingabe | Erwartetes Ergebnis | Automatisierung |
|----|----------|-------------|---------|---------------------|-----------------|
| V-01 | Warenkorbwert genau 50,00 € (Standardversand) | Grenzwertanalyse (BVA) | Produkte summieren auf 50,00 € → Standardversand | Versandkosten = 0,00 € (kostenfrei) | **Ja** (Grenzwert) |
| V-02 | Warenkorbwert 49,99 € (unter Freibetrag) | Grenzwertanalyse (BVA) | Summe 49,99 € → Standardversand | Versandkosten = 4,99 € | **Ja** (Grenzwert) |
| V-03 | Warenkorbwert 50,01 € (über Freibetrag) | Grenzwertanalyse (BVA) | Summe 50,01 € → Standardversand | Versandkosten = 0,00 € | **Ja** (Grenzwert) |
| V-04 | Warenkorb mit Alkohol → Expressversand auswählen | Fehlerermessen | Alkohol im Warenkorb → Express auswählen | Express-Option deaktiviert/grau, Tooltip "Express nicht für Alkohol" | **Ja** (Geschäftslogik) |
| V-05 | Gemischter Warenkorb (Alkohol + normal) | Anwendungsfalltest | Alkohol + TK-Produkt → Standard/Express? | Nur Standard verfügbar (Alkohol erzwingt) | **Ja** (Priorität) |
| V-06 | Gemischter Warenkorb (Normal + Express-Produkt) | Äquivalenzklasse | Normales Produkt + Express-Produkt | Teuerste Versandart: Express (9,99€) | **Ja** (Max-Logik) |
| V-07 | Rabatt reduziert Warenkorb unter 50€ | Grenzwertanalyse | Brutto 60€, Rabatt 15€ → Netto 45€ → Standard | Versandkosten = 4,99€ (da nach Rabatt <50€) | **Ja** (Rabatt-Integration) |
| V-08 | Versandkosten werden nicht auf Mindestbestellwert angerechnet | Fehlerermessen | Warenwert 48€ + Versand 4,99€ = 52,99€ → aber Freibetrag? | Keine Versandkostenfreiheit (nur Warenwert zählt) | **Ja** (Logiktest) |

**Automatisierungsbegründung:** Grenzwert- und Rabattlogik hervorragend automatisierbar. Manuelle Tests nur für komplexe UI-Fälle (Express-Deaktivierung visuell prüfen).

---

## Zusammenfassung Automatisierungsempfehlung

| Feature | Automatisierbare Tests | Manuelle Tests | Begründung |
|---------|----------------------|----------------|-------------|
| Bewertungssystem | 6 von 7 | 1 (UI-Flow komplex) | Hohe Wiederholrate, Regression |
| Altersverifikation | 7 von 8 | 1 (ESC/Click-Outside) | Sicherheitstests ideal automatisiert |
| Versandkosten | 8 von 8 | 0 | Reine Rechenlogik, perfekt automatisierbar |

**Gesamt:** 21 von 23 Testfälle automatisiert (91% Automatisierungsgrad)
