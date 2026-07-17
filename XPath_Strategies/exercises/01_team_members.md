# XPath – Team Members (HTML-Dokument)

## 🎯 Ziel

In dieser Übung werden verschiedene XPath-Ausdrücke anhand eines verschachtelten HTML-Dokuments erstellt.

Der Schwerpunkt liegt auf der Entwicklung **robuster und wartbarer XPath-Locatoren**, wie sie in der Testautomatisierung mit Selenium verwendet werden.

---

# HTML-Dokument

Alle XPath-Ausdrücke beziehen sich auf folgendes HTML-Dokument:

📄 `html/team_members.html`

---

# Aufgaben und Lösungen

## Aufgabe 1

### Beschreibung

Finde das Haupt-`<h1>`-Element.

### XPath

```xpath
//h1[@id="mainTitle"]
```

### Warum diese Lösung?

- verwendet eine eindeutige `id`
- eindeutig und gut wartbar
- unabhängig von der Position im DOM

---

## Aufgabe 2

### Beschreibung

Wähle den Navigationslink **About Us** aus.

### XPath

```xpath
//a[@href="#about"]
```

### Warum diese Lösung?

- nutzt ein eindeutiges Attribut (`href`)
- einfacher und stabiler als ein positionsbasierter XPath

---

## Aufgabe 3

### Beschreibung

Wähle den Dropdown-Link **Graphic Design** aus.

### XPath

```xpath
//a[@href="#graphicdesign"]
```

### Warum diese Lösung?

- eindeutiges Attribut
- unabhängig von der Position innerhalb des Dropdown-Menüs

---

## Aufgabe 4

### Beschreibung

Wähle den Namen des Teammitglieds **Jane Smith** aus.

### XPath

```xpath
//h4[text()="Jane Smith"]
```

### Warum diese Lösung?

- verwendet den sichtbaren Text
- gut lesbar
- eindeutig

---

## Aufgabe 5

### Beschreibung

Wähle die Beschreibung der **SEO Services** aus.

### XPath

```xpath
//div[@class="service-item"][h3[text()="SEO Services"]]/p
```

### Warum diese Lösung?

- kombiniert Kontext und sichtbaren Text
- deutlich robuster als eine Positionsangabe

---

## Aufgabe 6

### Beschreibung

Wähle alle Service-Elemente im Abschnitt **Our Services** aus.

### XPath

```xpath
//section[@id="services"]//div[@class="service-item"]
```

### Warum diese Lösung?

- Suche wird auf den Abschnitt beschränkt
- liefert alle Service-Karten

---

## Aufgabe 7

### Beschreibung

Wähle das E-Mail-Eingabefeld im Kontaktformular aus.

### XPath

```xpath
//input[@id="email"]
```

### Warum diese Lösung?

- eindeutige `id`
- bevorzugte Locator-Strategie

---

## Aufgabe 8

### Beschreibung

Wähle das gesamte Kontaktformular aus.

### XPath

```xpath
//form[@id="contactForm"]
```

### Warum diese Lösung?

- verwendet die Formular-ID
- eindeutig und leicht verständlich

---

## Aufgabe 9

### Beschreibung

Wähle den Absatz im Footer aus.

### XPath

```xpath
//footer/p
```

### Warum diese Lösung?

- nutzt die HTML-Struktur
- einfach und gut lesbar

---

## Aufgabe 10

### Beschreibung

Wähle den Namen (`<h4>`) des ersten Teammitglieds aus.

### XPath

```xpath
(//div[@class="team"]//h4)[1]
```

### Warum diese Lösung?

- liefert das erste gefundene `<h4>` innerhalb des Team-Bereichs
- relative XPath
- robust gegenüber Änderungen außerhalb dieses Bereichs

---

## Aufgabe 11

### Beschreibung

Wähle die Beschreibung des zweiten Service-Elements aus.

### XPath

```xpath
//div[@class="service-item"][2]/p
```

### Warum diese Lösung?

- nutzt bewusst einen Index
- sinnvoll, da explizit das zweite Element gefordert ist

---

## Aufgabe 12

### Beschreibung

Wähle die Überschrift der Sektion **Contact Us** aus.

### XPath

```xpath
//section[@id="contact"]//h2[@class="sectionTitle"]
```

### Warum diese Lösung?

- kombiniert Abschnitt und Klasse
- eindeutig und gut wartbar

---

## Aufgabe 13

### Beschreibung

