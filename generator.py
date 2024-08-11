import qrcode
from cryptography.fernet import Fernet
from datetime import datetime

# Klucz główny (musisz go przechowywać bezpiecznie)
# MAIN_KEY = Fernet.generate_key()
MAIN_KEY = b'NJTbCsa6xIpyhw5JoLGE2mI4GWk343Dm9vi9eekVGXk=' 



# Funkcja do szyfrowania tekstu
def encrypt_text(text, key):
    fernet = Fernet(key)
    encrypted_text = fernet.encrypt(text.encode())
    return encrypted_text

# Funkcja do generowania kodu QR
def generate_qr_code(id_request, points, date, time):
    # Tworzenie tekstu do zaszyfrowania
    # text = f"id: {user_id}, punkty: {points}, data: {date}, godzine: {time}"
    text = (
    '{'
    f'"id_request": "{id_request}", '
    f'"points": "{points}", '
    f'"date": "{date}", '
    f'"time": "{time}"'
    '}'
    )
    
    # Szyfrowanie tekstu
    encrypted_text = encrypt_text(text, MAIN_KEY)
    # url = f"http://127.0.0.1:8000/decode/?data={encrypted_text.decode()}"
    url = f"http://k.pspk.smallhost.pl/decode/?data={encrypted_text.decode()}"

    print(url)
    
    # Generowanie kodu QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save("qr_code.png")  # Zapisz kod QR do pliku
    img.show()  # Wyświetl kod QR

# Przykładowe użycie
points = 4
date = datetime.now().strftime("%Y-%m-%d")
time = datetime.now().strftime("%H:%M:%S")


id_date = datetime.now().strftime("%Y%m%d")
id_time = datetime.now().strftime("%H%M%S")

# Utwórz unikalne ID na podstawie daty i czasu, składające się tylko z cyfr
id_request = f"{id_date}{id_time}"

generate_qr_code(id_request, points, date, time)
