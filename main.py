import random
import string


def generate_password(length=8, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    """
    Génère un mot de passe aléatoire selon les critères fournis.
    :param length: Longueur du mot de passe
    :param use_upper: Inclure des lettres majuscules
    :param use_lower: Inclure des lettres minuscules
    :param use_digits: Inclure des chiffres
    :param use_symbols: Inclure des symboles
    :return: Mot de passe généré
    """
    character_passw = ''
    if use_upper:
        character_passw += string.ascii_uppercase
    if use_lower:
        character_passw += string.ascii_lowercase
    if use_digits:
        character_passw += string.digits
    if use_symbols:
        character_passw += string.punctuation

    if not character_passw:
        raise ValueError(
            "Au moins un type de caractère doit être sélectionné.")

    return ''.join(random.choice(character_passw) for _ in range(length))


# Demande des préférences à l'utilisateur
try:
    length = int(input("Entrez la longueur de votre mot de passe : "))
    use_upper = input("Inclure des majuscules ? (o/n) ").strip().lower() == 'o'
    use_lower = input("Inclure des minuscules ? (o/n) ").strip().lower() == 'o'
    use_digits = input("Inclure des chiffres ? (o/n) ").strip().lower() == 'o'
    use_symbols = input("Inclure des symboles ? (o/n) ").strip().lower() == 'o'

    password = generate_password(
        length, use_upper, use_lower, use_digits, use_symbols)
    print(f"Mot de passe généré : {password}")

except ValueError:
    print("Erreur : Veuillez entrer une longueur valide.")
