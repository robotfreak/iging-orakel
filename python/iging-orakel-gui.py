import random
import openai
import textwrap
import os
import sys
import PySimpleGUI as sg
from PIL import Image, ImageTk

openai.api_key = os.getenv('OPENAI_API_KEY')

filename = "pakua.png"
# Resize PNG file to size (100, 100)
size = (150, 150)
im = Image.open(filename)
im = im.resize(size, resample=Image.BICUBIC)

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
    ("䷂", "Chun - Die Anfangsschwierigkeit"),
    ("䷃", "Mêng - Die Jugendtorheit"),
    ("䷄", "Hsü - Das Warten"),
    ("䷅", "Sung - Der Streit"),
    ("䷆", "Shih - Das Heer"),
    ("䷇", "Pi - Das Zusammenhalten"),
    ("䷈", "Hsiao Ch'u - Des Kleinen Zähmungskraft"),
    ("䷉", "Lü - Das Auftreten"),
    ("䷊", "T'ai - Der Friede"),
    ("䷋", "P'i - Die Stockung"),
    ("䷌", "T'ung Jên - Die Gemeinschaft mit Menschen"),
    ("䷍", "Ta Yu - Der Besitz von Großem"),
    ("䷎", "Ch'ien - Die Bescheidenheit"),
    ("䷏", "Yü - Die Begeisterung"),
    ("䷐", "Sui - Die Nachfolge"),
    ("䷑", "Ku - Die Arbeit am Verdorbenen"),
    ("䷒", "Lin - Die Annäherung"),
    ("䷓", "Huan - Die Betrachteung"),
    ("䷔", "Shih Ho - Das Durchbeißen"),
    ("䷕", "Pi - Die Anmut"),
    ("䷖", "Po - Die Zersplitterung"),
    ("䷗", "Fu - Die Wendezeit"),
    ("䷘", "Wu Wang - Die Unschuld"),
    ("䷙", "Ta Ch'u - Des Großen Zähmungskraf"),
    ("䷚", "I - Die Ernährung"),
    ("䷛", "Ta Kuo - Des Großen Übergewicht"),
    ("䷜", "K'an - Das Abgründige"),
    ("䷝", "Li - Das Feuer"),
    ("䷞", "Hsien - Die Einwirkung"),
    ("䷟", "Hêng - Die Dauer"),
    ("䷠", "Tun - Der Rückzug"),
    ("䷡", "Ta Chuang - Des Großen Macht"),
    ("䷢", "Chin - Der Fortschritt"),
    ("䷣", "Ming I - Die Verfinsterung des Lichts"),
    ("䷤", "Jia Ren - Die Sippe"),
    ("䷥", "K'uei - Der Gegensatz"),
    ("䷦", "Jian - Das Hemmnis"),
    ("䷧", "Xie - Die Befreiung"),
    ("䷨", "Sun - Die Minderung"),
    ("䷩", "Yi - Die Mehrung"),
    ("䷪", "Kuei - Der Durchbruch"),
    ("䷫", "Gou - Das Entgegenkommen"),
    ("䷬", "Cui - Die Sammlung"),
    ("䷭", "Sheng - Das Empordringen"),
    ("䷮", "Kun - Die Bedrängnis"),
    ("䷯", "Jing - Der Brunnen"),
    ("䷰", "Ge - Die Umwälzung"),
    ("䷱", "Ding - Der Tiegel"),
    ("䷲", "Zhen - Das Erregende"),
    ("䷳", "Gen - Das Stillehalten"),
    ("䷴", "Jian - Die Entwicklung"),
    ("䷵", "Gui Mei - Das heiratende Mädchen"),
    ("䷶", "Feng - Die Fülle"),
    ("䷷", "Lu - Der Wanderer"),
    ("䷸", "Xun - Das Sanfte"),
    ("䷹", "Dui - Das Heitere"),
    ("䷺", "Huan - Die Auflösung"),
    ("䷻", "Jie - Die Beschränkung"),
    ("䷼", "Zhong Fu - Innere Wahrheit"),
    ("䷽", "Xiao Guo - Des Kleinen Übergewicht"),
    ("䷾", "Ji Ji - Nach der Vollendung"),
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


def iging_oracle_cli():

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

def iging_oracle_gui():
    input_width=80
    hexagram1 = []
    hexagram2 = []

    sg.theme('DarkAmber')

    layout = [[sg.Text('Stelle deine Frage an das Orakel und drücke danach den \'Orakel\' Button:')],
              [sg.InputText(size=(input_width, 1), font='Default 18', enable_events=True, key='-IN-')],
              [sg.Button('Orakel')],
              [sg.Text('Die Anwort des \'I Ging\' Orakels:')],
              [sg.Text('1. Hexagramm:', size=(50,1)), sg.Text('2. Hexagramm:', size=(50,1))],
              [sg.Text("", size=(6, 1), font='Default 96', key='OUTPUT1'),
               sg.Text("", size=(4, 1), font='Default 96', key='OUTPUT2'),
               sg.Image(size=(150,150), key='-IMAGE-')],
              [sg.Text("", size=(50,1), key='REMARK1'), sg.Text("", size=(50,1), key='REMARK2')],
              [sg.Text('Für eine Deutung durch ChatGPT drücke den \'ChatGPT\' Button:')],
              [sg.Button('ChatGPT')],
              [sg.Multiline("", size=(120,28), font='Default 18', key='ANSWER')],
              [sg.Button('Neu')]]

    window = sg.Window('ChatGPT \'I Ging\' Orakel', layout, finalize=True)
    # Convert im to ImageTk.PhotoImage after window finalized
    image = ImageTk.PhotoImage(image=im)

    # update image in sg.Image
    window['-IMAGE-'].update(data=image)

    while True:  # Event Loop
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        elif event == '-IN-':
            question = values['-IN-'] 
        elif event in ('Orakel'):
            # generate the i ging hexagrams
            if (question != ""):
                print(question)
                [hexagram_idx1, hexagram1] = randomHexagram() 
                [hexagram_idx2, hexagram2] = randomHexagram() 
                print(hexagram_idx1+1, hexagram1[0], hexagram1[1])
                print(hexagram_idx2+1, hexagram2[0], hexagram2[1])
                window['OUTPUT1'].update(value=hexagram1[0])
                window['OUTPUT2'].update(value=hexagram2[0])
                window['REMARK1'].update(value=hexagram1[1])
                window['REMARK2'].update(value=hexagram2[1])
        elif event in ('ChatGPT'):
            if (question != ""):
                chat = "Wie ist die Antwort Hexagramm " + str(hexagram_idx1+1) + " und " + str(hexagram_idx2+1) + " des I Ging Orakels auf die Frage '" + question + "' zu interpretieren?"
                wrapper = textwrap.TextWrapper(width=70, replace_whitespace=False)
                string = wrapper.fill(text=chat)
                print (string + "\n")   

                # ask ChatGpt and print th resault 
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
        elif event in ('Neu'):
            question = ""
            answer = ""
            window['-IN-'].update(value=answer)
            window['ANSWER'].update(value=answer)
            window['OUTPUT1'].update(value=answer)
            window['OUTPUT2'].update(value=answer)
            window['REMARK1'].update(value=answer)
            window['REMARK2'].update(value=answer)


    window.close()

# Aufruf der Funktion
iging_oracle_gui()
#iging_oracle_cli()
