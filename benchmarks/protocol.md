# Protocol de Benchmark

- Mesures réalisées avec le module Python `time`.
- Tests répétés sur 10 000 entiers.
- Valeurs de tests : valeurs stockées entre 0 et 127, + quelques grands entiers (overflow).
- Chaque méthode (compression, décompression, accès direct) est chronométrée séparément pour chaque version.
- On compare BitPackingClassic, BitPackingStrict et Overflow.
- Résultats affichés en secondes pour chaque opération sur une boucle de 1000 accès.
