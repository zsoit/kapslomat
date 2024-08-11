from django.http import HttpResponse
from cryptography.fernet import Fernet
from django.shortcuts import render
import json 

# Klucz główny (musisz go przechowywać bezpiecznie)
MAIN_KEY = b'NJTbCsa6xIpyhw5JoLGE2mI4GWk343Dm9vi9eekVGXk='  # Wstaw ten sam klucz, który użyto do szyfrowania

# Funkcja do odszyfrowania tekstu
def decrypt_text(encrypted_text, key):
    fernet = Fernet(key)
    decrypted_text = fernet.decrypt(encrypted_text.encode()).decode()
    return decrypted_text

# Widok do odszyfrowania danych
def decode_view(request):
    encrypted_text = request.GET.get('data')
    if encrypted_text:
        try:
            decrypted_text = decrypt_text(encrypted_text, MAIN_KEY)
            data_list = json.loads(decrypted_text)
            print(type(data_list))
            return render(request, 'decode.html', {'data': data_list})
            
            # return HttpResponse(f" {decrypted_text}")
        except Exception as e:
            return HttpResponse(f"Error")
    else:
        return HttpResponse("No data parameter provided.")
