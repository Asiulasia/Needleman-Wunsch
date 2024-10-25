sek1 = ""
sek2 = ""

with open("sekwencja1.fasta", "r") as sek_1:
    for line in sek_1.readlines():
        if line.startswith(">"):
            continue
        else:
            sek1 += line
sek1 = sek1.rstrip("\n")


with open("sekwencja2.fasta", "r") as sek_2:
    for line in sek_2.readlines():
        if line.startswith(">"):
            continue
        else:
            sek2 += line
sek2 = sek2.rstrip("\n")

m = len(sek1)   #liczba wierszy - Sekwencja1 po lewej
n = len(sek2)   #liczba kolumn - Sekwencja2 na gorze
mat = []   # macierz

match = 1
mismatch = -1
gap = -2

#uzupelnianie macierzy
for i in range(m+1):   #dodatkowa kolumna
    temp = []
    for j in range(n+1):   #dodatkowy wiersz
        temp.append(0)  #same zera
    mat.append(temp)

for j in range(n+1):   # uzupelniamy wartosciami
    mat[0][j] = gap*j

for i in range(m+1):
    mat[i][0] = gap*i


#uzupaleniamy macierz dopasowanie/niedopasowanie/gap
for i in range(1,m+1):
    for j in range(1, n+1):

        if sek1[i-1] == sek2[j-1]:
            mat[i][j] = max(mat[i][j-1]+gap, mat[i-1][j]+gap, mat[i-1][j-1]+match)

        else:
            mat[i][j] = max(mat[i][j-1]+gap, mat[i-1][j]+gap, mat[i-1][j-1]+mismatch)



for row in mat:
    for element in row:
        print(element, end="\t")
    print("\n")


#Backtracking
sek1_dopasowanie = ""
sek2_dopasowanie = ""

i = m
j = n


while i > 0 or j > 0:
    #jesli jest dopasowanie skocz do komorki na ukosie
    if sek1[i-1] == sek2[j-1]:
        sek1_dopasowanie += sek1[i-1]
        sek2_dopasowanie += sek2[j-1]
        i -= 1
        j -= 1

    #jesli nie ma dopasowania
    else:
        temp_list = [mat[i-1][j-1], mat[i-1][j], mat[i][j-1]]  #maksymalna z gory, ukosa, z lewej

        #sprawdzenie ktora byla wybrana maksymalna i uzupelnienie dopasowania do sekwencji
        if max(temp_list) == temp_list[0]:
            sek1_dopasowanie += sek1[i-1]
            sek2_dopasowanie += sek2[j-1]
            i -= 1
            j -= 1
        elif max(temp_list) == temp_list[1]:
            sek1_dopasowanie += sek1[i-1]
            sek2_dopasowanie += "-"
            i -= 1
        elif max(temp_list) == temp_list[-1]:
            sek1_dopasowanie += "-"
            sek2_dopasowanie += sek2[j-1]
            j-=1

sek1_dop = sek1_dopasowanie[::-1]
sek2_dop = sek2_dopasowanie[::-1]

#string pokazujacy dopasowanie/niedopasowanie/gapa
dopasowanie = ""
for i in range(len(sek1_dop)):
    if sek1_dop[i] == sek2_dop[i]:
        dopasowanie += "|"
    else:
        if (sek1_dop[i] == "-" or sek2_dop[i] == "-"):
            dopasowanie += " "
        else:
            dopasowanie += "*"

#liczenie score
score = 0
for i in range(len(dopasowanie)):
    if dopasowanie[i] == "|":
        score += 1
    elif (dopasowanie[i] == "*" or dopasowanie[i] == " "):
        score += -1

print(sek1_dop)
print(dopasowanie)
print(sek2_dop, "\n")
print("Score:", score)