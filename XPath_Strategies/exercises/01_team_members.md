# XPath

### 1. Schreibe das XPath, um das Haupt-**h1**-Element zu finden.

```xpath
//h1[@id="mainTitle"]
```

---

### 2. Schreibe das XPath, um den Navigationslink **About Us** auszuwählen.

```xpath
//a[@href="#about"]
```

---

### 3. Schreibe das XPath, um den Dropdown-Link **Graphic Design** auszuwählen.

```xpath
//a[@href="#graphicdesign"]
```

---

### 4. Schreibe das XPath, um den Namen des Teammitglieds **Jane Smith** auszuwählen.

```xpath
//h4[text()="Jane Smith"]
```

---

### 5. Schreibe das XPath, um die Beschreibung (die sich im Absatz befindet) der **SEO Services** auszuwählen.

```xpath
//div[@class="service-item"][h3[text()="SEO Services"]]/p
```

---

### 6. Schreibe einen XPath-Ausdruck, um alle Service-Elemente im Abschnitt **"Our Services"** auszuwählen.

```xpath
//section[@id="services"]//div[@class="service-item"]
```

---

### 7. Wie lautet das XPath, um das **E-Mail-Eingabefeld** im Kontaktformular auszuwählen?

```xpath
//input[@id="email"]
```

---

### 8. Wie würdest du ein XPath schreiben, um das **gesamte Kontaktformular** auszuwählen?

```xpath
//form[@id="contactForm"]
```

---

### 9. Gib das XPath an, um das **Footer-Absatz-Element** auszuwählen.

```xpath
//footer/p
```

---

### 10. Was ist das XPath, um den Namen (`<h4>`) des **ersten Teammitglieds** auszuwählen?

```xpath
//div[@class="team"]//h4[1]
```

---

### 11. Wie kannst du mit XPath die Beschreibung des **zweiten Service-Elements** auswählen?

```xpath
//div[@class="service-item"][2]/p
```

---

### 12. Was ist das XPath, um die Überschrift der Sektion **"Contact Us"** (`<h2>`-Element) auszuwählen?

```xpath
//section[@id="contact"]//h2[@class="sectionTitle"]
```

---

### 13. Schreibe einen XPath-Ausdruck, um alle Links innerhalb des Dropdowns unter dem Navigationspunkt **"Services"** auszuwählen.

```xpath
//a[@class="nav-link" and text()="Services"]/following-sibling::ul//a
```

---

### 14. Was ist das XPath, um das erste `<li>` im Abschnitt **"Our Team"** auszuwählen?

```xpath
//div[@class="team"]//li[1]
```

---

### 15. Gib das XPath an, um die Schaltfläche **"Send Message"** im Kontaktformular zu finden.

```xpath
//form[@id="contactForm"]//input[@type="submit"]
```

---

## Anmerkungen

Während dieser Aufgabe habe ich bewusst versucht, möglichst **stabile und wartbare XPath-Locatoren** zu verwenden.

**Priorisierung der Locator (wenn möglich):**

1. Eindeutige `id`
2. Eindeutiges Attribut (z. B. `href`, `type`)
3. Sichtbarer Text
4. Kontextbasierter XPath (Beziehung zwischen Elementen)
5. Positionsbasierter XPath – nur wenn die Aufgabenstellung dies ausdrücklich erfordert

**Grundsatz:**

> Nicht der kürzeste XPath ist der beste, sondern derjenige, der auch nach zukünftigen Änderungen am HTML möglichst stabil und wartbar bleibt.
