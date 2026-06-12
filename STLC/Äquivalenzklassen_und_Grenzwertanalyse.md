# Hausaufgabe - Äquivalenzklassenbildung und Grenzwertanalyse

Sie sind damit beauftragt, eine Funktion zu testen, die die Einstufung von Schülern basierend auf ihren Punktzahlen bestimmt. Die Funktion akzeptiert eine Ganzzahl zwischen 0 und 100 (einschließlich) und gibt eine Zeichenkette als Einstufung zurück, wie folgt:

- *„Nicht bestanden“ für Punktzahlen von 0–49*
- *„Bestanden“ für Punktzahlen von 50–69*
- *„Leistung“ für Punktzahlen von 70–89*
- *„Auszeichnung“ für Punktzahlen von 90–100*

**Aufgabe:** Entwerfen Sie Testfälle unter Verwendung von **Äquivalenzklassenbildung** und **Grenzwertanalyse**.

1. Identifizieren und definieren Sie Äquivalenzklassen für den Eingabebereich und kennzeichnen Sie diese als gültig oder ungültig.
2. Identifizieren und definieren Sie Grenzwerte für den Eingabebereich unter Verwendung der Zweiwert-Grenzwertanalyse-Technik.
3. Auf Grundlage von Aufgabe 1 und 2: Welche Testfälle können Sie entwerfen? Wie viele?

---

## 1. Äquivalenzklassen identifizieren und definieren (als gültig oder ungültig kennzeichnen)

Die Äquivalenzklassenbildung ist ein Black-Box-Testentwurfsverfahren, bei dem Eingabewerte in Klassen gruppiert werden, die ein gleichartiges Systemverhalten erwarten lassen. Das Ziel ist, aus jeder Klasse repräsentative Testfälle auszuwählen.

**Gültige Äquivalenzklassen** (innerhalb des spezifizierten Wertebereichs 0 bis 100) sind:

- **Klasse 1: Punktzahlen 0–49** → **„Nicht bestanden“**
- **Klasse 2: Punktzahlen 50–69** → **„Bestanden“**
- **Klasse 3: Punktzahlen 70–89** → **„Leistung“**
- **Klasse 4: Punktzahlen 90–100** → **„Auszeichnung“**

**Ungültige Äquivalenzklassen** (außerhalb des spezifizierten Wertebereichs) sind:

- **Klasse 5: Punktzahlen < 0** (negative Ganzzahlen)
- **Klasse 6: Punktzahlen > 100**

---

## 2. Grenzwerte gemäß Grenzwertanalyse definieren

Die Grenzwertanalyse ist ein weiteres wichtiges Black-Box-Testentwurfsverfahren. Hier werden Fehler oft an den "Kanten bzw. Grenzen" von Äquivalenzklassen gefunden, also direkt an oder knapp über/unter den Grenzwerten.

Für jede Äquivalenzklasse betrachten wir daher:

- die untere Grenze
- die obere Grenze
- und ggf. Werte direkt daneben

=> **Zweiwertige Grenzwertanalyse**: Betrachtet wird der Wert selbst und der nächste benachbarte Wert innerhalb der Klasse.

| Klassifikation | Untere Grenze (Wert, Nachbar) | Obere Grenze (Wert, Nachbar) |
| --- | --- | --- |
| Nicht bestanden | 0, 1 | 49, 50 |
| Bestanden | 50, 49 | 69, 70 |
| Leistung | 70, 69 | 89, 90 |
| Mit Auszeichnung | 90, 89 | 100, 101 (101 ungültig) |
| Ungültige Eingaben | -1 (ungültig), 0 (gültig) | 100 (gültig), 101 (ungültig) |

---

## 3. Testfälle basierend auf Äquivalenzklassenbildung & Grenzwertanalyse

| Testfall-ID | Beschreibung | Eingabe (Punktzahl) | Erwartetes Ergebnis |
| --- | --- | --- | --- |
| TC1 | Knapp unter unterer Gesamtgrenze | -1 | Ungültige Eingabe |
| TC2 | Exakt untere Gesamtgrenze | 0 | „Nicht bestanden“ |
| TC3 | Direkt über unterer Gesamtgrenze | 1 | „Nicht bestanden“ |
| TC4 | Knapp unter „Bestanden“ (Grenze 49/50) | 49 | „Nicht bestanden“ |
| TC5 | Exakt untere Grenze „Bestanden“ | 50 | „Bestanden“ |
| TC6 | Knapp unter „Leistung“ (Grenze 69/70) | 69 | „Bestanden“ |
| TC7 | Exakt untere Grenze „Leistung“ | 70 | „Leistung“ |
| TC8 | Knapp unter „Auszeichnung“ (Grenze 89/90) | 89 | „Leistung“ |
| TC9 | Exakt untere Grenze „Auszeichnung“ | 90 | „Auszeichnung“ |
| TC10 | Obere Gesamtgrenze | 100 | „Auszeichnung“ |
| TC11 | Knapp über oberer Gesamtgrenze | 101 | Ungültige Eingabe |
| TC12 | (Optional) Repräsentant Klasse 2 | 60 | „Bestanden“ |
| TC13 | (Optional) Repräsentant Klasse 3 | 80 | „Leistung“ |
| TC14 | (Optional) Repräsentant Klasse 4 | 95 | „Auszeichnung“ |
| TC15 | Repräsentativer Wert aus Klasse 1 | 30 | „Nicht bestanden“ |

### Erklärung der Anzahl

- **Grenzwertanalyse (Zwei-Wert-Technik):**  
  −1, 0, 1, 49, 50, 69, 70, 89, 90, 100, 101 → **11 Fälle**

- **Äquivalenzklassen:**  
  4 gültige + 2 ungültige Klassen → mind. 6 Fälle, aber Grenzwertanalyse erweitert dies.

- **Empfohlene minimale vollständige Menge:**  
  Die 11 Grenzfälle (−1, 0, 49, 50, 69, 70, 89, 90, 100, 101) decken bereits alle Äquivalenzklassen ab.  
  Zusätzlich kann man je einen Vertreter jeder Klasse für Robustheit nehmen (30, 60, 80, 95) → **15 Testfälle** insgesamt.
