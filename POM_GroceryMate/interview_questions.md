> Frage: Warum erzeugen wir den Driver in einer Fixture und nicht in jedem Test? 
> > Antwort: Die Initialisierung des WebDrivers wurde bewusst in einer Fixture gekapselt, um den Setup-Code zu zentralisieren. Dadurch vermeiden wir Code-Duplikate und stellen sicher, dass Änderungen, beispielsweise am verwendeten Browser oder an den Browseroptionen, nur an einer Stelle vorgenommen werden müssen. Das verbessert die Wartbarkeit und Skalierbarkeit der Testautomatisierung.
 

> Frage: Warum ```import pytest```  und nicht ```from pytest import *```?
> >  Antwort: Wildcard-Imports verschleiern die Herkunft von Funktionen und Klassen. Sie verschlechtern die Lesbarkeit und können zu Namenskonflikten führen. Deshalb werden sie gemäß PEP 8 vermieden.
   

> Warum importieren wir nicht einfach das komplette Selenium-Paket?
> > Wir importieren nur die Komponenten, die wir tatsächlich benötigen. Dadurch bleibt der Code übersichtlich, vermeidet unnötige Namensräume und macht die Abhängigkeiten klar erkennbar.
     

> Single Source of Truth
> >  Es gibt genau eine Stelle, an der diese Information gepflegt wird.
     

>  Warum werden die Werte in Konstanten ausgelagert?
> >  Wir vermeiden Hardcoding und schaffen eine zentrale Konfigurationsstelle. Änderungen müssen nur an einer Stelle vorgenommen werden, wodurch Wartbarkeit, Lesbarkeit und Wiederverwendbarkeit des Codes verbessert werden.
   

>  Was ist der Unterschied zwischen Setup und Teardown?
> > Setup und Teardown sind keine technischen Features, sondern Test-Hooks zur Lebenszyklus-Steuerung. Der entscheidende Unterschied liegt nicht in der Syntax (z. B. @BeforeEach vs. @AfterEach), sondern in ihrer Verantwortung und Fehlertoleranz:
>
> > Setup ist proaktiv: Es stellt sicher, dass der Test in einem bekannten, sauberen Zustand startet (State Resurrection). Es ist fehlerkritisch – schlägt das Setup fehl, hat der Test keine Daseinsberechtigung (Fail-Fast-Prinzip). 
>
> > Teardown ist reaktiv: Es kümmert sich um die Rückführung in einen definierten Grundzustand, unabhängig vom Testergebnis. Hier liegt der wahre Architektur-Unterschied:
→ Teardown muss robust gegen Fehler im Test sein (z. B. mit try/finally oder addFinalizer). Ein fehlgeschlagener Teardown darf nicht den Fehler des Tests verschlucken (sonst hat man maskierte Fehler – der schlimmste Albtraum im CI/CD). 
>
> > Praktische Konsequenz für PyTest + Selenium:
> 
> >Setup: Initialisiert den Treiber, navigiert zur Basis-URL, lädt Testdaten.
> 
>> Teardown: Macht driver.quit() – und zwar immer, egal ob der Test grün oder rot ist. Sonst haben Sie nach 2 Stunden 500 offene Browser-Instanzen im Docker-Container.
> 
>> Tipp:
> Nutzen Sie PyTest-Fixtures mit Scope (function, class, session, module) – denn der Unterschied zwischen Setup/Teardown verwischt, wenn Sie über Session-vs.-Methoden-Lebenszyklus nachdenken. Ein session-Scoped Setup (z. B. einmaliger Browser-Start) und ein function-Scoped Teardown (z. B. Cookie-Löschung) sind oft die bessere Wahl als starre @Before/@After.
> 
> > "Setup/Teardown definieren die Test-Hygiene, der zentrale Driver definiert die Test-Ökonomie. Wer beides vermischt, baut sich eine Wartungshölle. Wer beides trennt, hat eine skalierbare, wartbare E2E-Strategie."


>  Warum wird der WebDriver zentral verwaltet?
> >
    

> Warum verwenden Sie eine BasePage?
> > Die BasePage kapselt gemeinsame Funktionalitäten aller Seiten, beispielsweise den Zugriff auf den WebDriver oder häufig verwendete Interaktionen. Dadurch vermeiden wir Code-Duplikate und schaffen eine zentrale Stelle für Änderungen.
   

> Warum übergeben Sie den WebDriver an den Konstruktor und erzeugen ihn nicht direkt in der Klasse?
> >  Der WebDriver wird bewusst von außen übergeben (Dependency Injection). Dadurch bleibt die Klasse unabhängig von der Browserinitialisierung und kann mit jeder bereits bestehenden Browserinstanz arbeiten. Das verbessert die Wiederverwendbarkeit, Testbarkeit und Trennung der Verantwortlichkeiten.
     

> Warum speichern Sie den Driver als Instanzattribut?
> > Der WebDriver wird als Instanzattribut gespeichert, damit alle Methoden des Page Objects dieselbe Browserinstanz verwenden können. Dadurch bleibt der Zustand des Browsers über die gesamte Lebensdauer des Objekts erhalten.
     

> Warum erbt HomePage von BasePage?
> > HomePage erbt von BasePage, um gemeinsame Funktionalitäten wie den Zugriff auf den WebDriver oder allgemeine Interaktionen mit der Benutzeroberfläche wiederzuverwenden. Dadurch vermeiden wir Code-Duplikate und halten die Architektur wartbar.
      

> Warum kapseln Sie den Seitenaufruf in einer Methode und rufen nicht direkt driver.get(...) im Test auf?
>> Im Page Object Model werden alle Interaktionen mit einer Seite innerhalb des jeweiligen Page Objects gekapselt. Dadurch bleiben die Tests fachlich lesbar und Änderungen an der Navigation müssen nur an einer zentralen Stelle vorgenommen werden.

> 
