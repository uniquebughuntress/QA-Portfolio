# Testplan – Market Mate (Neue Funktionen)

## 1. Produktanalyse

**Zielsetzung**
Das Ziel des Produkts ist die Erweiterung des bestehenden Online-Supermarkets "Market Mate" um drei Kernfunktionen, um das Einkaufserlebnis zu verbessern und gesetzliche Anforderungen (Altersverifikation) zu erfüllen:
1. **Bewertungssystem für Produkte** (5-Sterne + Text)
2. **Altersverifikation für alkoholische Produkte** (18+)
3. **Dynamische Versandkostenregelung** (kostenfrei ab 50€)

**Zielnutzergruppe**
- **Primär:** Registrierte Endkunden (Privatpersonen) ab 18 Jahren
- **Sekundär:** Gastnutzer (eingeschränkter Zugriff auf Alkohol)
- **Administratoren:** Zur Moderation von Bewertungen

**Hardware- und Software-Spezifikationen**
- **Hardwareanforderungen:**
  - Geräte: PCs, Laptops, Smartphones, Tablets
  - Spezifikationen: Standardkonfigurationen für Android/iOS; Desktops mit 4 GB RAM, 2 GHz Prozessor
- **Softwareanforderungen:**
  - Betriebssysteme: Windows, macOS, Android, iOS
  - Browser: Chrome (aktuell), Firefox (aktuell), Safari (aktuell), Edge (aktuell)
  - Abhängigkeiten: Backend-Dienste, Zahlungsschnittstelle, Session/Cookie-Management

**Funktionalität des Produkts**
**Bestehende Funktionen (Regression relevant):**
- Registrierung und Login
- Produktsuche mit Sortierung, Kategorisierung
- Favoritenliste
- Warenkorb
- Bestellabschluss (Adressen, Zahlung, Preisberechnung)

**Neue Funktionen (Testfokus):**
- Bewertungssystem (Sterne, Text, Bearbeiten/Löschen, Durchschnittsberechnung)
- Altersverifikation (Geburtsdatumserfassung, Zugriffskontrolle für Alkohol)
- Versandkostenlogik (Standard/Express, Freibetrag 50€, Alkohol-Express-Sperre)

---

## 2. Teststrategie entwerfen

**Testumfang (Scope of Testing)**

**Im Umfang enthalten:**
- Bewertung abgeben (nur eingeloggte, nur gekaufte Produkte, 1x pro Produkt)
- Bewertung bearbeiten/löschen
- Anzeige der Durchschnittsbewertung (kaufmännisch gerundet auf 1 Dezimalstelle)
- Meldefunktion für unangemessene Bewertungen
- Altersverifikation (Erfassung Geburtsdatum, Zugriff auf Alkohol-Kategorie/-Detailseiten)
- Schutz vor Umgehung (ESC, Click-Outside, direkte URLs)
- Versandkostenberechnung (Standard 4,99€ / Express 9,99€)
- Versandkostenfreiheit ab 50€ (nach Rabatt, nur Standard)
- Express-Sperre für alkoholische Produkte
- Gemischte Warenkörbe (höchste Versandstufe)
- Regression: Login, Warenkorb, Bestellprozess

**Nicht im Umfang enthalten:**
- Backend-Datenbankoperationen ohne UI-Einfluss (direkte SQL-Tests)
- Integration externer Zahlungsdienstleister (Mock-Umgebung)
- Versand ins Ausland (nicht unterstützt)
- Mobile native Apps (nur responsive Web)
- Admin-Backend für Bewertungsmoderation (UI außerhalb des Scopes)

**Geplante Testarten**
- **Funktionstests:** Alle neuen Features gemäß Anforderungen
- **Regressions-Tests:** Sicherstellen, dass bestehende Features nicht brechen
- **Sicherheitstests:** Direkte URL-Zugriffe auf Alkohol-Produkte ohne Verifikation
- **Usability-Tests:** Altersverifikations-Modal nicht umgehbar, intuitive Bewertungsabgabe
- **Grenzwerttests:** Versandkostenfreigrenze (50,00€), Altersgrenze (18 Jahre), Textlängen (10-500 Zeichen)

**Risiken und Gegenmaßnahmen**
- **Entwicklungsverzögerungen** → Zeitpuffer von 3 Tagen einplanen
- **Fehlende Testdaten** → Mock-Daten für Produkte, Bestellungen, Bewertungen erstellen
- **Ressourcenengpässe** → Cross-Schulung des QA-Teams
- **Umgehung der Altersprüfung** → Zusätzliche Sicherheitstests mit direkten URLs

**Testlogistik (Testverantwortlichkeiten)**
- **Testmanager:** Jane Smith
- **QA Engineer (Funktion & Regression):** John Doe
- **QA Engineer (Sicherheit & Grenzwerte):** Alice Johnson
- **QA Engineer (Usability):** Robert Brown
- **Endanwender für UAT:** 3 registrierte Nutzer (18+ und <18)

---

## 3. Testziele definieren

**Ziele**
- **Funktionalität:** Alle neuen Features arbeiten gemäß der präzisierten Anforderungen
- **Sicherheit:** Altersverifikation ist nicht durch direkte URLs, ESC oder Click-Outside umgehbar
- **Datenintegrität:** Keine Mehrfachbewertungen, Bewertungen werden bei Produktlöschung entfernt
- **Grenzwertgenauigkeit:** Versandkostenfreiheit ab 50,00€, Altersprüfung bei 18 Jahren
- **Benutzbarkeit:** Modal zwingend ausfüllbar, Bewertungsinterface intuitiv

