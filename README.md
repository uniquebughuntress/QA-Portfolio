# 🐛 uniquebughuntress – QA Learning Portfolio

*„Bug hunting with structure and heart.“*

Willkommen in meinem öffentlichen Lernportfolio.  
Ich bin **uniquebughuntress** und dokumentiere hier meinen Weg durch das **Software Engineering Bootcamp** – mit vollem Fokus auf **Quality Assurance (QA)** und **Testautomatisierung**.

Ziel ist es, Theorie und Praxis zu verbinden:  
Von der Anforderungsanalyse über manuelle Testfälle bis hin zur automatisierten Testsuite mit Python, PyTest & Selenium.

---

## 📚 Lernplan (basierend auf Bootcamp & Udemy)

Die folgende Tabelle zeigt meinen Fortschritt durch die Kursinhalte.  
Erledigte Aufgaben sind verlinkt, kommende werden nach und nach ergänzt.

### TEIL 1 – GRUNDLAGEN DES TESTENS (STLC)

| Woche | Thema | Status | Hausaufgabe / Artefakt |
|-------|-------|--------|------------------------|
| 1.1 | Udemy Abschnitte 1–3 | ✅ | [Mock-up Test Session 1] – *folgt* |
| 1.2 | Udemy Abschnitt 4 | ✅ | [Mock-up Test Session 2] – *folgt* |
| 2.1 | Tests aus Sitzung 1 & 2 | ✅ | [Dokumentation der Tests] – *folgt* |
| 2.2 | Äquivalenzklassen & Grenzwertanalyse | ✅ | [Aufgabe EP & BVA](https://github.com/uniquebughuntress/QA-Portfolio/blob/main/STLC/%C3%84quivalenzklassen_und_Grenzwertanalyse.md) |
| 2.2 | Entscheidungstabellentest | ✅ | [Aufgabe Entscheidungstabelle](https://github.com/uniquebughuntress/QA-Portfolio/blob/main/STLC/Entscheidungstabellentest.md) |
| 3.1 | Zustandsübergangstest | ✅ | [Aufgabe Zustandsübergangstest](https://github.com/uniquebughuntress/QA-Portfolio/blob/main/STLC/Zustandsuebergangstest.md) |
| 3.2 | Anforderungen verstehen & präzisieren | ✅ | [Anforderungsanalyse Grocery Mate](https://github.com/uniquebughuntress/QA-Portfolio/blob/main/STLC/Anforderungsanalyse_v2.md) |
| 3.2 | Portfolio-Einrichtung | ✅ | Dieses Repository |
| 4.1 | Testplan & Testfallentwurf | ✅ | [Testplan](https://github.com/uniquebughuntress/QA-Portfolio/blob/main/STLC/Testplan_v2.md) und [Testfalldesign](https://github.com/uniquebughuntress/QA-Portfolio/blob/main/STLC/Testfallentwurf_Test-Case-Design_v2.md)|
| 4.2 | Testdurchführungsdokumentation & Testberichterstattung | ✅ | [Testdurchführung](https://github.com/uniquebughuntress/QA-Portfolio/blob/main/STLC/Testdurchführungsdokumentation.md) und [Testbericht](https://github.com/uniquebughuntress/QA-Portfolio/blob/main/STLC/Testberichterstattung_Test-Reporting.md)|

### TEIL 2 – TESTAUTOMATISIERUNG

| Woche | Thema | Status | Hausaufgabe / Artefakt |
|-------|-------|--------|------------------------|
| 5 | PyTest Grundlagen |  ✅ | [PyTest Übung](https://github.com/uniquebughuntress/QA-Portfolio/tree/main/Testautomatisierung/HW1_PyTest)|
| 6 | Selenium + PyTest | 🚧 |[Erste automatisierte Tests] – *in Arbeit* |
| 7 | XPath Strategien | ⏳ | [XPath Übungen] – *folgt* |
| 8 | **Projekt: Testautomatisierung** |⏳| [End-to-End Testsuite] – *folgt* |

> **Getestete Anwendung:** [Grocery Market Mate WebShop](https://grocerymate.masterschool.com/store)

---


## 📂 Repository-Struktur
```
uniquebughuntress-qa-portfolio/
│
├── .github/ # GitHub Issue Templates
│ └── ISSUE_TEMPLATE/
│ ├── bug_report.md # Bug-Ticket (Englisch/Markdown)
│ ├── bug_report.yml # Bug-Ticket (Englisch/YAML-Formular)
│ ├── config.yml # Keine leeren Issues erlaubt
│ ├── fehlerbericht.md # Bug-Ticket (Deutsch/Markdown)
│ ├── fehlerbericht.yml # Bug-Ticket (Deutsch/YAML-Formular)
│ ├── improvement.md # Verbesserungsvorschlag (Englisch/Markdown)
│ ├── improvement.yml # Verbesserungsvorschlag (Englisch/YAML)
│ ├── verbesserungsvorschlag.md # Verbesserungsvorschlag (Deutsch/Markdown)
│ └── verbesserungsvorschlag.yml # Verbesserungsvorschlag (Deutsch/YAML)
│
├── STLC/ # Software Testing Life Cycle Dokumentation
│ ├── Anforderungsanalyse.md # Ursprüngliche Anforderungen
│ ├── Anforderungsanalyse_v2.md # Anforderungen IST-Zustand + Nice-to-Have
│ ├── Einrichtung-Test-Umgebung.md # Testumgebung & Tools
│ ├── Entscheidungstabellentest.md # Decision Table Testing
│ ├── Testberichterstattung_Test-Reporting.md # Finaler Testbericht
│ ├── Testdurchführungsdokumentation.md # Test Execution Dokumentation
│ ├── Testfallentwurf_Test-Case-Design.md # Ursprünglicher Testfallentwurf
│ ├── Testfallentwurf_Test-Case-Design_v2.md # Finaler Testfallentwurf (17+ Testfälle)
│ ├── Testplan.md # Ursprünglicher Testplan
│ ├── Testplan_v2.md # Finaler Testplan
│ ├── Zustandsuebergangstest.md # State Transition Testing (ATM)
│ └── Äquivalenzklassen_und_Grenzwertanalyse.md # EP + BVA Dokumentation
│
├── Testautomatisierung/
│ └── HW1_PyTest
├── .gitignore
└── README.md

```

---

## 🐞 Bug-Reports

Alle gefundenen Fehler werden als **GitHub Issues** dokumentiert – mit Prioritäten, Umgebung und Reproduktionsschritten.

➡️ [Issues ansehen](https://github.com/uniquebughuntress/QA-Portfolio/issues)

---

## 📫 Kontakt & Austausch

Feedback, Hinweise oder einfach nur ein fachlicher Austausch sind willkommen.  
Du erreichst mich hier auf GitHub – oder über [dein bevorzugtes Medium, z. B. LinkedIn].

---

*Letzte Aktualisierung: 12.06.2026*  
*– Always learning, always hunting bugs.*
