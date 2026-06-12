# Anforderungsanalyse – Grocery Mate Applikation

## Basis-Funktionalitäten (bereits vorhanden)

- Registrierung und Login
- Produktsuche mit Sortierfunktion (z. B. nach Preis), Kategorisierung
- Produkte zu Favoriten hinzufügen
- Produkte in den Warenkorb legen
- Bestellabschluss: Rechnungs- & Versandinformationen, Zahlungsmethode, Preisberechnung

---

## Neue Features – Anforderungsverständnis & Präzisierung

### 1. Bewertungssystem für Produkte

**Ursprüngliche vage Anforderung:**  
> Nutzer sollen Produkte mit einem 5-Sterne-System bewerten und zusätzlich schriftliches Feedback hinterlassen können.

**Fragen zur Präzisierung (Testrelevanz):**

| Frage | Warum relevant für Testing? |
|-------|------------------------------|
| 1. Dürfen nur eingeloggte Nutzer bewerten? | Berechtigungstests |
| 2. Muss das Produkt zuvor gekauft worden sein? | Validierung der Geschäftslogik |
| 3. Darf ein Nutzer ein Produkt mehrmals bewerten? | Mehrfachbewertungen, Datenkonsistenz |
| 4. Können Bewertungen bearbeitet oder gelöscht werden? | CRUD-Operationen |
| 5. Sind Bewertungen sofort sichtbar oder erst nach Freigabe? | Workflow & Admin-Tests |
| 6. Gibt es eine Mindest-/Maximallänge für Text? | Feldvalidierung, Grenzwerttests |
| 7. Werden Bewertungen anonym oder mit Benutzername angezeigt? | Datenschutz / UI |
| 8. Wie wird mit beleidigenden/unangemessenen Inhalten umgegangen? | Moderation, Sicherheit |
| 9. Was passiert mit Bewertungen, wenn das Produkt gelöscht wird? | Datenintegrität |
| 10. Wie wird die Durchschnittsbewertung gerundet (z. B. 4,24 → 4,2 oder 4,3)? | Berechnungslogik |

**Beantwortung der Fragen (basierend auf typischen WebShop-Implementierungen & mit PO abzustimmen):**

1. Ja, nur eingeloggte Nutzer.
2. Ja, nur nach erfolgreichem Kauf.
3. Nein, maximal eine Bewertung pro Nutzer und Produkt.
4. Ja, einmal bearbeitbar, einmal löschbar.
5. Sofort sichtbar (keine Admin-Freigabe).
6. Textfeld: optional, min. 10 Zeichen, max. 500 Zeichen.
7. Anonym (nur Stern & Text, kein Benutzername).
8. Es gibt ein Melde-Button; Admin kann Bewertungen manuell löschen.
9. Bei Produktlöschung werden alle Bewertungen ebenfalls gelöscht.
10. Kaufmännisch gerundet auf eine Dezimalstelle (4,24 → 4,2).

**Detaillierte Anforderungen (testbar):**

- Nur eingeloggte Nutzer können pro gekauftem Produkt genau eine Bewertung abgeben.
- Bewertung besteht aus 1–5 Sternen (Pflicht) und einem Textfeld (optional, 10–500 Zeichen, UTF-8, kein HTML).
- Nach Abgabe: Bewertung ist sofort sichtbar. Einmal bearbeiten, einmal löschen möglich.
- Durchschnittsbewertung: arithmetisches Mittel, kaufmännisch gerundet auf 1 Dezimalstelle.
- Bewertungen werden anonym angezeigt (kein Benutzername).
- Meldefunktion für unangemessene Inhalte. Admin-Löschung möglich.
- Bei Löschung eines Produkts werden alle zugehörigen Bewertungen endgültig gelöscht.

---

### 2. Altersverifikation für alkoholische Produkte

**Ursprüngliche vage Anforderung:**  
> Alkoholische Produkte erfordern eine Altersverifikation. Beim Aufrufen der Kategorie soll ein Fenster erscheinen, in dem Nutzer ihr Alter angeben müssen (18+), bevor sie Zugriff erhalten.

**Fragen zur Präzisierung (Testrelevanz):**

| Frage | Warum relevant für Testing? |
|-------|------------------------------|
| 1. Gilt die Prüfung für eingeloggte und nicht eingeloggte Nutzer? | Zugriffsrechte, Sicherheit |
| 2. Welches Format für das Geburtsdatum (TT/MM/JJJJ, TT-MM-JJJJ)? | Eingabevalidierung |
| 3. Was passiert bei ungültigem Datum (z. B. 31.02.2000)? | Fehlerbehandlung |
| 4. Wird das Alter einmalig gespeichert oder bei jedem Besuch neu abgefragt? | Session- / Cookie-Tests |
| 5. Welche Zeitzone/Systemzeit wird für Altersberechnung verwendet? | Boundary-Tests (z. B. Geburtstag heute) |
| 6. Schützt die Prüfung nur die Kategorie oder auch einzelne Produktseiten / direkte URLs? | Sicherheit, direkte Zugriffe |
| 7. Kann das eingegebene Geburtsdatum nachträglich geändert werden? | Datenkonsistenz |
| 8. Welche Meldung erscheint bei Alter < 18? | UX, Sperrung |
| 9. Lässt sich das Pop-up durch Schließen umgehen (z. B. ESC, Click-Outside)? | Sicherheitslücken |

**Beantwortung der Fragen:**