**Erwartete Ergebnisse**
- 100% der Sicherheitstests für Altersverifikation bestehen
- Bewertungen können nur von berechtigten Nutzern abgegeben werden
- Versandkosten entsprechen der definierten Logik (auch bei gemischten Warenkörben)
- Alle Regressionstests für bestehende Funktionen bestehen

---

## 4. Testkriterien definieren

**Aussetzungskriterien (Suspension Criteria)**
- Kritischer Sicherheitsfehler (Altersumgehung möglich) – sofortiger Stop
- Ausfall der Testumgebung oder fehlende Testdaten
- Blockierender Fehler im Login (Voraussetzung für alle Tests)

**Abnahmekriterien (Exit Criteria)**
- 100% aller geplanten Testfälle wurden ausgeführt
- **Ausführungsrate:** 100% (keine übersprungenen Tests ohne Begründung)
- **Bestehensquote:** Mindestens 95% der ausgeführten Testfälle bestanden
- Alle kritischen und hochpriorisierten Defekte (Severity 1 & 2) sind geschlossen
- Keine offenen Sicherheitslücken bei Altersverifikation
- Grenzwerttests (50€, 18 Jahre) bestanden
- UAT (User Acceptance Test) mit 3 Endnutzern abgeschlossen und freigegeben

---

## 5. Ressourcenplanung

- **Personelle Ressourcen:** 1 Testmanager, 3 QA Engineers, 1 Entwickler (Support), 3 UAT-Tester
- **Hardware:** 3 Desktops (Win/Mac), 2 Smartphones (Android/iOS), 2 Tablets
- **Software:** Chrome DevTools, BrowserStack (für Cross-Browser), JIRA (Defect Tracking), TestRail (Testfallverwaltung), Selenium (Automatisierung)
- **Infrastruktur:** Separate TEST-Umgebung mit Mock-Zahlungsdienst

---

## 6. Testumgebung planen

- **Testgeräte:** Reale Endgeräte + BrowserStack für Cross-Browser-Tests
- **Umgebungen:**
  - **DEV:** Entwickler-Unittests
  - **TEST:** QA-Hauptumgebung für Systemtests
  - **ACC:** UAT mit echten Nutzerdaten (Mock-Produkte)
  - **PROD:** Nur nach Freigabe

**Konfigurationen:**
- Browser: Chrome 120+, Firefox 115+, Safari 16+, Edge 120+
- Betriebssysteme: Windows 11, macOS Sonoma, Android 13, iOS 16
- Netzwerk: Simulierte langsame Verbindungen (3G) für Altersprüfung

---

## 7. Zeitplan und Aufwandsschätzung

| Aktivität | Startdatum | Enddatum | Umgebung | Verantwortlich | Geplanter Aufwand |
| --- | --- | --- | --- | --- | --- |
| Testplanung | 01.06.2025 | 03.06.2025 | Alle | Testmanager | 16 Stunden |
| Testfalldesign | 04.06.2025 | 08.06.2025 | Alle | QA-Team | 40 Stunden |
| Unittest (Entwickler) | 09.06.2025 | 13.06.2025 | DEV | Entwickler | 40 Stunden |
| Systemtest Bewertungen | 14.06.2025 | 17.06.2025 | TEST | QA (John) | 24 Stunden |
| Systemtest Altersverifikation | 14.06.2025 | 17.06.2025 | TEST | QA (Alice) | 24 Stunden |
| Systemtest Versandkosten | 18.06.2025 | 20.06.2025 | TEST | QA (John) | 20 Stunden |
| Regressionstest | 21.06.2025 | 23.06.2025 | TEST | QA (John) | 24 Stunden |
| Sicherheitstest (Alkohol) | 21.06.2025 | 22.06.2025 | TEST | QA (Alice) | 12 Stunden |
| Grenzwerttests | 23.06.2025 | 24.06.2025 | TEST | QA (Alice) | 12 Stunden |
| Usability-Test | 24.06.2025 | 25.06.2025 | TEST | QA (Robert) | 10 Stunden |
| Abnahmetest (UAT) | 26.06.2025 | 29.06.2025 | ACC | Endanwender | 20 Stunden |
| Fehlerbehebung | 30.06.2025 | 02.07.2025 | TEST | Entwickler | 20 Stunden |
| Produktivfreigabe | 03.07.2025 | 03.07.2025 | PROD | DevOps | 4 Stunden |

**Gesamtaufwand QA:** ca. 200 Stunden

---

## 8. Testartefakte (Test-Deliverables)

Folgende Dokumente und Werkzeuge werden erstellt und bereitgestellt:

- **Testplandokument** (diese Datei)
- **Testfälle und Testskripte** (manuell + automatisiert) – siehe `Testfallentwurf.md`
- **Testdaten** (CSV/JSON mit Produkten, Bestellungen, Nutzern)
- **Testberichte** (täglich, Endbericht nach jeder Phase)
- **Fehlerberichte** (in JIRA mit Severity, Steps, Screenshots)
- **UAT-Freigabedokumentation** (Sign-off der Endanwender)
- **Sicherheitsaudit** (Altersverifikation – Bestätigung keine Umgehung)
