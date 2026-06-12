# Entscheidungstabellentest

## Aufgabenstellung

Das Szenario betrifft ein Zugticket-System mit verschiedenen Rabatten.

Die Bedingungen für die Anwendung eines Rabatts sind:

1. Der Fahrgast ist Senior (65 Jahre oder älter): **20 % Rabatt**
2. Der Fahrgast ist Student: **15 % Rabatt**
3. Der Fahrgast reist außerhalb der Hauptverkehrszeiten: **10 % Rabatt**
4. Der Fahrgast besitzt eine Vielfahrerkarte: **5 % Rabatt**

Rabatte können kombiniert werden, und der Gesamtrabatt ist die Summe aller zutreffenden Rabatte.

**Ziel:** Erstellen Sie eine Entscheidungstabelle zur Überprüfung der Rabattlogik im Zugticket-System.

Im Einzelnen:

1. Alle Bedingungen identifizieren, die die Anwendung eines Rabatts beeinflussen
2. Den Rabattprozentsatz für jede Bedingung bestimmen
3. Eine Entscheidungstabelle mit **allen möglichen Kombinationen** der Bedingungen erstellen
4. Den Gesamtrabatt für jede Kombination basierend auf den erfüllten Bedingungen berechnen

---

## Lösung

### 1. Bedingungen und Aktionen

**Bedingungen (jeweils Ja / Nein):**

| Bedingung | Rabatt |
|-----------|--------|
| Senior (≥ 65 Jahre) | 20 % |
| Student | 15 % |
| Außerhalb der Hauptverkehrszeiten | 10 % |
| Vielfahrerkarte | 5 % |

**Aktion:**  
Gesamtrabatt in Prozent (Summe aller zutreffenden Rabatte)

---

### 2. Anzahl der Regeln

4 Bedingungen → \( 2^4 = 16 \) Kombinationen

---

### 3. Vollständige Entscheidungstabelle

| Regel | Senior (20%) | Student (15%) | Außerhalb HVZ (10%) | Vielfahrer (5%) | **Gesamtrabatt** |
|-------|--------------|---------------|----------------------|------------------|------------------|
| 1     | Ja           | Ja            | Ja                   | Ja               | 50%              |
| 2     | Ja           | Ja            | Ja                   | Nein             | 45%              |
| 3     | Ja           | Ja            | Nein                 | Ja               | 40%              |
| 4     | Ja           | Ja            | Nein                 | Nein             | 35%              |
| 5     | Ja           | Nein          | Ja                   | Ja               | 35%              |
| 6     | Ja           | Nein          | Ja                   | Nein             | 30%              |
| 7     | Ja           | Nein          | Nein                 | Ja               | 25%              |
| 8     | Ja           | Nein          | Nein                 | Nein             | 20%              |
| 9     | Nein         | Ja            | Ja                   | Ja               | 30%              |
| 10    | Nein         | Ja            | Ja                   | Nein             | 25%              |
| 11    | Nein         | Ja            | Nein                 | Ja               | 20%              |
| 12    | Nein         | Ja            | Nein                 | Nein             | 15%              |
| 13    | Nein         | Nein          | Ja                   | Ja               | 15%              |
| 14    | Nein         | Nein          | Ja                   | Nein             | 10%              |
| 15    | Nein         | Nein          | Nein                 | Ja               | 5%               |
| 16    | Nein         | Nein          | Nein                 | Nein             | 0%               |

---

### 4. Kompakte Tabellenform (wie in der Demo)

| Bedingung          | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | R15 | R16 |
|--------------------|----|----|----|----|----|----|----|----|----|-----|-----|-----|-----|-----|-----|-----|
| Senior             | Ja | Ja | Ja | Ja | Ja | Ja | Ja | Ja | Nein | Nein | Nein | Nein | Nein | Nein | Nein | Nein |
| Student            | Ja | Ja | Ja | Ja | Nein | Nein | Nein | Nein | Ja | Ja | Ja | Ja | Nein | Nein | Nein | Nein |
| Außerhalb HVZ      | Ja | Ja | Nein | Nein | Ja | Ja | Nein | Nein | Ja | Ja | Nein | Nein | Ja | Ja | Nein | Nein |
| Vielfahrer         | Ja | Nein | Ja | Nein | Ja | Nein | Ja | Nein | Ja | Nein | Ja | Nein | Ja | Nein | Ja | Nein |
| **Gesamtrabatt**   | 50%| 45%| 40%| 35%| 35%| 30%| 25%| 20%| 30%| 25%| 20%| 15%| 15%| 10%| 5%| 0% |

---

## Hinweise zur Umsetzung

- Das Format der Tabelle folgt dem Beispiel aus der Demo (Zugangskontrollsystem).
- Die Reihenfolge der Regeln entspricht der binären Zählweise (Ja = 1, Nein = 0), beginnend mit „Alle Ja“ bis „Alle Nein“.
