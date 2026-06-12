# Anforderungsanalyse – Grocery Mate Applikation (Final)

> **Version:** 2.0  
> **Datum:** 2026-06-05  
> **Änderungen gegenüber v1:** Anpassung der Versandkostenwerte auf IST-Zustand (20€/5€), Präzisierung der Anonymisierung ("Kunde"), Integration der Erkenntnisse aus der Testdurchführung (Bugs #3–#32)

## Basis-Funktionalitäten (bereits vorhanden – IST-Zustand)

| Funktion | Ist-Zustand | Bekannte Einschränkungen (Bugs) |
|----------|-------------|--------------------------------|
| Registrierung und Login | Funktioniert grundsätzlich | Keine Passwort-Sichtbarkeit (#25), keine Passwort-Bestätigung (#25) |
| Produktsuche mit Sortierfunktion | Funktioniert | – |
| Produkte zu Favoriten hinzufügen | Funktioniert | Keine visuelle Rückmeldung (#18, #19, #20), Mehrfachklicks führen zu Fehlern (#24) |
| Produkte in den Warenkorb legen | Funktioniert | Nicht auf Produktdetailseite (#23) |
| Bestellabschluss | Funktioniert grundsätzlich | Keine Validierung der Eingabefelder (#6, #23) |

---

## Feature 1: Bewertungssystem für Produkte

**Ursprünglich vage formulierte Anforderung:**  
> Nutzer sollen Produkte mit einem 5-Sterne-System bewerten und zusätzlich schriftliches Feedback hinterlassen können.

### Fragen zur Präzisierung (abgeleitet aus IST-Zustand des Webshops)

| Frage | Antwort (basierend auf IST-Zustand + sinnvoller SOLL-Ergänzung) |
|-------|----------------------------------------------------------------|
| 1. Dürfen nur eingeloggte Nutzer bewerten? | Ja, nur eingeloggte Nutzer (#3, R-04 bestätigt) |
| 2. Muss das Produkt zuvor gekauft worden sein? | Ja, nur gekaufte Produkte können bewertet werden (#3, R-05 bestätigt) |
| 3. Darf ein Nutzer ein Produkt mehrmals bewerten? | Nein, maximal eine Bewertung pro Nutzer und Produkt (#3, R-06 bestätigt) |
| 4. Können Bewertungen bearbeitet oder gelöscht werden? | Ja, einmal bearbeitbar, einmal löschbar (#3, R-02, R-03 bestätigt) |
| 5. Sind Bewertungen sofort sichtbar oder erst nach Freigabe? | Sofort sichtbar (keine Admin-Freigabe) (#3) |
| 6. Gibt es eine Mindest-/Maximallänge für Text? | Textfeld: optional, max. 500 Zeichen, keine Mindestlänge (#3, R-07, R-08, R-09) |
| 7. Werden Bewertungen anonym oder mit Benutzername angezeigt? | **Anonym: Der Name wird durch "Kunde" ersetzt** (#5, R-10, R-10b, R-11) |
| 8. Wie wird mit beleidigenden/unangemessenen Inhalten umgegangen? | Meldefunktion ist geplant, aber noch nicht implementiert (#5) |
| 9. Was passiert mit Bewertungen, wenn das Produkt gelöscht wird? | Alle Bewertungen werden ebenfalls gelöscht (Datenintegrität) (#3) |
| 10. Wie wird die Durchschnittsbewertung gerundet? | Kaufmännisch gerundet auf eine Dezimalstelle (z.B. 4,24 → 4,2) (#3) |

### Detaillierte Anforderungen (testbar – SOLL-Zustand)

| ID | Anforderung | Abgedeckt durch Testfall |
|----|-------------|--------------------------|
| ANF-BEW-01 | Nur eingeloggte Nutzer können Bewertungen abgeben | R-04 |
| ANF-BEW-02 | Ein Nutzer kann nur gekaufte Produkte bewerten | R-05 |
| ANF-BEW-03 | Ein Nutzer kann ein Produkt maximal einmal bewerten | R-06 |
| ANF-BEW-04 | Bewertungen können bearbeitet (Edit) und gelöscht (Delete) werden | R-02, R-03 |
| ANF-BEW-05 | Eine Bewertung besteht aus 1–5 Sternen (Pflichtfeld) | R-12, R-13 |
| ANF-BEW-06 | Das Textfeld ist optional (leerer Kommentar ist erlaubt) | R-07 |
| ANF-BEW-07 | Die maximale Textlänge beträgt 500 Zeichen | R-08, R-09 |
| ANF-BEW-08 | Die minimale Textlänge beträgt 0 Zeichen (optional, keine Mindestlänge) | R-07 |
| ANF-BEW-09 | Nach dem Absenden erscheint die Bewertung sofort in der Liste oben | R-01 |
| ANF-BEW-10 | Der Durchschnitt und die Anzahl der Bewertungen werden neu berechnet | R-01, R-03 |
| ANF-BEW-11 | Bewertungen werden anonym angezeigt: Der Name wird durch "Kunde" ersetzt | R-10, R-10b, R-11 |

### Bekannte Abweichungen (Bugs aus der Testdurchführung)

| Bug # | Beschreibung | Betroffene Anforderung |
|-------|--------------|------------------------|
| #001 | 500 Zeichen werden abgelehnt, 0 Sterne werden akzeptiert | ANF-BEW-05, ANF-BEW-07 |
| #002 | Keine Zeichenlimit-Prüfung beim Bearbeiten | ANF-BEW-07 |
| #003 | Cancel-Button ohne Funktion | ANF-BEW-xx (implizite UX) |
| #005 | Keine Anonymisierung (Name wird nicht durch "Kunde" ersetzt) | ANF-BEW-11 |
| #008 | Berechtigungsleck – Bewertung pro Produkt gesperrt | ANF-BEW-02, ANF-BEW-03 |

---

## Feature 2: Altersverifikation für alkoholische Produkte

**Ursprünglich vage formulierte Anforderung:**  
> Alkoholische Produkte erfordern eine Altersverifikation. Beim Aufrufen der Kategorie soll ein Fenster erscheinen, in dem Nutzer ihr Alter angeben müssen (18+), bevor sie Zugriff erhalten.

### Fragen zur Präzisierung (abgeleitet aus IST-Zustand des Webshops)

| Frage | Antwort (basierend auf IST-Zustand + sinnvoller SOLL-Ergänzung) |
|-------|----------------------------------------------------------------|
| 1. Gilt die Prüfung für eingeloggte und nicht eingeloggte Nutzer? | Nur für eingeloggte Nutzer; nicht eingeloggte sehen die Kategorie gar nicht |
| 2. Welches Format für das Geburtsdatum? | Format: TT-MM-JJJJ mit Fehlermeldungen bei ungültigem Format |
| 3. Was passiert bei ungültigem Datum (z. B. 31.02.2000)? | Fehlermeldung: „Ungültiges Datum. Bitte im Format TT-MM-JJJJ eingeben“ |
| 4. Wird das Alter einmalig gespeichert oder bei jedem Besuch neu abgefragt? | Einmalige Speicherung im Benutzerprofil (dauerhaft) – **noch nicht implementiert** |
| 5. Welche Zeitzone/Systemzeit wird für Altersberechnung verwendet? | Serverzeit (UTC) |
| 6. Schützt die Prüfung nur die Kategorie oder auch einzelne Produktseiten / direkte URLs? | Sollte alle Zugriffe schützen – **noch nicht vollständig implementiert** |
| 7. Kann das eingegebene Geburtsdatum nachträglich geändert werden? | Ja, soll im Profil änderbar sein – **noch nicht implementiert** |
| 8. Welche Meldung erscheint bei Alter < 18? | „Sie sind unter 18. Sie können keine alkoholischen Produkte sehen.“ |
| 9. Lässt sich das Pop-up durch Schließen umgehen (z. B. ESC, Click-Outside)? | Nein, Modal kann nicht umgangen werden |

### Detaillierte Anforderungen (testbar – SOLL-Zustand)

| ID | Anforderung | Abgedeckt durch Testfall |
|----|-------------|--------------------------|
| ANF-ALT-01 | Nicht eingeloggte Nutzer erhalten keinen Zugriff auf alkoholische Produkte | A-03 |
| ANF-ALT-02 | Eingeloggte Nutzer müssen einmalig ihr Geburtsdatum angeben | A-01, A-02 |
| ANF-ALT-03 | Bei Alter ≥ 18: Freigabe für alkoholische Produkte | A-01 |
| ANF-ALT-04 | Bei Alter < 18: Kategorie gesperrt, Hinweismeldung | A-02 |
| ANF-ALT-05 | Das Modal kann nicht durch ESC oder Click-Outside umgangen werden | A-05 |
| ANF-ALT-06 | Geburtsdatum muss im Format TT-MM-JJJJ eingegeben werden | A-06 |
| ANF-ALT-07 | Geburtsdatum ist ein Pflichtfeld | A-08 |
| ANF-ALT-08 | Die Prüfung gilt für Kategorie, Detailseiten und direkte URLs | A-04 |

### Bekannte Abweichungen (Bugs aus der Testdurchführung)

| Bug # | Beschreibung | Betroffene Anforderung |
|-------|--------------|------------------------|
| #006 | Alkohol-Zugriff nach Ausloggen möglich (Cache-Problem) | ANF-ALT-02 |
| #007 | Direkter URL-Zugriff ohne Altersprüfung möglich | ANF-ALT-08 |
| #010 | Session bleibt, Altersprüfung muss wiederholt werden | ANF-ALT-02 |
| #012 | Keine rechtssichere Altersprüfung (nur Geburtsdatums-Eingabe) | ANF-ALT-02 |
| #015 | Geburtsdatum nicht änderbar | ANF-ALT-02 |
| #016 | Kein Benutzerprofil (DSGVO) | ANF-ALT-02 |
| #021 | Buchstaben/Sonderzeichen im Geburtsdatum erlaubt | ANF-ALT-06 |

---

## Feature 3: Versandkosten

**Ursprünglich vage formulierte Anforderung:**  
> Versandkosten entfallen ab einem bestimmten Bestellwert. Darunter fallen Versandkosten an.

### Fragen zur Präzisierung (basierend auf IST-Zustand des Webshops)

| Frage | Antwort (basierend auf IST-Zustand) |
|-------|-------------------------------------|
| 1. Ab welchem Bestellwert genau entfallen die Versandkosten? | **Versandkostenfrei ab 20,00 €** (IST-Wert, abweichend von ursprünglicher Planung) |
| 2. Wie hoch sind die Versandkosten unter diesem Wert? | **Standardversand: 5,00 €** (IST-Wert) |
| 3. Gibt es verschiedene Versandarten (Standard, Express)? | Derzeit nur Standardversand implementiert; Express ist geplant (9,99 €) |
| 4. Zählen Versandkosten selbst zum Mindestbestellwert? | Nein, Versandkosten zählen nicht zum Mindestbestellwert |
| 5. Wird der Bestellwert vor oder nach Rabattcodes berechnet? | Nach Rabattcodes (noch nicht implementiert – in Klärung) |
| 6. Gelten unterschiedliche Versandkosten für gekühlte/alkoholische Produkte? | Alkohol: kein Express (geplant, noch nicht implementiert) |
| 7. Was passiert bei gemischten Warenkörben? | Höchste Versandkostenstufe gilt (geplant, noch nicht implementiert) |
| 8. Welche Währung? Wie wird gerundet? | Euro (€), kaufmännisch auf 2 Dezimalstellen |
| 9. Gilt Versandkostenfreiheit auch für Expressversand? | Nein, nur für Standardversand (Express geplant) |
| 10. Wird ins Ausland versendet? | Nein, nur innerhalb Deutschlands |

### Detaillierte Anforderungen (testbar – IST-Zustand)

| ID | Anforderung | Abgedeckt durch Testfall |
|----|-------------|--------------------------|
| ANF-VER-01 | Standardversand kostet 5,00 € | V-02 |
| ANF-VER-02 | Versandkostenfrei bei Warenkorbwert ≥ 20,00 € | V-01, V-03 |
| ANF-VER-03 | Versandkosten werden nicht auf Mindestbestellwert angerechnet | V-08 |
| ANF-VER-04 | Währung: Euro, Rundung kaufmännisch auf 2 Stellen | (implizit) |
| ANF-VER-05 | Kein Versand ins Ausland | (implizit) |

### Noch in Klärung / Nicht implementiert (zukünftige Features)

| Punkt | Status | Betroffene Testfälle (geplant) |
|-------|--------|-------------------------------|
| Expressversand (9,99 €) | ❌ Nicht implementiert | V-04, V-05, V-06 |
| Rabattcodes reduzieren Warenkorbwert vor Versandberechnung | ❌ Nicht implementiert | V-07 |
| Alkoholische Produkte: kein Expressversand | ❌ Nicht implementiert | V-04 |
| Gemischter Warenkorb: Höchste Versandkostenstufe | ❌ Nicht implementiert | V-05, V-06 |

### Bekannte Abweichungen (Bugs aus der Testdurchführung)

| Bug # | Beschreibung | Betroffene Anforderung |
|-------|--------------|------------------------|
| #24 | Versandaktualisierung fehlerhaft (nach Entfernen/Reduzieren bleibt Versand kostenlos) | ANF-VER-02 |

---

## Zusammenfassung der gewonnenen Informationen

| Feature | Anzahl Fragen | Abweichungen (Bugs) | Offene Punkte (Nice-to-Have) |
|---------|--------------|---------------------|------------------------------|
| Bewertungssystem | 10 | 6 | 2 (#31, #32) |
| Altersverifikation | 9 | 7 | – |
| Versandkosten | 10 | 1 | 4 (Express, Rabatt, gemischter WK) |

**Erkenntnisse aus der IST-Zustands-Analyse:**

1. Der Webshop weicht in mehreren Punkten von branchenüblichen Best Practices ab (keine Anonymisierung, fehlende Validierung).
2. Kritische Sicherheits- und DSGVO-relevante Mängel wurden identifiziert (#5, #16, #17, #23).
3. Die Versandkostenregelung ist mit 20€/5€ einfacher als ursprünglich angenommen – aber fehlerhaft in der Aktualisierung (#24).
4. Viele geplante Features (Expressversand, Rabattintegration, gemischte Warenkörbe) sind noch nicht umgesetzt.

**Nächste Schritte (bereits durchgeführt):**
- ✅ Testfallentwurf auf Basis der präzisierten Anforderungen
- ✅ Testdurchführung mit Dokumentation aller Abweichungen (Bugs)
- ✅ Testberichterstattung mit 30+ Issues