Wähle alle Links innerhalb des Dropdown-Menüs **Services** aus.

### XPath

```xpath
//a[@class="nav-link" and text()="Services"]/following-sibling::ul//a
```

### Warum diese Lösung?

- verwendet die Beziehung zwischen Geschwisterelementen (`following-sibling`)
- unabhängig von der Anzahl der Menüeinträge

---

## Aufgabe 14

### Beschreibung

Wähle das erste `<li>` im Bereich **Our Team** aus.

### XPath

```xpath
//div[@class="team"]//li[1]
```

### Warum diese Lösung?

- beschränkt die Suche auf den Team-Bereich
- wählt gezielt das erste Listenelement

---

## Aufgabe 15

### Beschreibung

Wähle die Schaltfläche **Send Message** aus.

### XPath

```xpath
//form[@id="contactForm"]//input[@type="submit"]
```

### Warum diese Lösung?

- Suche wird auf das Formular beschränkt
- verwendet den Eingabetyp
- gut lesbar und wartbar

---

# Best Practices

Bei der Erstellung der XPath-Ausdrücke wurde bewusst versucht, möglichst **stabile und wartbare Locatoren** zu verwenden.

**Empfohlene Reihenfolge bei der Wahl eines Locators:**

1. Eindeutige `id`
2. Eindeutiges Attribut (z. B. `name`, `href`, `type`)
3. Sichtbarer Text (`text()`)
4. Kontextbasierte XPath-Ausdrücke
5. Positionsbasierte XPath-Ausdrücke (`[1]`, `[2]`) nur wenn erforderlich

---

# Typische Fehler

❌ Absolute XPath-Ausdrücke wie

```xpath
/html/body/main/section[1]/div/div/ul/li[2]/h4
```

sind sehr empfindlich gegenüber Änderungen der HTML-Struktur.

✔ Besser:

```xpath
//h4[text()="Jane Smith"]
```

oder

```xpath
//div[@class="team"]//h4[text()="Jane Smith"]
```

---

# Was ich in dieser Übung gelernt habe

- relative XPath-Ausdrücke
- Auswahl über Attribute
- Auswahl über sichtbaren Text (`text()`)
- Kontextbasierte XPath-Ausdrücke
- Positionsbasierte Auswahl
- `following-sibling`
- Auswahl verschachtelter Elemente
- Erstellung wartbarer Locatoren

---

# Mock-Interview-Fragen

- Wann würdest du XPath einem CSS-Selektor vorziehen?
- Warum sollten absolute XPath-Ausdrücke möglichst vermieden werden?
- Wann ist die Verwendung eines Index (`[1]`, `[2]`) sinnvoll?
- Welche Locator-Strategie würdest du bevorzugen, wenn sowohl `id` als auch `text()` verfügbar sind?

---

# Mögliche Antworten

> Ich bevorzuge grundsätzlich CSS-Selektoren, wenn sie die gewünschte Eindeutigkeit bieten, da sie in der Regel einfacher zu lesen und oft etwas performanter sind. XPath verwende ich dann, wenn CSS an seine Grenzen stößt – beispielsweise bei der Auswahl anhand von Textinhalten, komplexen Beziehungen zwischen Elementen (z. B. parent, ancestor, following-sibling) oder bei verschachtelten Strukturen. Die Wahl des Locators richtet sich letztlich nach Stabilität, Lesbarkeit und Wartbarkeit.
> Absolute XPath-Ausdrücke sind eng an die aktuelle DOM-Struktur gebunden. Bereits kleine Änderungen, beispielsweise das Einfügen eines zusätzlichen Containers oder eines neuen Elements, können den XPath ungültig machen. Relative XPath-Ausdrücke sind deutlich robuster und dadurch langfristig wartbarer. 
> Positionsbasierte XPath-Ausdrücke sollten möglichst vermieden werden. Sie sind jedoch sinnvoll, wenn die Position selbst Bestandteil der Anforderung ist – beispielsweise "das erste Teammitglied" oder "das zweite Service-Element". Fehlen eindeutige Attribute oder Texte, kann ein Index ebenfalls eine praktikable Lösung sein.
> Ich würde eine eindeutige id bevorzugen. IDs sind für die eindeutige Identifikation von Elementen vorgesehen und ändern sich in gut gepflegten Anwendungen seltener als sichtbare Texte. Textbasierte Locators können dagegen durch Übersetzungen, UI-Anpassungen oder Änderungen im Wording beeinflusst werden.
