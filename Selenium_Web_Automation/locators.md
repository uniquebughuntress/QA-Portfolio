# Selenium Locators

## Priorität

1. data-test / data-testid
2. ID 
3. Name
4. CSS Selector
5. XPath
6. Link Text
7. Class Name

---

## ID

```python
By.ID
```

---

## Name

```python
By.NAME
```

---

## CSS Selector

```python
By.CSS_SELECTOR
```

Beispiele

```css
#username

.login

button[type="submit"]

input[name="email"]
```

---

## XPath

```python
By.XPATH
```

Beispiele

```xpath
//button[@type="submit"]

//input[@id="email"]

//a[text()="Login"]
```

---

## Link Text

```python
By.LINK_TEXT
```

---

## Partial Link Text

```python
By.PARTIAL_LINK_TEXT
```

---

## Class Name

```python
By.CLASS_NAME
```

---

# Best Practice

Empfohlene Reihenfolge

- ID
- data-test
- Name
- CSS
- XPath
- Class Name
