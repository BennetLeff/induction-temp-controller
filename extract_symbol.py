import sys

def find_matching_paren(text, start_index):
    count = 0
    for i in range(start_index, len(text)):
        if text[i] == '(':
            count += 1
        elif text[i] == ')':
            count -= 1
        if count == 0:
            return i
    return -1

with open('temp-kicad-libraries/symbols/Espressif.kicad_sym', 'r') as f:
    content = f.read()

start_str = '(symbol "ESP32-DevKitC"'
start_index = content.find(start_str)

if start_index != -1:
    end_index = find_matching_paren(content, start_index)
    if end_index != -1:
        with open('controller/esp32.kicad_sym', 'w') as out_file:
            out_file.write(content[start_index:end_index+1])
        print("Symbol extracted successfully.")
    else:
        print("Error: Could not find matching closing parenthesis.")
else:
    print("Error: Symbol not found.")
