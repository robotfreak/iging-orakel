﻿import random
import openai
import textwrap
import os
import sys
import PySimpleGUI as sg

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
    ("䷵", "Fêng - Die Entwicklung"),
    ("䷶", "Lü - Die Erschöpfung"),
    ("䷷", "Ting - Der Übergang"),
    ("䷸", "Chien - Die Sorge"),
    ("䷹", "Chun - Die Lösen"),
    ("䷺", "Hsiao Kuo - Das Halten"),
    ("䷻", "Ku - Die Geistesgegenwart"),
    ("䷼", "Hsü - Die Hemmung"),
    ("䷽", "Chien - Die Unmäßigkeit"),
    ("䷾", "Sun - Die Innigkeit"),
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

def main():
    input_width=80
    hexagram1 = []
    hexagram2 = []

    sg.theme('DarkAmber')

    layout = [[sg.Text('Stelle deine Frage an das Orakel und drücke \'Start\':')],
              [sg.InputText(size=(input_width, 1), enable_events=True, key='-IN-')],
              [sg.Text('Die Anwort des \'I Ging\' Orakels:')],
              [sg.Text('1. Hexagramm:', size=(40,1)), sg.Text('2. Hexagramm:', size=(40,1))],
              [sg.Text("", size=(6, 1), font='Default 78', key='OUTPUT1'),
               sg.Text("", size=(6, 1), font='Default 78', key='OUTPUT2')],
              [sg.Text("", size=(40,1), key='REMARK1'), sg.Text("", size=(40,1), key='REMARK2')],
              [sg.Button('Start')],
              [sg.Text('Drücke \'Submit\' für eine Interpretation von ChatGPT:')],
              [sg.Multiline("", size=(80,30), key='ANSWER')],
              [sg.Submit(), sg.Cancel()]]

    window = sg.Window('ChatGPT \'I Ging\' Orakel', layout)

    while True:  # Event Loop
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        elif event == '-IN-':
            question = values['-IN-'] 
        elif event in ('Start'):
            # generate the i ging hexagrams
            print(question)
            [hexagram_idx1, hexagram1] = randomHexagram() 
            [hexagram_idx2, hexagram2] = randomHexagram() 
            print(hexagram_idx1+1, hexagram1[0], hexagram1[1])
            print(hexagram_idx2+1, hexagram2[0], hexagram2[1])
            window['OUTPUT1'].update(value=hexagram1[0])
            window['OUTPUT2'].update(value=hexagram2[0])
            window['REMARK1'].update(value=hexagram1[1])
            window['REMARK2'].update(value=hexagram2[1])
        elif event in ('Submit'):
            chat = "Wie ist die Antwort Hexagramm " + str(hexagram_idx1+1) + " und " + str(hexagram_idx2+1) + " des I Ging Orakels auf die Frage '" + question + "' zu interpretieren?"
            wrapper = textwrap.TextWrapper(width=70, replace_whitespace=False)
            string = wrapper.fill(text=chat)
            print (string + "\n")   

            # ask ChatGpt and print th resault 
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
            answer = wrapper.fill(text=reply)
            print (answer)   
            window['ANSWER'].update(value=answer)


    window.close()

# Aufruf der Funktion
main()
#iging_oracle()
