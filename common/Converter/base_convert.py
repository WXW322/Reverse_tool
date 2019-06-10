
class Converter:
    def __init__(self):
        pass

    def convert_raw_to_text(self, message):
        phrase = ''
        for i in range(len(message)):
            if(len(phrase) == 0):
                phrase = phrase + str(message[i])
            else:
                phrase = phrase + ' ' + str(message[i])
        return phrase

    def convert_text_to_raw(self, phrase):
        pass

