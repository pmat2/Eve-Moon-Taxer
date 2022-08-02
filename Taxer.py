import tkinter as tk

header = """
/********************\\
    Moon Taxer
    Author: Zonnie
    v0.1
\\********************/
"""

r4_l = ['Hydrocarbons', 'Atmospheric Gases', 'Evaporite Deposits', 'Silicates']
r8_l = ['Cobalt', 'Scandium', 'Tungsten', 'Titanium']
r16_l = ['Chromium', 'Cadmium', 'Platinum', 'Vanadium']
r32_l = ['Technetium', 'Mercury', 'Caesium', 'Hafnium']
r64_l = ['Promethium', 'Neodymium', 'Dysprosium', 'Thulium']

r4 = {}
r8 = {}
r16 = {}
r32 = {}
r64 = {}

r4_tax = 0
r8_tax = 10
r16_tax = 20
r32_tax = 25
r64_tax = 35

characters = []
char_labels = []
values = []
raw = {}


padx = pady = 10

root = tk.Tk()
root.title("Moon taxer")

# support var for grid placement
global row_num
row_num = 3

def add_character_action():
    if(     character_entry.get() not in characters
        and character_entry.get() != ''
        and character_entry.get() != None):

        characters.append(character_entry.get())
        global row_num
        char_label = tk.Label(root, text=character_entry.get())
        char_label.grid(row=row_num, column=0, padx=padx, sticky='W')
        char_labels.append(char_label)
        row_num = row_num + 1
        character_entry.delete(0, 'end')

def remove_characters():
    for label in char_labels:
        label.grid_remove()
    characters.clear()

def after_tax(val, tax):
    return str(int(val) * (100 - tax) / 100)

def tax(val, tax):
    return str(int(val) * tax / 100)

def message_characters():
    message = 'Characters:\n'
    for char in characters:
        message = message + '- ' + char + '\n'
    message = message + '\n'
    return message

def parse_data(r4, r8, r16, r32, r64):
    message = message_characters()
    message = message + 'Name\tTotal\tNet\tTax\nr4 - no tax\n'
    for elem in r4.keys():
        message = message + elem + '\t' + r4.get(elem) + '\n'
    message = message + '\nr8 - ' + str(r8_tax) + '%\n'
    for elem in r8.keys():
        message = message   + elem + '\t' + r8.get(elem) + '\t' + after_tax(r8.get(elem), r8_tax) + '\t' + tax(r8.get(elem), r8_tax) + '\n'
    message = message + '\nr16 - ' + str(r16_tax) + '%\n'
    for elem in r16.keys():
        message = message   + elem + '\t' + r16.get(elem) + '\t' + after_tax(r16.get(elem), r16_tax) + '\t' + tax(r16.get(elem), r16_tax) + '\n'
    message = message + '\nr32 - ' + str(r32_tax) + '%\n'
    for elem in r32.keys():
        message = message   + elem + '\t' + r32.get(elem) + '\t' + after_tax(r32.get(elem), r32_tax) + '\t' + tax(r32.get(elem), r32_tax) + '\n'
    message = message + '\nr64 - ' + str(r64_tax) + '%\n'
    for elem in r64.keys():
        message = message   + elem + '\t' + r64.get(elem) + '\t' + after_tax(r64.get(elem), r64_tax) + '\t' + tax(r64.get(elem), r64_tax) + '\n'
    print(message)
    return message

def submit_action():
    if(len(characters) > 0):
        clip = tk.Tk()
        clip.withdraw()
        clipboard = clip.clipboard_get().split('\n')
        for elem in clipboard:
            values.append(elem)

        for elem in values:
            raw_elem = elem.split('\t')
            if(raw_elem[0] in r4_l):
                r4[raw_elem[0]] = raw_elem[1]
            elif(raw_elem[0] in r8_l):
                r8[raw_elem[0]] = raw_elem[1]
            elif(raw_elem[0] in r16_l):
                r16[raw_elem[0]] = raw_elem[1]
            elif(raw_elem[0] in r32_l):
                r32[raw_elem[0]] = raw_elem[1]
            elif(raw_elem[0] in r64_l):
                r64[raw_elem[0]] = raw_elem[1]
        result = tk.Tk()
        result.withdraw()
        result_message = parse_data(r4, r8, r16, r32, r64)
        result.clipboard_append(result_message)

        message = tk.Tk()
        msg = tk.Label(message, text='Parsed message copied to clipboard. Contact Zixie\n\n', width=50, height=20)
        msg.pack()

# tk objects
character_entry = tk.Entry(root, borderwidth=5, width=33)
add_character_button = tk.Button(root, text='Add character', command=add_character_action)
remove_characters_button = tk.Button(root, text='Clear characters', command=remove_characters)
characters_header = tk.Label(root, text='Characters')
submit_button = tk.Button(root, text='Submit', command=submit_action)

# tk grid
characters_header.grid(row=0, column=0, padx=padx, pady=pady, columnspan=2)
character_entry.grid(row=1, column=0, columnspan=5, padx=padx, pady=pady, sticky='W')
add_character_button.grid(row=2, column=0, padx=padx)
remove_characters_button.grid(row=2, column=1, sticky='E', padx=padx, pady=pady)
submit_button.grid(row=100, column=0, columnspan=2, padx=padx, pady=pady)

print(header)
root.mainloop()