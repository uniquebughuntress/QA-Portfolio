# XPath – Interview Questions

## 1. Wann würdest du XPath statt CSS-Selektoren verwenden?

### Musterantwort

CSS-Selektoren bevorzuge ich für einfache und gut identifizierbare Elemente. XPath verwende ich, wenn ich anhand von sichtbarem Text, Beziehungen zwischen Elementen oder komplexeren DOM-Strukturen selektieren muss.

---

## 2. Warum sollten absolute XPath-Ausdrücke vermieden werden?

### Musterantwort

Absolute XPath-Ausdrücke hängen stark von der DOM-Struktur ab. Bereits kleine Änderungen im HTML können sie ungültig machen. Relative XPath-Ausdrücke sind robuster und leichter wartbar.

---

## 3. Wann ist ein positionsbasierter XPath sinnvoll?

### Musterantwort

Wenn die Position Teil der Anforderung ist oder keine stabileren Merkmale wie `id`, `data-test` oder eindeutige Attribute verfügbar sind.

---

## 4. Welche Locator-Reihenfolge würdest du bevorzugen?

### Musterantwort

1. `id`
2. `data-test`
3. `name`
4. funktionale Attribute
5. sichtbarer Text
6. Kontext
7. Position

---

## 5. Wann kann `text()` problematisch sein?

### Musterantwort

Bei mehrsprachigen Anwendungen oder wenn Texte häufig geändert werden. In solchen Fällen sind technische Attribute meist stabiler.

---

## 6. Warum sind `data-test`-Attribute für Testautomatisierung besonders geeignet?

### Musterantwort

Sie sind speziell für automatisierte Tests vorgesehen und ändern sich in der Regel nicht durch Layout- oder Designanpassungen. Dadurch bleiben Tests stabiler.

---

## 7. Was ist der Unterschied zwischen `child` und `descendant`?

### Musterantwort

`child` wählt nur direkte Kindelemente aus, während `descendant` alle Nachfahren unabhängig von ihrer Ebene berücksichtigt.

---

## 8. Wie würdest du vorgehen, wenn mehrere Elemente dieselbe Klasse besitzen?

### Musterantwort

Ich würde zusätzliche Attribute, sichtbaren Text oder den Kontext innerhalb der DOM-Struktur verwenden, um den Locator eindeutig zu machen.

---

## 9. Was zeichnet einen guten XPath aus?

### Musterantwort

Ein guter XPath ist eindeutig, stabil, gut lesbar und möglichst unabhängig von Änderungen der HTML-Struktur.

---

## 10. Wie gehst du vor, wenn Spezifikation und Anwendung nicht übereinstimmen?

### Musterantwort

Ich dokumentiere die Abweichung, prüfe die Reproduzierbarkeit und stimme sie mit dem Product Owner oder Entwicklungsteam ab, bevor Testfälle angepasst werden.
