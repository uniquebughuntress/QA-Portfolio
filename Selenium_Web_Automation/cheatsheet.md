# Selenium WebDriver Cheatsheet

## Browser starten

```python
from selenium import webdriver

driver = webdriver.Firefox()
driver = webdriver.Chrome()
```

---

## Webseite öffnen

```python
driver.get("https://example.com")
```

---

## Browser schließen

```python
driver.quit()
```

---

## Seitentitel

```python
driver.title
```

---

## Aktuelle URL

```python
driver.current_url
```

---

## Element finden

```python
driver.find_element(By.ID, "username")
```

Mehrere Elemente

```python
driver.find_elements(By.CLASS_NAME, "product")
```

---

## Texte lesen

```python
element.text
```

---

## Attribute lesen

```python
element.get_attribute("value")
```

---

## Eingabe

```python
element.send_keys("Natalya")
```

---

## Feld leeren

```python
element.clear()
```

---

## Klick

```python
element.click()
```

---

## Dropdown

```python
from selenium.webdriver.support.ui import Select

select = Select(element)

select.select_by_visible_text("Germany")
```

---

## Checkbox

```python
checkbox.click()
```

---

## Radio Button

```python
radio.click()
```

---

## Alert

```python
alert = driver.switch_to.alert

alert.accept()
alert.dismiss()
alert.text
```

---

## Fenster wechseln

```python
driver.switch_to.window(handle)
```

---

## Screenshot

```python
driver.save_screenshot("page.png")
```

---

## Cookies

```python
driver.get_cookies()

driver.delete_all_cookies()
```

---

## JavaScript

```python
driver.execute_script(
    "arguments[0].click();",
    element
)
```

---

## Navigation

```python
driver.back()

driver.forward()

driver.refresh()
```