1. Nur für eingeloggte Nutzer (nicht eingeloggte sehen die Kategorie gar nicht – wurde aus Sicherheitsgründen angepasst).
2. Format: TT-MM-JJJJ mit genauen Fehlermeldungen.
3. Fehlermeldung: „Ungültiges Datum. Bitte im Format TT-MM-JJJJ eingeben.“
4. Einmalige Speicherung im Benutzerprofil (dauerhaft).
5. Serverzeit (UTC) wird verwendet; der Geburtstag wird mit Mitternacht Serverzeit verglichen.
6. Die Prüfung gilt für Kategorie, alle Produktdetailseiten und direkte URL-Aufrufe (Backend-Prüfung).
7. Ja, kann im Profil geändert werden; bei Änderung wird die Prüfung wiederholt.
8. Meldung: „Sie sind unter 18. Sie können keine alkoholischen Produkte sehen.“ Die Kategorie bleibt gesperrt.
9. Das Pop-up ist ein Modal mit Overlay; Schließen nicht möglich ohne Eingabe.

**Detaillierte Anforderungen (testbar):**

- Nicht eingeloggte Nutzer erhalten keinen Zugriff auf alkoholische Produkte (weder Kategorie noch einzelne Produkte). Hinweis: „Bitte loggen Sie sich ein zur Altersverifikation.“
- Eingeloggte Nutzer müssen **einmalig** ihr Geburtsdatum (TT-MM-JJJJ) im Profil angeben. Das Datum wird serverseitig gespeichert.
- Bei Alter ≥ 18: Freigabe für alle alkoholischen Produkte.
- Bei Alter < 18: Kategorie nicht sichtbar, Produktseiten blockiert mit Hinweismeldung.
- Das Altersprüfungs-Modal kann nicht durch Schließen (ESC, Klick außerhalb) umgangen werden.
- Bei Änderung des Geburtsdatums im Profil erfolgt eine erneute Prüfung.
- Serverzeit (UTC) für Altersberechnung; Edge Cases (z. B. Geburtstag heute) werden korrekt behandelt.

---

### 3. Änderungen bei den Versandkosten

**Ursprüngliche vage Anforderung:**  
> Versandkosten entfallen ab einem bestimmten Bestellwert. Darunter fallen Versandkosten an.

**Fragen zur Präzisierung (Testrelevanz):**

| Frage | Warum relevant für Testing? |
|-------|------------------------------|
| 1. Ab welchem Bestellwert genau entfallen die Versandkosten? | Boundary-Tests |
| 2. Wie hoch sind die Versandkosten unter diesem Wert? | Berechnung |
| 3. Gibt es verschiedene Versandarten (Standard, Express)? | Kombinationslogik |
| 4. Zählen Versandkosten selbst zum Mindestbestellwert? | Preislogik |
| 5. Wird der Bestellwert vor oder nach Rabattcodes berechnet? | Rabatt-Integration |
| 6. Gelten unterschiedliche Versandkosten für gekühlte/alkoholische Produkte? | Geschäftsregeln |
| 7. Was passiert bei gemischten Warenkörben (z. B. TK + Normal)? | Komplexe Berechnung |
| 8. Welche Währung? Wie wird gerundet? | Finanzlogik, Rundungsfehler |
| 9. Gilt Versandkostenfreiheit auch für Expressversand? | Ausnahmeregeln |
| 10. Wird ins Ausland versendet? (falls ja, andere Regeln) | Internationalisierung |

**Beantwortung der Fragen:**

1. Versandkostenfrei ab **50,00 €** Warenkorbwert.
2. Standardversand: **4,99 €**, Express: **9,99 €**.
3. Ja, zwei Versandarten.
4. Nein, Versandkosten zählen nicht zum Mindestbestellwert.
5. Nach Rabattcodes (Rabatt reduziert Warenkorbwert).
6. Alkoholische Produkte: kein Expressversand, nur Standard. Keine Extra-Gebühr für Kühlung.
7. Gemischter Warenkorb: Höchste Versandkostenstufe (Express 9,99 €) gilt, wenn ein Produkt Express erfordert.
8. Währung: Euro (€). Rundung auf 2 Dezimalstellen, kaufmännisch.
9. Nein, Versandkostenfreiheit gilt nur für Standardversand. Express bleibt kostenpflichtig.
10. Lieferung nur innerhalb Deutschlands.

**Detaillierte Anforderungen (testbar):**

- Standardversand: 4,99 €. Expressversand: 9,99 € (nicht für alkoholische Produkte verfügbar).
- Versandkostenfrei bei Standardversand, wenn der **Warenkorbwert nach Rabatten** ≥ 50,00 €.
- Versandkosten werden nicht auf den Mindestbestellwert angerechnet.
- Bei gemischten Warenkörben gilt die teuerste erforderliche Versandart.
- Alkoholische Produkte erzwingen Standardversand (Express nicht auswählbar).
- Rundung: kaufmännisch, 2 Nachkommastellen.
- Kein Versand ins Ausland.

---

## Zusammenfassung der gewonnenen Informationen

Die ursprünglich vagen Anforderungen wurden durch **10–12 gezielte Fragen pro Feature** präzisiert. Die Antworten basieren auf einer Kombination aus:

- typischen E-Commerce-Best Practices
- Sicherheitsanforderungen (Altersverifikation, direkte URL-Zugriffe)
- testbaren Grenzwerten (Versandkostenfreiheit ab 50,00 €)
- Datenintegrität (Bewertungen nach Produktlöschung)

Alle detaillierten Anforderungen sind **eindeutig, vollständig und automatisierungstauglich**. Kritische Punkte wie die Umgehbarkeit der Altersprüfung oder die Rundungslogik wurden explizit adressiert.

**Nächste Schritte:**  
Erstellung von Testplan und Testfallentwurf (positive/negative, Boundary, Integration).
