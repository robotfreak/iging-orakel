﻿import random


def iging_oracle():
    # Liste der Bilder mit Unicode-Zeichen
    pictures = [
        ("⚌", "tai yang - altes Yang (Luft)"),
        ("⚍", "shao yang - junges Yang (Feuer)"),
        ("⚎", "shao yin - junges Yin (Wasser)"),
        ("⚏", "tai yin - altes Yin (Erde)")
    ]

    # Liste der Trigramme mit Unicode-Zeichen
    trigrams = [
        ("☰", "Qian - Der Himmel"),
        ("☱", "Dui - Der See"),
        ("☲", "Li - Das Feuer"),
        ("☳", "Zhen - Der Donner"),
        ("☴", "Xun - Der Wind"),
        ("☵", "Kan - Das Wasser"),
        ("☶", "Gen - Der Berg"),
        ("☷", "Kun - Die Erde")
    ]


    # Liste der Hexagramme mit Unicode-Zeichen
    hexagrams = [
        ("䷀", "Ch'ien - Das Schöpferische"),
        ("䷁", "K'un - Das Empfangende"),
        ("䷂", "Chun - Das Anregende"),
        ("䷃", "Mêng - Die Jugendtorheit"),
        ("䷄", "Hsü - Das Warten"),
        ("䷅", "Sung - Der Streit"),
        ("䷆", "Shih - Das Heer"),
        ("䷇", "Pi - Das Zusammenhalten"),
        ("䷈", "Hsiao Ch'u - Das kleine Übergewicht"),
        ("䷉", "Lü - Das Verhalten"),
        ("䷊", "T'ai - Der Friede"),
        ("䷋", "P'i - Das Hindernis"),
        ("䷌", "T'ung Jên - Die Gemeinschaft mit Menschen"),
        ("䷍", "Ta Yu - Das Große Übergewicht"),
        ("䷎", "Ch'ien - Die Bescheidenheit"),
        ("䷏", "Yü - Das Begeisternde"),
        ("䷐", "Sui - Das Nachfolgende"),
        ("䷑", "Ku - Das Verderben"),
        ("䷒", "Lin - Der Annähernde"),
        ("䷓", "Huan - Das Betrachtende"),
        ("䷔", "Shih Ho - Das Beißen"),
        ("䷕", "Pi - Die Menge"),
        ("䷖", "Po - Das Abscheuliche"),
        ("䷗", "Po - Das Zurückschreckende"),
        ("䷘", "Fu - Die Wiederkehr"),
        ("䷙", "Wu Wang - Das Unschuldige"),
        ("䷚", "Ta Ch'u - Das Große Übergewicht"),
        ("䷛", "I - Das Nährende"),
        ("䷜", "Ta Kuo - Das Übergewicht des Großen"),
        ("䷝", "K'an - Das Abgründige"),
        ("䷞", "Li - Das Leitende"),
        ("䷟", "Hsien - Das Reifen"),
        ("䷠", "Hêng - Der Einfluss"),
        ("䷡", "Tun - Der Rückgang"),
        ("䷢", "Ta Chuang - Das Übergewicht des Großen"),
        ("䷣", "Chin - Das Hemmende"),
        ("䷤", "Mêng - Die Verwirrung"),
        ("䷥", "K'uei - Das Abziehende"),
        ("䷦", "Chien - Die Erschöpfung"),
        ("䷧", "Hsiao Kuo - Das kleine Übergewicht"),
        ("䷨", "Ku - Die Befreiung"),
        ("䷩", "Chia Jên - Die Verbindung mit Menschen"),
        ("䷪", "Kuei Mei - Das Sammeln"),
        ("䷫", "Fêng - Das Erregende"),
        ("䷬", "Lü - Das Karge"),
        ("䷭", "Ting - Der Ruin"),
        ("䷮", "Chien - Das Verdrängte"),
        ("䷯", "Hsiao Ch'u - Das Kreative"),
        ("䷰", "Hêng - Das Beharrliche"),
        ("䷱", "Chung Fu - Die Innere Wahrheit"),
        ("䷲", "Hsiao Kuo - Das Kühne"),
        ("䷳", "Chia Jên - Das Einengende"),
        ("䷴", "Kuei Mei - Die Beharrlichkeit"),
        ("䷵", "Fêng - Die Entwickelung"),
        ("䷶", "Lü - Die Erschöpfung"),
        ("䷷", "Ting - Der Übergang"),
        ("䷸", "Chien - Die Sorge"),
        ("䷹", "Chun - Die Lösen"),
        ("䷺", "Hsiao Kuo - Das Halten"),
        ("䷻", "Ku - Die Geistesgegenwart"),
        ("䷼", "Hsü - Die Hemmung"),
        ("䷽", "Chien - Die Unmäßigkeit"),
        ("䷾", "Sun - Die Innigkeit")
    ]

    # Zufällige Auswahl eines Bilds
    picure_idx = random.randint(0,3)
    picture = pictures[picure_idx]
    # picture = random.choice(pictures)


    # Zufällige Auswahl eines Trigramms
    trigram_idx = random.randint(0,7)
    trigram = trigrams[trigram_idx]
    # trigram = random.choice(trigrams)


    # Zufällige Auswahl eines Hexagramms
    hexagram_idx1 = random.randint(0,63)
    hexagram1 = hexagrams[hexagram_idx1]

    hexagram_idx2 = random.randint(0,63)
    hexagram2 = hexagrams[hexagram_idx2]
    # hexagram = random.choice(hexagrams)


    # Ausgabe der Trigramme und des Hexagramms als Unicode-Zeichen
    print("Dein Bild ist: ")
    print(picure_idx, picture[0], picture[1])
    print("\n")
    print("Dein Trigramm ist: ")
    print(trigram_idx, trigram[0], trigram[1])
    print("\n")
    print("Dein 1. Hexagramm ist: ")
    print(hexagram_idx1, hexagram1[0], hexagram1[1])
    print("Dein 2. Hexagramm ist: ")
    print(hexagram_idx2, hexagram2[0], hexagram2[1])




# Aufruf der Funktion
iging_oracle()