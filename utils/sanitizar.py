import unicodedata

def sanitizar(text):
    # Convertir a minúsculas
    text = text.lower()

    # Normalizar el texto para separar acentos
    text = unicodedata.normalize('NFD', text)

    # Eliminar acentos y diéresis
    text = ''.join(
        c for c in text
        if unicodedata.category(c) != 'Mn'
    )

    # Reemplazar la ñ por n
    text = text.replace('ñ', 'n')

    return text