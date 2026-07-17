# XPath – Best Practices

## Ziel

Diese Best Practices helfen dabei, stabile, wartbare und gut lesbare XPath-Locatoren für die Testautomatisierung mit Selenium zu erstellen.

---

# Reihenfolge bei der Wahl eines Locators

Wenn mehrere Möglichkeiten existieren, bevorzuge folgende Reihenfolge:

1. `id`
2. `data-test` / `data-testid`
3. `name`
4. Funktionale Attribute (`type`, `href`, `role`, ...)
5. Sichtbarer Text (`text()`)
6. Kontextbasierte XPath-Ausdrücke
7. Positionsbasierte XPath-Ausdrücke (`[1]`, `[2]`)

---

# Relative statt absolute XPath-Ausdrücke

❌ Vermeiden

```xpath
/html/body/div/div/main/section[2]/div[3]/button
```

✔ Bevorzugen

```xpath
//button[@type="submit"]
```

oder

```xpath
//section[@id="contact"]//button
```

---

# Möglichst eindeutige Attribute verwenden

✔ Gut

```xpath
//input[@id="email"]
```

```xpath
//button[@data-test="login"]
```

❌ Weniger gut

```xpath
//button[@class="btn"]
```

---

# Kontext sinnvoll nutzen

Wenn mehrere Elemente gleich aussehen:

```xpath
//div[@class="product-card"][h3[text()="Apple"]]/button
```

statt

```xpath
//button[@class="btn-cart"]
```

---

# Sichtbaren Text gezielt einsetzen

Wenn der Text stabil ist:

```xpath
//button[text()="Confirm"]
```

Nicht geeignet bei:

- mehrsprachigen Anwendungen
- häufig wechselnden UI-Texten

---

# Positionsbasierte XPath-Ausdrücke sparsam verwenden

Nur verwenden, wenn

- die Position Teil der Anforderung ist
- keine eindeutigen Attribute vorhanden sind

Beispiel

```xpath
(//div[@class="team"]//h4)[1]
```

---

# XPath möglichst kurz halten

✔

```xpath
//input[@id="password"]
```

statt

```xpath
//html/body/div/main/form/div/input[@id="password"]
```

---

# Lesbarkeit ist wichtiger als Kürze

Ein Locator sollte auch Monate später noch verständlich sein.

---

# QA-Empfehlung

Ein guter XPath ist

- eindeutig
- stabil
- wartbar
- leicht verständlich
- möglichst unabhängig von Layoutänderungen

Nicht der kürzeste XPath ist der beste, sondern derjenige, der langfristig zuverlässig funktioniert.
