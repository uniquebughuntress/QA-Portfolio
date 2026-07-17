# XPath – GroceryMate

## 🎯 Ziel

In dieser Übung werden XPath-Locatoren für verschiedene Bereiche der Anwendung **GroceryMate** erstellt.

Der Schwerpunkt liegt auf der Auswahl möglichst **stabiler, eindeutiger und wartbarer Locatoren** für die spätere Testautomatisierung mit Selenium.

---

# Testanwendung

🌐 https://grocerymate.masterschool.com

Die XPath-Ausdrücke beziehen sich auf die zum Zeitpunkt der Bearbeitung aktuelle Version der Anwendung.

---

# Aufgaben und Lösungen

## Aufgabe 1

### Beschreibung

Ermittle den XPath für das hervorgehobene Header-Symbol.

### XPath

```xpath
//div[@class="headerIcon"][1]
```

### Warum diese Lösung?

- Es stehen keine eindeutigen Attribute (`id`, `data-test`, `aria-*`) zur Verfügung.
- Deshalb wird hier bewusst ein positionsbasierter XPath verwendet.
- In produktiven Anwendungen wären eindeutige `data-test`-Attribute die bevorzugte Lösung.

---

## Aufgabe 2

### Beschreibung

Erstelle XPath-Ausdrücke für die Login-Seite.

### E-Mail

```xpath
//input[@type="email"]
```

### Passwort

```xpath
//input[@type="password"]
```

### Sign In

```xpath
//button[@type="submit"]
```

### Create a new account

```xpath
//a[@class="switch-link"]
```

### Go to Home

```xpath
//a[@class="home-link"]
```

### Warum diese Lösung?

- Verwendung funktionaler Attribute (`type`)
- Klassen werden nur verwendet, wenn sie eindeutig sind.
- Textbasierte Locators wurden bewusst vermieden.

---

## Aufgabe 3

### Beschreibung

Erstelle XPath-Ausdrücke für das Registrierungsformular.

### Full Name

```xpath
//input[@placeholder="Full Name"]
```

### E-Mail

```xpath
//input[@type="email"]
```

### Passwort

```xpath
//input[@type="password"]
```

### Sign Up

```xpath
//button[@type="submit"]
```

### Warum diese Lösung?

Für das Namensfeld existiert kein eindeutiges Attribut.

Der Placeholder wurde deshalb als eindeutigstes verfügbares Merkmal gewählt.

In produktiven Anwendungen wären eindeutige IDs oder `data-test`-Attribute vorzuziehen.

---

## Aufgabe 4

### Beschreibung

Ermittle den XPath für die **Confirm**-Schaltfläche im Altersverifizierungs-Modal.

### XPath

```xpath
//div[@class="modal-content"]//button[text()="Confirm"]
```

### Warum diese Lösung?

- Suche wird auf das Modal beschränkt.
- Der Button wird zusätzlich über seinen sichtbaren Text identifiziert.
- Ein exakter Textvergleich ist hier präziser als `contains()`.

---

## Aufgabe 5

### Beschreibung

Erstelle XPath-Ausdrücke für eine Produktkarte auf der Shop-Seite.

### Mengeneingabefeld

```xpath
//div[@class="product-card"][1]//input[@type="number"]
```

### Add to Cart

```xpath
//div[@class="product-card"][1]//button[@class="btn btn-primary btn-cart"]
```

### Add to Wish List

```xpath
//div[@class="product-card"][1]//div[@class="col-1"]/button
```

### Warum diese Lösung?

Die ursprüngliche Aufgabenstellung verweist auf das Produkt **Oranges**.

Zum Zeitpunkt der Bearbeitung war dieses Produkt in der aktuellen Version der Anwendung nicht mehr vorhanden.

Da sich die Aufgabe auf die Identifikation der Bedienelemente innerhalb einer Produktkarte konzentriert, wurden die XPath-Ausdrücke anhand der ersten verfügbaren Produktkarte erstellt.

Dies stellt eine typische Situation im QA-Alltag dar, in der Spezifikation und Implementierung voneinander abweichen können.

---

# Best Practices

Bei der Auswahl der XPath-Ausdrücke wurden folgende Prioritäten berücksichtigt:

1. eindeutige `id`
2. eindeutiges `data-test`
3. funktionale Attribute (`type`, `href`, `name`)
4. eindeutige Klassen
5. sichtbarer Text
6. Kontext innerhalb der DOM-Struktur
7. Position (`[1]`, `[2]`) nur wenn erforderlich

---

# Typische Fehler

❌ Absolute XPath-Ausdrücke

```xpath
/html/body/div/div/div/div[2]/button
```

Diese reagieren empfindlich auf Änderungen der DOM-Struktur.

---

❌ Auswahl ausschließlich über CSS-Klassen

```xpath
//button[@class="btn"]
```

CSS-Klassen werden häufig erweitert oder geändert.

---

✔ Besser

```xpath
//button[@type="submit"]
```

oder

```xpath
//button[text()="Confirm"]
```

---

# QA-Hinweis

Während der Bearbeitung wurde festgestellt, dass die Aufgabenstellung nicht vollständig mit der aktuellen Version der Anwendung übereinstimmt.

Das ursprünglich verwendete Produkt **Oranges** war in der aktuellen Version nicht mehr vorhanden.

Solche Abweichungen zwischen Spezifikation und implementierter Anwendung sollten im Projekt dokumentiert und mit Product Owner oder Entwicklungsteam abgestimmt werden.

---

# Was ich in dieser Übung gelernt habe

- Locator-Strategien bewerten
- funktionale Attribute bevorzugen
- Kontext zur Eingrenzung nutzen
- Positionen nur als letzte Option verwenden
- Spezifikation und Ist-Zustand kritisch vergleichen

---

# Was ich in dieser Übung gelernt habe

- Auswahl geeigneter XPath-Locatoren
- Priorisierung von Attributen
- Einsatz von Kontext in XPath-Ausdrücken
- bewusster Umgang mit positionsbasierten Locators
- Bewertung der Wartbarkeit von Locators
- Vergleich zwischen Aufgabenstellung und aktuellem Anwendungsstand

---

# Weiterführende Informationen

- 📄 `best_practices.md`
- 📄 `cheatsheet.md`
- 📄 `interview_questions.md`
