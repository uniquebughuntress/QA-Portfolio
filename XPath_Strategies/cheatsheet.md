# XPath Cheatsheet

## Beliebiges Element

```xpath
//tag
```

---

## Attribut

```xpath
//input[@id="email"]
```

---

## Mehrere Attribute

```xpath
//input[@type="text" and @name="username"]
```

---

## Sichtbarer Text

```xpath
//button[text()="Login"]
```

---

## Teiltext

```xpath
//button[contains(text(),"Login")]
```

---

## Attribut enthält Text

```xpath
//a[contains(@href,"login")]
```

---

## Beginnt mit

```xpath
//input[starts-with(@id,"user")]
```

---

## Kind-Element

```xpath
//div/p
```

---

## Nachfahre

```xpath
//section//button
```

---

## Parent

```xpath
//input/parent::div
```

---

## Ancestor

```xpath
//button/ancestor::form
```

---

## Following sibling

```xpath
//label[text()="Email"]/following-sibling::input
```

---

## Preceding sibling

```xpath
//input[@id="email"]/preceding-sibling::label
```

---

## Erstes Element

```xpath
(//button)[1]
```

---

## Letztes Element

```xpath
(//button)[last()]
```

---

## N-tes Element

```xpath
(//button)[3]
```

---

## Kombination aus Kontext und Text

```xpath
//div[@class="card"][h3[text()="Apple"]]
```

---

## Mehrere Bedingungen

```xpath
//input[@type="email" and @required]
```

---

## Oder-Bedingung

```xpath
//input[@id="email" or @name="email"]
```

---

# Achsen

| Achse | Beschreibung |
|--------|--------------|
| parent | Elternelement |
| child | Kind |
| ancestor | Vorfahre |
| descendant | Nachfahre |
| following-sibling | nächstes Geschwister |
| preceding-sibling | vorheriges Geschwister |

---

# Häufig verwendete Funktionen

| Funktion | Beispiel |
|----------|----------|
| text() | `//button[text()="Save"]` |
| contains() | `contains(@class,"btn")` |
| starts-with() | `starts-with(@id,"user")` |
| last() | `(//li)[last()]` |
