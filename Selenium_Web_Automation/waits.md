# Selenium Waits

## Warum Waits?

Moderne Webseiten laden Inhalte asynchron.

Ohne Waits entstehen häufig instabile Tests.

---

# Implicit Wait

```python
driver.implicitly_wait(10)
```

Gilt für alle Element-Suchen.

---

# Explicit Wait

```python
wait = WebDriverWait(driver, 10)
```

---

## Sichtbarkeit

```python
wait.until(
    EC.visibility_of_element_located(locator)
)
```

---

## Klickbarkeit

```python
wait.until(
    EC.element_to_be_clickable(locator)
)
```

---

## Element vorhanden

```python
wait.until(
    EC.presence_of_element_located(locator)
)
```

---

## URL

```python
wait.until(
    EC.url_contains("login")
)
```

---

## Titel

```python
wait.until(
    EC.title_contains("Dashboard")
)
```

---

## Element verschwindet

```python
wait.until(
    EC.invisibility_of_element(locator)
)
```

---

# Warum keine time.sleep()?

❌

```python
time.sleep(5)
```

Probleme

- unnötig langsam
- instabil
- feste Wartezeit

✔

```python
WebDriverWait(...)
```

wartet nur so lange wie nötig.

---

# Best Practice

- Explicit Wait bevorzugen
- Implicit Wait sparsam einsetzen
- `time.sleep()` möglichst vermeiden
