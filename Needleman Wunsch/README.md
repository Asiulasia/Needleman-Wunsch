# Algorytm dopasowania globalnego sekwencji - Needleman-Wunsch

## Opis

Ten program implementuje algorytm Needleman-Wunsch do dopasowywania dwóch sekwencji nukleotydowych. 
Algorytm ten pozwala znaleŸæ optymalne globalne dopasowanie miêdzy dwoma sekwencjami, wykorzystuj¹c macierz wyników i procedurê backtrackingu.

## Sposób uŸycia

Aby uruchomiæ program, za³aduj do pliku para_sek.fasta dwie sekwencje, których dopasowanie chcesz znaleŸæ.
Nale¿y wprowadziæ sekwencje aminokwasowe do pliku tylko w formacie FASTA.
Plik para_sek.fasta powinien byæ sformatowany tak, aby ka¿da sekwencja by³a poprzedzona lini¹ zaczynaj¹c¹ siê od >, na przyk³ad:

```plaintext 
> Sequence 1
GATTACA
> Sequence 2
GTCGACGCA

Po zakoñczeniu dzia³ania programu zostanie zapisany plik wynikowy wynik.txt z przyk³adow¹ zawartoœci¹:
GATTA--CAG
|***|  ||*
GTCGACGCAT
Score:-2
