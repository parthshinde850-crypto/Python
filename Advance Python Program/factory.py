class FrenchLocalizer:
    def __init__(self):
        self.translations = {
            "car": "voiture",
            "bike": "bicyclette",
            "cycle": "cyclette"
        }

    def localize(self, msg):
        return self.translations.get(msg, msg)


class SpanishLocalizer:
    def __init__(self):
        self.translations = {
            "car": "coche",
            "bike": "bicicleta",
            "cycle": "ciclo"
        }

    def localize(self, msg):
        return self.translations.get(msg, msg)


class EnglishLocalizer:
    def localize(self, msg):
        return msg


def Factory(language):
    languages = {
        "French": FrenchLocalizer,
        "Spanish": SpanishLocalizer,
        "English": EnglishLocalizer
    }

    return languages[language]()


if __name__ == "__main__":
    f = Factory("French")
    s = Factory("Spanish")
    e = Factory("English")

    words = ["car", "bike", "cycle"]

    print("French:")
    for word in words:
        print(f.localize(word))

    print("\nSpanish:")
    for word in words:
        print(s.localize(word))

    print("\nEnglish:")
    for word in words:
        print(e.localize(word))