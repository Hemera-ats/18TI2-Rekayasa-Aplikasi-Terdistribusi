## Nama : Julina Happy
## IM : 03082180002
## Kelas : 18TI2

# Crypto List and Price using CoinCap API

Dalam UAS ini saya menggunakan CoinCap API sebagai API saya, dimana CoinCap merupakan sebuah tools yang digunakan untuk melihat market activty secara real-time(cryptocurrency)
Dokumentasi CoinCap https://docs.coincap.io/

# Endopoints
Endpoints yang saya gunakan dalam project kali ini adalah:
api.coincap.io/v2/assets

# Requirement
Requirement yang dibutuhkan untuk dapat menjalankan project ini adalah sebagai berikut:
- Visual Studio Code
- Terminal / Command Prompt
- Python
- Web Browser(Chrome)

# Dependencies
Dependencies yang diperlukan adalah sebagai berikut:
- Django

# Running the Code
- Install the project
- import django
- run -> py manage.py runserver untuk mendapatkan url server yang akan memunculkan
  Starting development server at http://127.0.0.1:8000/
- Setelah itu ketika akan masuk ke halaman list dari crypto, url tersebut ditambahkan dengan path yang telah dibuat yaitu:
  path('api/coin-list', views.coin_list, name="coin list"), yang artinya http://127.0.0.1:8000/api/coin-list
- Setelah di klik maka akan ditemukan harga/price dari crypto tersebut atau dengan path:path('api/coin-list/<str:coinName>', views.coin_view, name="Coin Desc"),
  yang artinya http://127.0.0.1:8000/api/coin-list/bitcon (untuk contoh list crypto bitcoin)


