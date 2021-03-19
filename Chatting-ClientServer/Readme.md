Kelas : 18TI2

NIM : 03082180002

Nama : Julina Happy

Dalam flie client server ini, saya memilih untuk melakukan fitur chatting/messaging

Pertama jalankan terlebih dahulu server.py dengan :

py server.py --host 127.0.0.1 --port 8080(blh port dan host yang lain, tetapi saat dikoneksikan harus menggunakan port yang sama agar terkoneksi dengan sesama client)
tetapi dalam default saya memberikan:

ip : 127.0.0.1

port : 8080

sehingga ketika user tidak tau ingin menggunakan ip dan port apa maka ketika user menekan:

py server.py akan secara otomatis terkoneksi dengan ip dan port yang menjadi default

setelah berhasil dikoneksikan maka jalankan clien.py :
py client.py

Maka akan muncuk sebuah tab UI yang akan berisi ip address dan port, isilah ip dan port sesuai dengan ip dan port yang terdapat dalam server.py saat dikoneksikan.
Ketika tidak sesuai dengan port dan ip address yang telah dikoneksikan maka client tidak dapat mengakses chat room (connection refused/failed)

Setelah terkoneksi maka tab "chat room" akan dapat di-klik dan akan dapat melakukan percakapan disana

Orang baru dapat bergabung dalam percakapan dengan menjalankan client.py dan juga dengan menggunakan ip dan port yang sama, setelah itu akan muncul tab dan diminta untuk menuliskan

nama, dan setelah terkoneksi maka dapat bergabung dengan percakapan.

Dalam percakapan dapat mengirim sticker dan juga dapat melakukan percakapan private dengan orang yang terdapat di dalam percakapan, jika sesorang melakukan private chat kepada sesorang

maka orang ketiga tidak dapat melihat percakapan tersebut karena bersifat private.
