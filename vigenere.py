"""Bib for list of letters in alphabetic order"""
import string
import sys

class Vigenere():
    """ class for de- and encripting according to vigenere-algorithm """
    def __init__(self, key):
        
        """
        Args:
            key (_string_): Keyword for description
        """
        start = 0
        end = 26
        self.quad = []
        # Vigenerequadrat
        vigenere_quad = string.ascii_uppercase
        for letter in vigenere_quad:
            line = string.ascii_uppercase[vigenere_quad.index(letter):end]
            if vigenere_quad.index(letter) > 0:
                for plus_letter in string.ascii_uppercase[start: vigenere_quad.index(letter)]:
                    line += plus_letter
            self.quad.append(line)
            
        # print vigenere_quad
        # =====================================
        # for line in self.quad:
        #     print(line)

        self.key = key
        self.encrypt_sol = ''
        self.decrypt_sol = ''


    def encrypt(self, message):
        """encrypt message according to given key

        Args:
            message (_string_): clear message for encryption

        Returns:
            _string_: encrypted message
        """
        key_pos = 0
        for pos in message:
            if pos != ' ':
                if key_pos == len(self.key):
                    key_pos = 0
                for line in self.quad:
                    if line[0] == self.key[key_pos]:
                        ind = self.quad[0].index(pos)
                        enc = line[ind]
                        self.encrypt_sol += enc
                key_pos += 1
            else:
                self.encrypt_sol += ' '
        return self.encrypt_sol
    

    def decrypt(self, message):
        """decrypt message according to given key

        Args:
            message (_string_): encrypted message

        Returns:
            _string_: clear message according t
        """
        key_pos = 0
        for pos in message:
            if pos != ' ':
                if key_pos == len(self.key):
                    key_pos = 0
                for line in self.quad:
                    if line[0] == self.key[key_pos]:
                        ind = line.index(pos)
                        enc = self.quad[0][ind]
                        self.decrypt_sol += enc
                key_pos += 1
            else:
                self.decrypt_sol += ' '
        return self.decrypt_sol
    

if __name__ == '__main__' :
    key = sys.argv[1].upper()
    print(f"Your key: {key}")
    message = sys.argv[2].upper()
    action = sys.argv[3].upper()

    vig = Vigenere(key)
    
    if action == 'DE':
        print(vig.decrypt(message))
    elif action == "EN":
        print(vig.encrypt(message))
        
        