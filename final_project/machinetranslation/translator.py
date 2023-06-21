"""
App to translate english to french and french to english
"""
from deep_translator import MyMemoryTranslator

# function for english to french
def englis_to_french(english_text):
    """
    Translate english to french
    Args:
        english_text (str): text to translate
    Returns:
        str: the translated text
    """
    french_text = MyMemoryTranslator(source='en', target='fr').translate(english_text)
    return french_text

#function for french to english
def french_to_english(french_text):
    """
    Translate french to english
    Args:
        french_text (str): text to translate
    Returns:
        str: the translated text
    """
    english_text = MyMemoryTranslator(source='fr', target='en').translate(french_text)
    return english_text

