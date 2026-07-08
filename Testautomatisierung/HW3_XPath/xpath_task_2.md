# XPath – Hausaufgabe 1

## Aufgabe 2

### 1. Schreibe das XPath für das im Bild hervorgehobene Symbol/den hervorgehobenen Button.

```xpath
//div[@class="headerIcon"][1]
```

**Anmerkung:**

Das HTML stellt für die drei Header-Icons keine eindeutigen Attribute (`id`, `data-test`, `aria-*` usw.) bereit. Daher wurde hier bewusst ein positionsbasierter XPath gewählt. In einer produktiven Testautomatisierung wären eindeutige `data-test`-Attribute die bevorzugte Lösung.

---

### 2. Öffne die Login-Seite und schreibe das XPath für alle Eingabefelder, die **"Sign In"**-Schaltfläche, den Link **"Create a new account"** und den Link **"Go to Home"**.

**E-Mail-Feld**

```xpath
//input[@type="email"]
```

**Passwort-Feld**

```xpath
//input[@type="password"]
```

**Sign In-Schaltfläche**

```xpath
//button[@type="submit"]
```

**Link "Create a new account"**

```xpath
//a[@class="switch-link"]
```

**Link "Go to Home"**

```xpath
//a[@class="home-link"]
```

**Anmerkung:**

Wo möglich wurden funktionale Attribute (`type`) bzw. eindeutige Klassen verwendet, da diese stabiler sind als sichtbare Texte oder Platzhalter.

---

### 3. Klicke auf **"Create a new account"** und schreibe das XPath für alle Eingabefelder sowie die **"Sign Up"**-Schaltfläche.

**Name**

```xpath
//input[@placeholder="Full Name"]
```

**E-Mail**

```xpath
//input[@type="email"]
```

**Passwort**

```xpath
//input[@type="password"]
```

**Sign Up-Schaltfläche**

```xpath
//button[@type="submit"]
```

**Anmerkung:**

Für das Namensfeld wurde der Placeholder verwendet, da `type="text"` nicht eindeutig genug ist. Obwohl Placeholder grundsätzlich geändert werden können, stellt er hier das eindeutigste verfügbare Merkmal dar.

---

### 4. Schreibe das XPath der **"Confirm"**-Schaltfläche im Altersverifizierungs-Modal.

```xpath
//div[@class="modal-content"]//button[text()="Confirm"]
```

**Anmerkung:**

Hier wurde bewusst auf `contains()` verzichtet, da sowohl die Klasse als auch der Button-Text eindeutig und vollständig bekannt sind. Ein exakter Vergleich ist daher präziser und besser lesbar.

---

### 5. Schreibe das XPath für das Mengeneingabefeld, die **"Add to Cart"**-Schaltfläche und die **"Add to wish list"**-Schaltfläche eines Produkts auf der Shop-Seite.

**Mengeneingabefeld**

```xpath
//div[@class="product-card"][1]//input[@type="number"]
```

**"Add to Cart"-Schaltfläche**

```xpath
//div[@class="product-card"][1]//button[@class="btn btn-primary btn-cart"]
```

**"Add to wish list"-Schaltfläche**

```xpath
//div[@class="product-card"][1]//div[@class="col-1"]/button
```

**Anmerkung:**

Die ursprüngliche Aufgabenstellung verweist auf das Produkt **"Oranges"**. Zum Zeitpunkt der Bearbeitung war dieses Produkt in der aktuellen Version der Anwendung nicht mehr vorhanden. Stattdessen beginnt der Produktkatalog mit **"Celery"**.

Da sich die Aufgabe auf das Auffinden der Bedienelemente innerhalb einer Produktkarte konzentriert und nicht auf das Testen eines bestimmten Produktnamens, wurden die XPath-Ausdrücke anhand der ersten verfügbaren Produktkarte erstellt.

---

## Anmerkungen

Während dieser Aufgabe wurde bewusst versucht, möglichst stabile und wartbare XPath-Locatoren zu verwenden.

**Priorisierung der Locator (wenn möglich):**

1. Eindeutige `id`
2. Eindeutiges `data-test`
3. Eindeutige funktionale Attribute (z. B. `type`, `href`)
4. Eindeutige Klassen
5. Sichtbarer Text
6. Kontextbasierter XPath
7. Positionsbasierter XPath – nur wenn keine stabilere Alternative verfügbar ist

**Grundsatz:**

> Nicht der kürzeste XPath ist der beste, sondern derjenige, der auch nach zukünftigen Änderungen am HTML möglichst stabil und wartbar bleibt.

**QA-Hinweis:**

Während der Bearbeitung wurde festgestellt, dass die Aufgabenstellung nicht vollständig mit der aktuellen Version der Anwendung übereinstimmt (Produktliste geändert). Solche Abweichungen zwischen Spezifikation und System sollten im QA-Alltag dokumentiert und mit dem Entwicklungsteam oder Product Owner geklärt werden.
