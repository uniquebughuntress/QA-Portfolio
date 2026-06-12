# Test Case Design (Testfallentwurf) – Market Mate (Neue Funktionen)

## Testentwurfstechniken (verwendet)
- **Äquivalenzklassenbildung (EP)** – für gültige/ungültige Eingaben
- **Grenzwertanalyse (BVA)** – für Altersgrenze (18), Versandkostenfreibetrag (20,00€), Textlängen (500 Zeichen)
- **Fehlerermessen (Error Guessing)** – für Umgehungsversuche (ESC, direkte URLs)
- **Anwendungsfalltest (Use Case)** – für typische Nutzerpfade

---

## Feature 1: Bewertungssystem für Produkte

### Testfälle

| ID | Testfall | Testtechnik | Eingabe | Erwartetes Ergebnis | Automatisierung | Bug-Referenz |
|----|----------|-------------|---------|---------------------|-----------------|--------------|
| R-01 | Bewertung abgeben als eingeloggter Nutzer mit gekauftem Produkt | Use Case Test | Login → gekauftes Produkt → 4 Sterne auswählen → Kommentar "Gut" → "Send" | Bewertung erscheint in der Liste oben, Durchschnittsbewertung und Anzahl der Bewertungen aktualisiert sich | ✅ Ja | – |
| R-02 | Bewertung ändern (bearbeiten) | Use Case Test | Eingeloggt → bereits bewertetes Produkt aufrufen → "Edit" → Sterne von 4 auf 5 ändern → Text ändern → "Save Changes" | Bewertung wird aktualisiert (kein zweiter Eintrag) | ✅ Ja | – |
| R-03 | Bewertung löschen | Use Case Test | Eingeloggt → eigene Bewertung → "Delete" → Bestätigung "OK" | Bewertung verschwindet aus UI, Durchschnitt und Anzahl der Bewertungen wird neu berechnet, keine Fehlermeldung | ✅ Ja | – |
| R-04 | Bewertung ohne Login versuchen | Error Guessing | **Vorbedingung:** Browser im privaten Modus. Altersprüfung mit 01.01.2000 bestehen → beliebiges Produkt (nicht gekauft) → kein Login | Bewertungs-UI vollständig ausgeblendet, Hinweistext "You need to buy this product to tell us your opinion!" sichtbar | ✅ Ja | – |
| R-05 | Als eingeloggter Nutzer Produkt bewerten, das nicht gekauft wurde | Äquivalenzklassenbildung (EP) | Eingeloggt → Produkt ohne Kaufhistorie aufrufen | Bewertungsfeld nicht sichtbar, Hinweistext "You need to buy this product to tell us your opinion!" | ✅ Ja | #008 |
| R-06 | Zweite Bewertung für selbes Produkt | Error Guessing | Eingeloggt → bereits bewertetes Produkt → erneut Bewertung versuchen | Bewertungsfeld durch "You have already reviewed this product" ersetzt. Nur Buttons "Edit" und "Delete" in abgegebener Bewertung vorhanden | ✅ Ja | – |
| R-07 | Textfeld ist optional | Äquivalenzklassenbildung (EP) | Eingeloggt, gekauftes Produkt → 5 Sterne auswählen → Textfeld leer → "Send" | Bewertung wird gespeichert, Kommentar ist leer/null, 5 Sterne werden angezeigt | ✅ Ja | – |
| R-08 | Text auf 500 Zeichen begrenzt (Maximum) | Grenzwertanalyse (BVA) | Text mit genau 500 Zeichen | Bewertung wird akzeptiert | ✅ Ja | #001 |
| R-09 | Text mit 501 Zeichen (Überschreitung des Limits) | Grenzwertanalyse (BVA) | 501 Zeichen eingeben → "Send" | Fehlermeldung "Maximal 500 Zeichen erlaubt" | ✅ Ja | #001 |
| R-10 | Anonymität für nicht eingeloggte Besucher | Error Guessing | Nutzer A (eingeloggt) gibt Bewertung ab → Nicht eingeloggter Besucher ruft Produkt auf | Name wird durch **"Kunde"** ersetzt | ✅ Ja | #005 |
| R-10b | Sichtbarkeit für andere eingeloggte Nutzer | Error Guessing | Nutzer A bewertet → Nutzer B (eingeloggt) ruft selbes Produkt auf | Bewertung von A ist für B unter **"Kunde"** sichtbar | ❌ Manuell | #005 |
| R-11 | Anonymität nach Ausloggen | Error Guessing | Nutzer A bewertet → loggt aus → ruft Produkt erneut auf (nicht eingeloggt) | Name wird durch **"Kunde"** ersetzt (anonymisiert) | ✅ Ja | #005 |
| R-12 | Sterne-Bewertung mit gültigen Werten (1,2,3,4,5) | Äquivalenzklassenbildung (EP) | Eingeloggt, gekauftes Produkt → jeweils 1,2,3,4,5 Sterne auswählen → "Send" | Jede Bewertung wird akzeptiert, die entsprechende Sternzahl wird gespeichert und angezeigt | ✅ Ja | – |
| R-13 | Sterne-Bewertung ohne Auswahl (0 Sterne) | Grenzwertanalyse (BVA) – untere Grenze | Eingeloggt, gekauftes Produkt → **keinen** Stern auswählen → "Send" | Fehlermeldung: "Invalid input for the field 'Rating'. Please check your input." | ✅ Ja | #001 |
| R-14 | Cancel-Button im Bewertungsfenster | Error Guessing | Bewertungsfenster öffnen → Sterne auswählen → Text eingeben → "Cancel" klicken | Entweder: Fenster schließt sich ODER Eingaben werden zurückgesetzt (Sterne = 0, Text leer) | ✅ Ja | #003 |

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

