import random
import openai
import textwrap
import os
import sys

openai.api_key = os.getenv('OPENAI_API_KEY')

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
    ("䷀", "Ch'ien - Das Schöpferische"),                   # 1
    ("䷁", "K'un - Das Empfangende"),                       # 2
    ("䷂", "Chun - Das Anregende"),                         # 3
    ("䷃", "Mêng - Die Jugendtorheit"),                     # 4
    ("䷄", "Hsü - Das Warten"),                             # 5
    ("䷅", "Sung - Der Streit"),                            # 6
    ("䷆", "Shih - Das Heer"),                              # 7
    ("䷇", "Pi - Das Zusammenhalten"),                      # 8
    ("䷈", "Hsiao Ch'u - Das kleine Übergewicht"),          # 9
    ("䷉", "Lü - Das Verhalten"),                           # 10
    ("䷊", "T'ai - Der Friede"),                            # 11
    ("䷋", "P'i - Das Hindernis"),                          # 12
    ("䷌", "T'ung Jên - Die Gemeinschaft mit Menschen"),    # 13
    ("䷍", "Ta Yu - Das Große Übergewicht"),                # 14
    ("䷎", "Ch'ien - Die Bescheidenheit"),                  # 15
    ("䷏", "Yü - Das Begeisternde"),                        # 16
    ("䷐", "Sui - Das Nachfolgende"),                       # 17
    ("䷑", "Ku - Das Verderben"),                           # 18
    ("䷒", "Lin - Der Annähernde"),                         # 19
    ("䷓", "Huan - Das Betrachtende"),                      # 20
    ("䷔", "Shih Ho - Das Beißen"),                         # 21
    ("䷕", "Pi - Die Menge"),                               # 22
    ("䷖", "Po - Das Abscheuliche"),                        # 23
    ("䷗", "Po - Das Zurückschreckende"),                   # 24
    ("䷘", "Fu - Die Wiederkehr"),                          # 25    
    ("䷙", "Wu Wang - Das Unschuldige"),                    # 25 --
    ("䷚", "Ta Ch'u - Das Große Übergewicht"),              # 26
    ("䷛", "I - Das Nährende"),                             # 27
    ("䷜", "Ta Kuo - Das Übergewicht des Großen"),          # 28
    ("䷝", "K'an - Das Abgründige"),                        # 29
    ("䷞", "Li - Das Leitende"),                            # 30  
    ("䷟", "Hsien - Das Reifen"),                           # 31
    ("䷠", "Hêng - Der Einfluss"),                          # 32
    ("䷡", "Tun - Der Rückgang"),                           # 33
    ("䷢", "Ta Chuang - Das Übergewicht des Großen"),       # 34
    ("䷣", "Chin - Das Hemmende"),                          # 35
    ("䷤", "Mêng - Die Verwirrung"),                        # 36
    ("䷥", "K'uei - Das Abziehende"),                       # 37
    ("䷦", "Chien - Die Erschöpfung"),                      # 38
    ("䷧", "Hsiao Kuo - Das kleine Übergewicht"),           # 39
    ("䷨", "Ku - Die Befreiung"),                           # 40
    ("䷩", "Chia Jên - Die Verbindung mit Menschen"),       # 41
    ("䷪", "Kuei Mei - Das Sammeln"),                       # 42
    ("䷫", "Fêng - Das Erregende"),                         # 43
    ("䷬", "Lü - Das Karge"),                               # 44
    ("䷭", "Ting - Der Ruin"),                              # 45
    ("䷮", "Chien - Das Verdrängte"),                       # 46
    ("䷯", "Hsiao Ch'u - Das Kreative"),                    # 47
    ("䷰", "Hêng - Das Beharrliche"),                       # 48          
    ("䷱", "Chung Fu - Die Innere Wahrheit"),               # 49   
    ("䷲", "Hsiao Kuo - Das Kühne"),                        # 50
    ("䷳", "Chia Jên - Das Einengende"),                    # 51
    ("䷴", "Kuei Mei - Die Beharrlichkeit"),                # 52
    ("䷵", "Fêng - Die Entwicklung"),                       # 53
    ("䷶", "Lü - Die Erschöpfung"),                         # 54
    ("䷷", "Ting - Der Übergang"),                          # 55
    ("䷸", "Chien - Die Sorge"),                            # 56
    ("䷹", "Chun - Die Lösen"),                             # 57
    ("䷺", "Hsiao Kuo - Das Halten"),                       # 58
    ("䷻", "Ku - Die Geistesgegenwart"),                    # 59
    ("䷼", "Hsü - Die Hemmung"),                            # 60
    ("䷽", "Chien - Die Unmäßigkeit"),                      # 61
    ("䷾", "Sun - Die Innigkeit"),                           # 62
    ("䷿", "Wei Ji - Vor der Vollendung")                           # 62
]


def randomHexagram(): 
    # Zufällige Auswahl eines Hexagramms
    hexagram_idx = random.randint(0,63)
    hexagram = hexagrams[hexagram_idx]
    # hexagram = random.choice(hexagrams)
    return hexagram_idx, hexagram

def randowTrigram():
    # Zufällige Auswahl eines Trigramms
    trigram_idx = random.randint(0,7)
    trigram = trigrams[trigram_idx]
    # trigram = random.choice(trigrams)
    return trigram_idx, trigram

def randomPicture():
    # Zufällige Auswahl eines Bilds
    picure_idx = random.randint(0,3)
    picture = pictures[picure_idx]
    # picture = random.choice(pictures)
    return picure_idx, picture


def iging_oracle():

    # read string from user
    print("> Gib deine Frage ein: ")
    res = sys.stdin.readline()  # used in place of input()
    question = res.strip()
    #question = input('> Enter your Question: ')
    print(question)

    # generate the i ging hexagrams
    [hexagram_idx1, hexagram1] = randomHexagram() 
    [hexagram_idx2, hexagram2] = randomHexagram() 
    # show the i ging hexagrams
    print("\nDie Antwort des Orakels:")
    print("Dein 1. Hexagramm ist: ")
    print(hexagram_idx1, hexagram1[0], hexagram1[1])
    print("Dein 2. Hexagramm ist: ")
    print(hexagram_idx2, hexagram2[0], hexagram2[1])

    # ask chatgpt for the interpretation of the hexagrams to the specific question
    print("\nDie Interpretation von ChatGPT:")
    chat = "Wie ist die Antwort Hexagramm " + str(hexagram_idx1) + " und " + str(hexagram_idx2) + " des I Ging Orakels auf die Frage '" + question + "' zu interpretieren?"
    wrapper = textwrap.TextWrapper(width=70, replace_whitespace=False)
    string = wrapper.fill(text=chat)
    print (string + "\n")   

    # TODO: ask ChatGpt and print th resault 
    messages = [ {"role": "user", "content": 
              "Wie ist die Antwort des I Ging Orakel Hexagramm " + str(hexagram_idx1) + " und " + str(hexagram_idx2) + " auf die Frage '" + question + "' zu interpretieren?"} ]
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": chat}],
        temperature=1,
        max_tokens=641,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    reply = response.choices[0].message.content
    wrapper = textwrap.TextWrapper(width=70, replace_whitespace=False)
    string = wrapper.fill(text=reply)
    print (string)   

# Aufruf der Funktion
iging_oracle()
