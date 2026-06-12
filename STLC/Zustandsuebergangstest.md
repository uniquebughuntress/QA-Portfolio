## 1. Zustandsübergangstest

### 1.1. Zustände, Übergänge und Ereignisse

**Zustände:**

| ID | Zustand |
| --- | --- |
| S1 | Start |
| S2 | Warte auf PIN |
| S3 | PIN-Eingabe |
| S4 | Zugriff gewährt |
| S5 | Karte eingezogen |

**Ereignisse/Übergänge:**

- **Start → Warte auf PIN:**
Benutzer führt die Karte ein.
- **Warte auf PIN → PIN-Eingabe:**
Benutzer beginnt mit der Eingabe der PIN.
- **PIN-Eingabe → Zugriff gewährt:**
Benutzer gibt die korrekte PIN ein.
- **PIN-Eingabe → PIN-Eingabe:**
Benutzer gibt eine falsche PIN ein und hat noch weniger als 3 Versuche.
- **PIN-Eingabe → Karte eingezogen:**
Benutzer gibt eine falsche PIN ein und überschreitet die maximale Anzahl von 3 Versuchen.

### 1.2. Zustandsübergangsdiagramm und Zustandsübergangstabelle

### **Zustandsübergangsdiagramm ATM:**

![Zustandsdiagramm ATM](-Bild folgt)


### Zustandsübergangstabelle ATM:

|  | E1: Karte eingeführt | E2: PIN-Eingabe beginnt | E3: PIN korrekt | E4: PIN falsch (1-2 Versuche) | E5: PIN falsch (3.Versuch) |
| --- | --- | --- | --- | --- | --- |
| **S1: Start** | S2 |  |  |  |  |
| **S2: Warte auf PIN** |  | S3 |  |  |  |
| **S3: PIN-Eingabe** |  |  | S4 | S3 | S5 |
| **S4: Zugriff gewährt** |  |  |  |  |  |
| **S5: Karte eingezogen** |  |  |  |  |  |

## 2. Überdeckung

### 2.1. Kontrollflussdiagramm (is_shipping_free)

In diesem Kontext wird dies als **Kontrollfluss** innerhalb des Codes betrachtet (sowohl bedingte als auch unbedingte Verbindungen).

![Kontrollflussdiagramm - Code-Flow für is_shipping_free Funktion] (- Bild folgt)


### 2.2 Berechnung der Anweisungsüberdeckung (Statement Coverage) und der Zweigüberdeckung (Branch Coverage)

### Analyse der Testfälle

| Testfall | IF1 | Statement 2 | IF2 | Statement 3 | ELIF | Statement 4 | Rückgabe |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `is_shipping_free(30,2,True)` | TRUE | ✔ | TRUE | ✔ | – | – | `True` |
| `is_shipping_free(15,1,False)` | FALSE | – | FALSE | – | TRUE | ✔ | `False` |
| `is_shipping_free(15,1,True)` | TRUE | ✔ | FALSE | – | TRUE | ✔ | `False` |
| `is_shipping_free(50,1,False)` | FALSE | – | TRUE | ✔ | – | – | `True` |

---

### Anweisungsüberdeckung (Statement Coverage)

### Ausführbare Statements

| Nr. | Statement | Getestet |
| --- | --- | --- |
| 1 | `print("Additional Statement 1")` | ✔ |
| 2 | `print("Additional Statement 2")` | ✔ |
| 3 | `print("Additional Statement 3")` | ✔ |
| 4 | `print("Additional Statement 4(discount)")` | ✔ |
| 5 | `return False` | ✔ |
| 6 | `return True` | ✔ |
| 7 | `print("Additional Statement 5")` | ✘ |

---

### Berechnung

- Getestete Statements: **6**
- Gesamte Statements: **7**

$\frac{6}{7}$ x 100 = 85.7 %

#### Statement Coverage = 85.7 %

---

### Zweigüberdeckung (Branch Coverage)

### Übersicht der Zweige

| Bedingung | TRUE getestet | FALSE getestet |
| --- | --- | --- |
| `if price > 50 or isPrimeShoppingMember` | ✔ | ✔ |
| `if price > 25 and numberOfItems < 3` | ✔ | ✔ |
| `elif price > 10 and numberOfItems == 1` | ✔ | ✘ |

---

### Berechnung

- Gesamtanzahl Zweige: **6**
- Getestete Zweige: **5**

$\frac{5}{6}$ x 100 = 83.3%

#### Branch Coverage = 83.3 %

---

### 2.3 Berechnung der Anweisungsüberdeckung und der Zweigüberdeckung, wenn die Zeile `print("Additional Statement 5")` aus dem Code entfernt wird

#### Neue Anweisungsüberdeckung (Statement Coverage)

Nach Entfernen der unerreichbaren Zeile:

```python
print("Additional Statement 5")
```

existieren nur noch **6 ausführbare Statements**.

---

#### Berechnung

- Getestete Statements: **6**
- Gesamte Statements: **6**

$\frac{6}{6}$ x 100 = 100%

#### Statement Coverage = 100 %

---

### Neue Zweigüberdeckung (Branch Coverage)

Die Zweige ändern sich nicht, da nur unerreichbarer Code entfernt wurde.

| Bedingung | TRUE getestet | FALSE getestet |
| --- | --- | --- |
| `if price > 50 or isPrimeShoppingMember` | ✔ | ✔ |
| `if price > 25 and numberOfItems < 3` | ✔ | ✔ |
| `elif price > 10 and numberOfItems == 1` | ✔ | ✘ |

---

### Berechnung

- Gesamtanzahl Zweige: **6**
- Getestete Zweige: **5**

$\frac{5}{6}$ x 100 = 83.3%

#### Branch Coverage = 83.3 %
