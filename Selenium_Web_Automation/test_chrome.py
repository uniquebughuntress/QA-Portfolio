# Importiere das notwendige Modul, um den Web-Browser zu kontrollieren
from selenium import webdriver
import time  # Importiere das Time-Modul, um Wartezeiten hinzuzufügen

# Initiiere den Web-Treiber für den Chrome-Browser
driver = webdriver.Chrome()

# Navigiere zu der Masterschool-Webseite
driver.get("https://www.masterschool.com")

# Warte für 3 Sekunden, um die Webseite komplett zu laden
time.sleep(3)  # besser: explizite Waits (WebDriverWait) // flaky Test

# Schreibe den Titel der Webseite in die Konsole
print(driver.title)

# Schließe den Web-Browser und beende die Web-Treiber-Session
driver.quit()
