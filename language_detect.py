# pip install langid
import langid

def detect_language(string):
    language, _ = langid.classify(string)
    return language

# Example usage
string = "Hola, ¿cómo estás?"
language = detect_language(string)
print("Detected language:", language)