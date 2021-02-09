# Theorie Software Design

### 1. Frage
*Sie beginnen als EntwicklerIn in einem neuen Unternehmen und bekommen die Verantwortung für ein Modul. Das Modul ist über eine lange Zeit hinweg gewachsen und besteht nur aus sehr wenigen Klassen. Die Methoden dieser Klassen sind meist sehr lange, oftmals einige hundert Zeilen oder länger, und sie sind auch eher spärlich dokumentiert. Was für Nachteile ergeben sich für Sie durch diesen Code? Welche grundlegenden Software Design Prinzipien werden evtl. nicht eingehalten?*


**Antwort:**

Um gute Software zu beschreiben, gibt es einige sog. Design Prinzipien, deren Erfüllung die Qualität des Programmcodes erhöht. Im Bereich des objektorientierten Software-Designs kann beispielsweise nach den 5 sog. SOLID-Prinzipien gearbeitet werden. Im vorliegenden Beispiel wird es uns erschwert, den Code in angemessener Weise zu warten – Änderungen und Fehlerkorrekturen, auch die Erweiterung des Codes wird uns durch seine Unübersichtlichkeit und fehlende Dokumentation erschwert. Dadurch ergeben sich für uns große Probleme beim Verstehen des Codes. Ein zentrales Prinzip des Software Designs ist das sog. ***KISS** – Keep it simple and stupid/small*. In diesem Fall könnte man von einer Verletzung dieses grundlegenden Prinzips sprechen.
Wichtig ist, dass stets auch eine geeignete und ausreichende Dokumentation zum Code geschrieben wird, damit dieser auch in weiterer Folge von anderen Personen verwendet und verstanden werden kann. 

---

### 2. Frage
*Für die vollständige Überarbeitung/Neuschreiben bleibt Ihnen keine Zeit, da sie ihr/e Vorgesetze/r schon mit der Umsetzung des nächsten Features beauftragt hat. Wie würden Sie bei der Umsetzung vorgehen?*


**Antwort:**

Da der Code ja soweit läuft, versuchen wir die nächsten Features so gut als möglich darin zu implementieren unter Berücksichtigung der grundlegenden Software-Design-Prinzipien. Im Allgemeinen streben wir aber eine Refaktorisierung an, d.h. eine Änderung der internen Struktur, ohne das externe Verhalten zu verbessern. Mithilfe der Refaktorisierung kann der Code übersichtlicher und entsprechend der Design-Prinzipien angepasst werden. Für den Refaktorisierungsprozess muss allerdings mehr Zeit eingeplant werden, da genau getestet und überprüft werden muss, ob die Refaktorisierung erfolgreich umgesetzt wurde. Diesen Schritt würden wir also erst nach der vorläufigen Implementierung des entsprechend benötigten Features angehen.
