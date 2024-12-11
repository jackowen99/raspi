import tkinter as tk
import time

class MorseTransmitterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Morse Code Transmitter")

        # Morse Code Dictionary
        self.morse_dict = {
            "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
            "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
            "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
            "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
            "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
            "Z": "--..", "0": "-----", "1": ".----", "2": "..---", "3": "...--",
            "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..",
            "9": "----.", " ": "/"
        }

        # Input Textbox
        self.input_label = tk.Label(root, text="Enter Text to Transmit:")
        self.input_label.pack(pady=10)

        self.input_text = tk.Entry(root, width=50)
        self.input_text.pack(pady=10)

        # Transmit Button
        self.transmit_button = tk.Button(root, text="Transmit", command=self.transmit_morse)
        self.transmit_button.pack(pady=10)

        # Flashing Label
        self.flash_label = tk.Label(root, text="", bg="black", width=20, height=10)
        self.flash_label.pack(pady=10)

    def transmit_morse(self):
        """Convert the input text to Morse code and flash it."""
        text = self.input_text.get().upper()
        morse_code = ""

        # Convert text to Morse code
        for char in text:
            morse_code += self.morse_dict.get(char, "") + " "

        # Transmit Morse code
        for symbol in morse_code:
            if symbol == ".":
                self.flash_on()
                time.sleep(0.2)  # Dot duration
                self.flash_off()
            elif symbol == "-":
                self.flash_on()
                time.sleep(0.6)  # Dash duration
                self.flash_off()
            elif symbol == " ":
                time.sleep(0.2)  # Space between letters
            elif symbol == "/":
                time.sleep(0.6)  # Space between words

    def flash_on(self):
        """Turn the flash on (change label background to white)."""
        self.flash_label.config(bg="white")
        self.root.update()

    def flash_off(self):
        """Turn the flash off (change label background to black)."""
        self.flash_label.config(bg="black")
        self.root.update()
        time.sleep(0.2)  # Gap between symbols

if __name__ == "__main__":
    root = tk.Tk()
    app = MorseTransmitterApp(root)
    root.mainloop()