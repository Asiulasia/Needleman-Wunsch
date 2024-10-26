# Algorytm dopasowania globalnego sekwencji - Needleman-Wunsch

## Opis

Ten program implementuje algorytm Needleman-Wunscha do dopasowywania dw�ch sekwencji nukleotydowych. Algorytm ten pozwala znale�� optymalne globalne dopasowanie mi�dzy dwoma sekwencjami, wykorzystuj�c macierz wynik�w i procedur� backtrackingu.

## Spos�b uzycia

Aby uruchomi� program, za�aduj do pliku para_sek.fasta dwie sekwencje, kt�rych dopasowanie chcesz znale��.
Nale�y wprowadzi� sekwencje aminokwasowe do pliku tylko w formacie FASTA.
Plik para_sek.fasta powinien by� sformatowany tak, aby ka�da sekwencja by�a poprzedzona lini� zaczynaj�c� si� od >, na przyk�ad:
#> Sequence 1
#GATTACA
#> Sequence 2
#GTCGACGCA

Po zako�czeniu dzia�ania programu zostanie zapisany plik wynikowy wynik.txt z przyk�adow� zawarto�ci�:
GATTA--CAG
|***|  ||*
GTCGACGCAT
Score:-2
