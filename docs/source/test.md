# 4-Gewinnt - Tests

Getestet wurde auf Basis der 4 Klassen **Player**, **GUI**, **Field** und **RuleSet**.
Als erstes haben wir einen Test geschrieben, der die Eingabe des Spielmodus überprüft - korrekt sind nur die Eingaben 1 (für Mensch) und 2 (für Computer). Andere Eingaben beschwören eine Fehlermeldung. Weiters haben wir die Funktion für das Spielfeld getestet, d.h. ob die Spielsteine korrekt gesetzt werden. Bei der **RuleSet**-Klasse haben wir v.a. getestet, ob ein Zug möglich bzw. nicht möglich ist. Der Test für die Funktion *checkGameOver* überprüft, ob noch freie Felder auf dem Spielfeld vorhanden sind und liefert *True* oder *False* zurück. Auch die Funktionen, die überprüfen, ob einer der Spieler gewonnen hat, d.h. ob jemand 4 Steine in einer Reihe (horizontal, vertikal, diagonal) hat, wurden getestet, da es sich hier um ganz zentrale Funktionen unseres Spiels handeln. 
Grundsätzlich haben wir versucht, alle (relevanten) Funktionen zu testen. Die Klasse **FourWinsGame** wurde dabei ausgespart, weil sie lediglich zur Erstellung des Spiels dient.

Mehr Informationen zu den Tests befinden sich in der Dokumentation in der Test-Datei (*viergewinnt_tests.py*)!
