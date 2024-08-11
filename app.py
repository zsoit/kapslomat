from cryptography.fernet import Fernet

# Klucz główny (musisz go przechowywać bezpiecznie)
MAIN_KEY = b'NJTbCsa6xIpyhw5JoLGE2mI4GWk343Dm9vi9eekVGXk=' 

# Funkcja do odszyfrowania tekstu
def decrypt_text(encrypted_text, key):
    fernet = Fernet(key)
    decrypted_text = fernet.decrypt(encrypted_text).decode()
    return decrypted_text

# Funkcja do zamiany URL-a na dane
def decode_url(url):
    encrypted_text = url.split('/')[-1].encode()
    decrypted_text = decrypt_text(encrypted_text, MAIN_KEY)
    print("Decrypted data:", decrypted_text)

# Przykładowe użycie
encoded_url = "https://kapsolmat.pl/gAAAAABmt3quRrB3p5BmTIjR_T1Ahpy5ax6XPrqT-EFR0Zy7t5pdN_Ulo8vNBrZw1ZXtybcfvdBf1TXUDtirrz1hZG7m1pZwPpus0AkZfSLOYHQx1_63sICeRyZ-niTjgWt0bxcS5SSXKxhF0Fx6MF8qq77OXaHrMQ=="  # Wstaw URL wygenerowany przez poprzednią aplikację
decode_url(encoded_url)