### Testfälle

| ID | Testfall | Testtechnik | Eingabe | Erwartetes Ergebnis | Automatisierung | Bug-Referenz |
|----|----------|-------------|---------|---------------------|-----------------|--------------|
| A-01 | Nutzer mit 18 Jahren (genau an der Grenze) | Grenzwertanalyse (BVA) | Geburtsdatum = Heute - 18 Jahre | Zugriff auf Alkohol-Kategorie gewährt | ✅ Ja | – |
| A-02 | Nutzer mit 17 Jahren (1 Tag unter 18) | Grenzwertanalyse (BVA) | Geburtsdatum = Heute - 18 Jahre + 1 Tag | Meldung "Sie sind unter 18", Kategorie gesperrt | ✅ Ja | – |
| A-03 | Nicht eingeloggter Nutzer ruft Alkohol-Kategorie auf | Fehlerermessen | Nicht eingeloggt → Kategorie Alkohol | Meldung "Bitte loggen Sie sich ein" | ✅ Ja | #007, #010 |
| A-04 | Direkter URL-Aufruf eines Alkohol-Produkts ohne Verifikation | Sicherheitstest | URL direkt eingeben: /products/alkohol-produkt-id | Meldung "Zugriff verweigert" oder Weiterleitung | ✅ Ja | #010 |
| A-05 | Modal durch ESC schließen versuchen | Fehlerermessen | Modal offen → ESC-Taste drücken | Modal bleibt geöffnet, keine Umgehung | ❌ Nein | – |
| A-06 | Ungültiges Datumsformat (Buchstaben/Sonderzeichen) | Äquivalenzklasse | Eingabe: `abc!!!` oder `31-13-2000` | Fehlermeldung "Ungültiges Datum. Format TT-MM-JJJJ" | ✅ Ja | #021 |
| A-07 | Geburtsdatum nachträglich ändern | Anwendungsfalltest | Geburtsdatum von <18 auf 18+ ändern | Alkohol-Kategorie wird sofort freigeschaltet | ✅ Ja | #015, #016 |
| A-08 | Geburtsdatum leer lassen | Fehlerermessen | Feld leer → Confirm klicken | Fehlermeldung "Geburtsdatum erforderlich" | ✅ Ja | – |

