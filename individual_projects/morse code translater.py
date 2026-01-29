#ZC 2nd Morse code translator.py
morse_dict = (
    (".-", "A"), ("-...", "B"), ("-.-.", "C"), ("-..", "D"), (".", "E"),
    ("..-.", "F"), ("--.", "G"), ("....", "H"), ("..", "I"), (".---", "J"),
    ("-.-", "K"), (".-..", "L"), ("--", "M"), ("-.", "N"), ("---", "O"),
    (".--.", "P"), ("--.-", "Q"), (".-.", "R"), ("...", "S"), ("-", "T"),
    ("..-", "U"), ("...-", "V"), (".--", "W"), ("-..-", "X"), ("-.--", "Y"),
    ("--..", "Z"), ("-----", "0"), (".----", "1"), ("..---", "2"), ("...--", "3"),
    ("....-", "4"), (".....", "5"), ("-....", "6"), ("--...", "7"), ("---..", "8"), ("----.", "9"), (".-.-.-", "."), ("--..--", ","), ("..--..", "?"), ("-..-.", "/"), ("-....-", "-"), (".----.", "'"),
    ("-...-", "="), (".-..-.", '"'), ("...-..-", "$"), (".--.--.", "@"), ("---...", ":"), ("-.-.-.", ";"), ("..--.-", "_"), ("-.--.", "("), ("-.--.--", ")")
)

print("Welcome to the Morse Code Translator!")
def main():


    def morsetoenglish():
        while True:
            translation = ""
            print("Enter morse code to translate (separate letters with spaces and words with ' / ' when possible)")
            print("or type 'exit' or 'q' to quit:")
            morse_input = input().strip()
            if morse_input.lower() == 'exit' or morse_input.lower() == 'q':
                print("Exiting Morse Code Translator. Goodbye!")
                break
            morse_list = morse_input.split(" ")
            found_invalid = False
            for letter in morse_list:
                if letter == "":
                    continue
                if letter == "/":
                    translation += " "
                else:
                    found = False
                    for morse, english in morse_dict:
                        if morse == letter:
                            translation += english
                            found = True
                            break
                    if not found:
                        print(f"Invalid Morse Code '{letter}'. Please try again.")
                        found_invalid = True
                        break
            if not found_invalid and translation:
                print("Translated message:", translation)


    def englishtomorse():
        while True:
            morse_translation = ""
            print("Enter english text to translate to morse code (type 'exit' or 'q' to quit):")
            english_input = input().strip()
            if english_input.lower() == 'exit' or english_input.lower() == 'q':
                print("Exiting English to Morse Code Translator. Goodbye!")
                break
            found_invalid = False
            for char in english_input.upper():
                if char == " ":
                    morse_translation += " / "
                else:
                    found = False
                    for morse, english in morse_dict:
                        if english == char:
                            morse_translation += morse + " "
                            found = True
                            break
                    if not found:
                        print(f"Character '{char}' cannot be translated to Morse Code. Please try again.")
                        found_invalid = True
                        break
            if not found_invalid and morse_translation:
                print("Translated Morse Code:", morse_translation.strip())


    while True:
        print ("are you translating morse to english or english to morse?(enter 'm' for morse to english and 'e' for english to morse. type q to quit.)")
        choice = input().strip().lower()
        if choice == 'm':
            morsetoenglish()
        elif choice == 'e':
            englishtomorse()
        elif choice == 'q':
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please enter 'm', 'e', or 'q'.")
main()