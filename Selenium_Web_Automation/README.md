# 🤖 Selenium Web Automation

Automatisierte UI-Tests mit **Python**, **PyTest** und **Selenium WebDriver**.

Dieses Verzeichnis enthält meine ersten Projekte zur Browserautomatisierung. Ziel war es, grundlegende Selenium-Konzepte kennenzulernen und durch Fixtures, Parametrisierung und saubere Teststrukturen wartbaren Testcode zu schreiben.

---

## 🛠 Technologien

- Python
- Selenium WebDriver
- PyTest
- Firefox
- WebDriverWait
- XPath
- CSS-Selektoren

---

## 📚 Inhalte

### 1. SauceDemo – Login & Produkttest

**Testseite**

https://www.saucedemo.com/

#### Automatisierte Szenarien

- Erfolgreicher Login
- Parametrisierter Login für alle Testnutzer
- Überprüfung der Produktseite
- Verifikation des Produkts
  - Sauce Labs Backpack

#### Gelernte Konzepte

- WebDriver
- find_element()
- send_keys()
- click()
- Assertions
- Fixtures
- Parametrisierung
- Wiederverwendbarer Browser-Setup

---

### 2. Automation Exercise – Registrierung

**Testseite**

https://automationexercise.com/

#### Automatisierte Szenarien

- Benutzerregistrierung
- Formularautomatisierung
- Dropdowns
- Checkboxen
- Dynamische Testdaten
- Konto löschen

#### Gelernte Konzepte

- WebDriverWait
- Expected Conditions
- Select
- UUID für eindeutige E-Mail-Adressen
- Firefox-Profil
- Umgang mit Cookie-Bannern
- End-to-End-Test

---

## 📁 Projektstruktur

```
Selenium_Web_Automation/
│
├── SauceDemo/
│
├── AutomationExercise/
│
└── README.md
```

---

## 📖 Wichtige Selenium-Konzepte

- Browser starten
- Locators
- CSS Selector
- XPath
- Explicit Waits
- Dropdowns
- Formulare
- Assertions
- Parametrisierung
- Fixtures

---

## 💡 Erkenntnisse

Während dieser Übungen habe ich gelernt,

- warum `WebDriverWait` robuster ist als `time.sleep()`,
- wie sich Testcode durch Fixtures wiederverwenden lässt,
- wie Parametrisierung Redundanz reduziert,
- wie dynamische Testdaten erzeugt werden,
- warum stabile Locators entscheidend für wartbare UI-Tests sind.
