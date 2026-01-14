# DatZM024 Programmēšanas uzdevums

## Algoritma apraksts

Uzdevuma risinājumā izmantots Union-Find algoritms, kas no dotā grafa ģenerē mežu - 1 vai vairākus nesakarīgus kokus bez cikliem. [1]

Ja atrodam visas šķautnes, kas pieder šim mežam, un tad pievienojam kādu no pārējām šķautnēm, izveidosies cikls. Tātad mežam nepiederošās šķautnes piederēs visiem dotā grafa cikliem, kas izpilda uzdevuma 1. nosacījumu (katrā ciklā ir vismaz viens celiņš ar koka dobumu, kurā ir medus krājumi).

Ja mums izdodas atrast mežu, kuram piederošo šķautņu grūtības pakāpju summa ir maksimālā iespējamā (vispirms dotās šķautnes sakārtojot pēc to grūtības pakāpēm), tad mežam nepiederošās šķautnes būs ar minimālo iespējamo grūtības pakāpju summu, tādējādi izpildot 2. nosacījumu.

## Sarežģītības novērtējums

grafam ar n virsotnēm un m šķautnēm
- Ievades faila nolasīšana: O(m)
- Šķautņu sakārtošana: O(m log m) (izmantojot Python iebūvēto sort() metodi, kas izmanto Timsort algoritmu) [2][3]
- Meža ģenerēšana ar Union-Find algoritmu: O(m*α(n)) (kur α(n) ir ļoti lēni augošā inversā Akermana funkcija) [4]
- Kopējās grūtības aprēķināšana: O(1)
- Rakstīšana izvades failā: O(m)

Visaugstākā sarežģītība ir šķautņu saraksta sakārtošanas solī, kas risinājuma kopējo sarežģītību padara **O(m log m)**.

***
## Avoti:

[1] GeeksforGeeks - Introduction to Disjoint Set (Union-Find Data Structure) (2025-07-24)

https://www.geeksforgeeks.org/dsa/introduction-to-disjoint-set-data-structure-or-union-find-algorithm/

[2] Python Documentation - Sorting Techniques

https://docs.python.org/3/howto/sorting.html

[3] Wikipedia - Timsort

https://en.wikipedia.org/wiki/Timsort

[4] Wikipedia - Disjoint-set data structure

https://en.wikipedia.org/wiki/Disjoint-set_data_structure