**Automatisierungsbegründung:** Grenzwert- und Sicherheitstests ideal für Automatisierung (wiederholbar, schnell). ESC-Test manuell wegen UI-Interaktion.

---

## Feature 3: Versandkosten (IST-Zustand: 20€ frei / 5€ Standard)

### Testfälle

| ID | Testfall | Testtechnik | Eingabe | Erwartetes Ergebnis | Automatisierung | Bug-Referenz |
|----|----------|-------------|---------|---------------------|-----------------|--------------|
| V-01 | Warenkorbwert genau 20,00 € (Grenze – kostenfrei) | Grenzwertanalyse (BVA) | Produkte summieren auf 20,00 € → Standardversand | Versandkosten = 0,00 € (kostenfrei) | ✅ Ja | – |
| V-02 | Warenkorbwert 19,99 € (unter Freibetrag) | Grenzwertanalyse (BVA) | Summe 19,99 € → Standardversand | Versandkosten = 5,00 € | ✅ Ja | – |
| V-03 | Warenkorbwert 20,01 € (über Freibetrag) | Grenzwertanalyse (BVA) | Summe 20,01 € → Standardversand | Versandkosten = 0,00 € | ✅ Ja | – |
| V-04 | Versandaktualisierung nach Artikelentfernung | Grenzwertanalyse | ≥20€ → Versand 0€ → Artikel entfernen → <20€ | Versandkosten werden wieder auf 5,00 € aktualisiert | ✅ Ja | #024 |
| V-05 | Versandaktualisierung nach Stückzahlreduzierung | Grenzwertanalyse | Durch "+" auf ≥20€ → Versand 0€ → Durch "-" auf <20€ | Versandkosten werden wieder auf 5,00 € aktualisiert | ✅ Ja | #024 |
| V-06 | Versandkosten werden nicht auf Mindestbestellwert angerechnet | Fehlerermessen | Warenwert 18€ + Versand 5€ = 23€ → aber Freibetrag? | Keine Versandkostenfreiheit (nur Warenwert zählt, 18€ < 20€) | ✅ Ja | – |
| V-07 | Expressversand (geplant – noch nicht implementiert) | Fehlerermessen | Expressversand auswählen (falls verfügbar) | Expressversand = 9,99 € (sobald implementiert) | ⏳ Nach Implementierung | – |
| V-08 | Alkohol + Express (geplant – noch nicht implementiert) | Fehlerermessen | Alkohol im Warenkorb → Express auswählen | Express-Option deaktiviert/grau | ⏳ Nach Implementierung | – |

**Automatisierungsbegründung:** Grenzwert- und Rechenlogik hervorragend automatisierbar.

---

## Zusammenfassung Automatisierungsempfehlung

| Feature | Automatisierbare Tests | Manuelle Tests | Begründung |
|---------|----------------------|----------------|-------------|
| Bewertungssystem | 13 von 14 | 1 (R-10b) | Hohe Wiederholrate, Regression |
| Altersverifikation | 7 von 8 | 1 (A-05) | Sicherheitstests ideal automatisiert |
| Versandkosten | 6 von 8 | 0 (2 geplant, noch nicht implementiert) | Reine Rechenlogik, perfekt automatisierbar |

**Gesamt:** 26 von 30 Testfälle automatisiert (87% Automatisierungsgrad)

---

## Versionshistorie

| Version | Datum | Änderungen |
|---------|-------|------------|
| v1 | 2026-06-02 | Initiale Version mit 50€/4,99€ |
| **v2** | **2026-06-05** | **Anpassung Versandwerte auf IST-Zustand (20€/5€); Ergänzung Bug-Referenzen; Präzisierung Anonymisierung ("Kunde")** |
