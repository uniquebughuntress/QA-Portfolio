# Testberichterstattung (Test Reporting) – Market Mate

**Berichtszeitraum:** 01.06.2026 – 05.06.2026  
**Tester:** Natalya Weiß  
**Version:** 1.0 (Final)

---

## 1. Zusammenfassung

| Kennzahl | Wert |
|----------|------|
| **Geplante Testfälle** | 28 |
| **Ausgeführte Testfälle** | 28 (100%) |
| **Bestandene Tests** | 13 (46,4%) |
| **Fehlgeschlagene Tests** | 15 (53,6%) |
| **Gefundene Bugs** | 30 |
| **Dokumentierte Issues** | 28 (#3–#30) |
| **Blocker (während Testdurchführung)** | 7 |

---

## 2. Testabdeckung nach Feature

| Feature | Testfälle | Bestanden | Fehlgeschlagen | Bestandsquote |
|---------|-----------|-----------|----------------|---------------|
| Bewertungssystem | 14 | 8 | 6 | 57,1% |
| Altersverifikation | 8 | 2 | 6 | 25,0% |
| Versandkosten | 6 | 3 | 3 | 50,0% |
| **Gesamt** | **28** | **13** | **15** | **46,4%** |

---

## 3. Bug-Zusammenfassung nach Priorität

| Priorität | Anzahl | Beispiele |
|-----------|--------|-----------|
| 🔴 **Critical** | 10 | #004 (Exponentialdarstellung), #006 (Alkohol nach Logout), #010 (direkter URL), #015 (kein Profil), #016 (kein Impressum), #023 (Injection), #024 (Versandausnutzung) |
| 🟠 **Medium** | 10 | #001 (500 Zeichen), #005 (Anonymisierung), #008 (Berechtigungsleck), #021 (Geburtsdatum-Validierung) |
| 🟡 **Low** | 10 | #003 (Cancel-Button), #011 (Tippfehler), #017–#020 (Favoriten/UX), #026–#030 (Mobile) |

---

## 4. Bugs nach Feature

| Feature | Critical | Medium | Low | Gesamt |
|---------|----------|--------|-----|--------|
| Bewertungssystem | 0 | 3 | 2 | 5 |
| Altersverifikation | 4 | 2 | 0 | 6 |
| Versandkosten | 1 | 0 | 0 | 1 |
| Warenkorb / Bestellung | 1 | 1 | 0 | 2 |
| Session / Sicherheit | 2 | 1 | 0 | 3 |
| DSGVO / Rechtlich | 2 | 1 | 0 | 3 |
| Favoriten | 0 | 0 | 3 | 3 |
| Mobile / Kosmetik | 0 | 0 | 5 | 5 |
| Login / Benutzerkonto | 0 | 2 | 0 | 2 |
| **Gesamt** | **10** | **10** | **10** | **30** |

---

## 5. Top 5 Kritische Bugs (Showstopper)

| # | Titel | Risiko |
|---|-------|--------|
| **#004** | Exponentialdarstellung – keine Stückzahlbegrenzung | Wirtschaftlicher Schaden (Millionenbestellungen) |
| **#006, #007, #010** | Alkohol-Zugriff nach Logout / direkter URL / Session bleibt | Umgehung Jugendschutz + Sicherheit |
| **#015, #016** | Kein Benutzerprofil / Kein Impressum / Keine Datenschutzerklärung | DSGVO (Bußgeld bis 20 Mio. €) + Abmahnung |
| **#023** | Keine Sanitization – Injection-Angriffe möglich | XSS, SQL-Injection – System kompromittierbar |
| **#024** | Versandaktualisierung fehlerhaft (finanzielle Ausnutzung) | Verlust von 5€ pro Bestellung bei Ausnutzung |

---

## 5b. Blocker während der Testdurchführung

Folgende Blocker haben die Testdurchführung behindert oder verzögert:

| ID | Blocker | Auswirkung | Lösung / Workaround | Status |
|----|---------|------------|---------------------|--------|
| **B-01** | Kein Benutzerprofil vorhanden (#016) | Testfälle zur Profiländerung (z.B. Geburtsdatum ändern) konnten nicht vollständig ausgeführt werden | Workaround: Browser-Tab/Browser schließen und neu öffnen (#015) | ⚠️ Workaround vorhanden |
| **B-02** | Session bleibt nach Browser-Schließen erhalten (#012, #027) | Tests mit neuen Logins erforderten manuelles Löschen von Cache/Cookies | Umgebung vor jedem Test zurücksetzen | ⚠️ Behoben durch Workaround |
| **B-03** | Keine Testdaten für gekaufte Produkte | Testfälle für Bewertungen (R-01 bis R-03) benötigten gekaufte Produkte | Eigene Testnutzer mit Bestellhistorie erstellt (test1@test.de) | ✅ Gelöst |
| **B-04** | Mobile Ansicht (Android 16) – Category-Leiste nicht versteckbar (#028) | Tests der mobilen Shop-Ansicht waren erschwert | Sehr langes Scrollen erforderlich | ⚠️ Workaround vorhanden |
| **B-05** | Keine Möglichkeit, Passwort während der Eingabe sichtbar zu schalten (#025) | Erstellung mehrerer Testnutzer war fehleranfällig (Vertipper) | Passwörter in externem Dokument notiert | ⚠️ Workaround vorhanden |
| **B-06** | Favoriten-Seite bleibt nach langer Session ausgegraut (#027) | Tests der Favoriten-Funktion nach 24h nicht möglich | Aus- und wieder einloggen als Workaround | ⚠️ Workaround vorhanden |
| **B-07** | Keine Bestellhistorie (#014) | Testfälle für "nur gekaufte Produkte bewerten" waren schwer validierbar | Manuelles Merken der Bestellungen notwendig | ⚠️ Workaround vorhanden |

### Zusammenfassung der Blocker

| Kategorie | Anzahl |
|-----------|--------|
| Kritische Blocker (Testausführung stark behindert) | 2 (#016, #012) |
| Mittlere Blocker (Workaround möglich) | 4 (#014, #025, #027, #028) |
| Geringe Blocker (kosmetisch) | 1 (#015) |

**Fazit zu den Blockern:**  
Die Testdurchführung war durch die fehlende Profil- und Session-Funktionalität erheblich erschwert. In einer professionellen Testumgebung wären diese Blocker **vorab** zu beheben gewesen. Für das Bootcamp wurden Workarounds eingesetzt, um die Testfälle dennoch ausführen zu können.

---

## 6. Empfehlung an den Product Owner

> **Der Webshop kann in der aktuellen Form nicht live gehen.**

Die Testdurchführung hat **10 kritische Mängel** aufgedeckt, darunter:
- **Sicherheitslücken** (#004, #006, #007, #010, #023)
- **DSGVO-Verstöße** (#015, #016)
- **Finanzielle Verlustrisiken** (#024)

**Vor einem Go-Live müssen folgende Punkte zwingend behoben werden:**
1. DSGVO-konformes Benutzerprofil mit Impressum und Datenschutzerklärung (#015, #016)
2. Altersverifikation gegen direkte URLs und Session-Probleme absichern (#006, #007, #010)
3. Eingabevalidierung und Sanitization gegen Injection-Angriffe (#023)
4. Versandkostenaktualisierung korrigieren (#024)
5. Stückzahlbegrenzung im Warenkorb einführen (#004)

**Nach Behebung dieser Punkte wird ein vollständiger Regressionstest empfohlen.**

---

## 7. Verbesserungsvorschläge (Nice-to-Have)

| # | Vorschlag | Nutzen |
|---|-----------|--------|
| #31 | Zeitstempel bei Bewertungen anzeigen | Höhere Glaubwürdigkeit |
| #32 | Bewertungen filter- und sortierbar machen | Bessere UX |

---

## 8. Testartefakte

| Artefakt | Ort |
|----------|-----|
| Anforderungsanalyse_v2 | `/anforderungen/Anforderungsanalyse_v2.md` |
| Testplan_v2 | `/testplan/Testplan_v2.md` |
| Testfallentwurf_v2 | `/testfallentwurf/Testfallentwurf_v2.md` |
| Testdurchführungsdokumentation | `/testdurchfuehrung/Testdurchfuehrungsdokumentation.md` |
| Issues (Bugs) | https://github.com/uniquebughuntress/portfolio/issues (#3–#30) |

---

## 9. Fazit

Die Qualität des Webshops ist **nicht ausreichend** für eine Produktivfreigabe. Die hohe Anzahl kritischer Bugs (insbesondere im Bereich Sicherheit, Datenschutz und finanzielle Logik) erfordert eine umfassende Überarbeitung.

**Nächste Schritte:**
1. PO-Entscheidung zu den kritischen Bugs einholen
2. Entwickler-Team mit der Behebung beauftragen
3. Nach Behebung: Vollständigen Regressionstest durchführen

---

## Versionshistorie

| Version | Datum | Änderungen |
|---------|-------|------------|
| **1.0** | **2026-06-05** | **Finale Version nach vollständiger Testdurchführung mit 30 Bugs, 7 Blockern und Handlungsempfehlung** |
