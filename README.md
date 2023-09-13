"# tugas-pbp-gyan" 
Gyanamurti Adhikara Bano
2206082266

link: https://libralogia.adaptable.app/

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step

A. Membuat dan Aktifkan Virtual Environment
Pada langkah pertama ini, saya akan membuat dan mengaktifkan virtual environment. Virtual environment adalah lingkungan terisolasi di komputer saya yang memungkinkan saya mengisolasi proyek Python dari proyek lain dan mengelola dependensi proyek secara terpisah. Ini memungkinkan saya untuk menjaga kebersihan dan independensi proyek saya. Saya dapat memulainya dengan membuka terminal atau command prompt di komputer saya dan navigasi ke direktori proyek yang ingin saya gunakan. Setelah berada di direktori tersebut, saya membuat virtual environment dengan perintah python -m venv myenv, di mana myenv adalah nama lingkungan virtual yang bisa saya ubah sesuai keinginan. Kemudian, saya mengaktifkan lingkungan virtual dengan menggunakan perintah yang sesuai untuk sistem operasi saya (dalam kasus ini Windows).

B. Membuat Proyek Django Baru
Setelah virtual environment saya aktif, langkah berikutnya adalah menginstall requirements.txt pada langkah ini akan menginstall beberapa hal meliputi django, gunicorn, whitenoise, psycopg2-binary, requests dan,urllib3 yang semuanya akan berguna dalam proyek kali ini. Lalu dilanjutkan dengan membuat proyek Django baru. Proyek Django adalah kerangka kerja web yang akan saya gunakan untuk membangun aplikasi web saya. Saya dapat melakukan ini dengan perintah django-admin startproject tugas_pbp_gyan, di mana tugas_pbp_gyan adalah nama proyek yang akan saya buat. Ini akan menciptakan struktur dasar proyek Django saya.

C. Membuat Aplikasi Main
Dalam Django, aplikasi adalah komponen yang dapat digunakan untuk mengelompokkan fungsionalitas dalam proyek saya. Dalam langkah ini, saya membuat aplikasi dengan nama "main" yang akan saya gunakan untuk mengelola buku dalam perpustakaan saya. Untuk melakukannya, saya perlu masuk ke direktori proyek saya dan menjalankan perintah python manage.py startapp main. Ini akan menciptakan struktur dasar aplikasi "main" dalam proyek saya.

D. Konfigurasi Routing
Routing adalah cara Django mengarahkan permintaan web dari pengguna ke fungsi yang sesuai dalam aplikasi saya. Pada langkah ini, saya perlu mengkonfigurasi routing dalam proyek saya. Saya membuka file mylibrary/urls.py dan menambahkan routing untuk aplikasi "main" dengan perintah path('', include('main.urls')). Ini akan memetakan permintaan web yang datang tanpa path tambahan ke aplikasi "main" yang akan saya konfigurasi selanjutnya.

E. Membuat Model "Item"
Langkah ini berfokus pada pembuatan model Django untuk menggambarkan entitas "Item" dalam aplikasi pengelolaan buku perpustakaan saya. Model ini didefinisikan dalam file main/models.py dan mencakup atribut seperti "name" (nama buku), "amount" (jumlah buku), "description" (deskripsi buku), "image_url" (URL gambar buku), "author" (nama penulis), "year" (tahun penerbitan), "publisher" (nama penerbit), "genre" (genre buku), dan "rating" (peringkat buku). Atribut-atribut ini akan digunakan untuk menyimpan informasi rinci tentang buku dalam basis data. Setelah model didefinisikan, saya membuat migrasi menggunakan perintah python manage.py makemigrations main untuk menghasilkan file migrasi, lalu menerapkannya ke database dengan perintah python manage.py migrate, sehingga tabel yang sesuai dengan model "Item" akan dibuat dalam database. Dengan demikian, struktur data yang komprehensif untuk buku dalam perpustakaan telah diatur dalam proyek Django saya.

F. Membuat View
Pada langkah ini, saya membuat view Django yang bertugas menangani permintaan web dari pengguna dan menghasilkan respons untuk ditampilkan. Proses ini dimulai dengan membuka file main/views.py dan menambahkan fungsi show_main di dalamnya. Fungsi show_main ini dirancang untuk menampilkan informasi pribadi saya, seperti nama dan kelas, kepada pengguna. Ketika fungsi ini menerima permintaan HTTP dari pengguna sebagai argumen, ia akan menghasilkan respons yang nantinya akan diarahkan ke sebuah template HTML yang telah saya buat sebelumnya, yaitu main.html. Saya menggunakan modul render yang disediakan oleh Django untuk menghasilkan respons ini dengan cara merender template HTML yang akan digunakan untuk menampilkan informasi. Dalam contoh ini, informasi nama dan kelas saya disediakan secara statis di dalam fungsi, namun dalam implementasi aplikasi yang sebenarnya, saya mungkin akan mengambil data tersebut dari database atau sumber data lain sesuai dengan kebutuhan aplikasi.

G. Konfigurasi Routing Aplikasi Main
Routing atau pemetaan URL adalah cara Django mengarahkan permintaan web dari pengguna ke fungsi view yang sesuai. Dalam langkah ini, saya membuka file main/urls.py dan menambahkan konfigurasi routing untuk aplikasi "main." Saya mendefinisikan bahwa permintaan yang datang ke URL utama (misalnya, http://localhost:8000/) akan diarahkan ke fungsi show_main yang telah saya buat dalam views. Ini dilakukan dengan menggunakan path('', views.show_main, name='show_main'), yang berarti ketika pengguna mengakses URL utama, Django akan memanggil fungsi show_main dan mengembalikan responsnya.

H. Testing Django
Tutorial ini memberikan pengantar tentang penggunaan unit testing dalam Django, pentingnya pengujian untuk memastikan bahwa kode berfungsi sesuai harapan, dan bagaimana mengimplementasikannya. Langkah pertama melibatkan pembuatan dua tes dalam berkas tests.py yang memeriksa akses URL dan penggunaan template pada halaman /main/. Langkah kedua adalah menjalankan tes dengan perintah python manage.py test, yang memberikan laporan tentang berapa banyak tes yang dijalankan dan jika semuanya berhasil. Ini adalah praktik yang sangat berguna dalam pengembangan aplikasi Django untuk memastikan fungsionalitas yang andal dan mendeteksi masalah yang mungkin timbul selama perubahan kode.

I. Menambahkan, Mendorong, dan Melakukan Commit ke Repositori GitHub
Setelah berhasil melakukan pengujian, langkah pertama adalah mengunggah proyek saya ke repositori Library-Inventory di GitHub. Sebelum melakukan unggahan, pastikan saya telah membuat file .gitignore untuk menentukan file dan direktori yang harus diabaikan oleh Git, seperti file sementara atau yang berisi informasi rahasia. Setelah itu, lanjutkan dengan menggunakan perintah git add . untuk menambahkan semua perubahan ke dalam staging area, lalu gunakan git commit -m "Pesan commit saya" untuk membuat commit yang berisi perubahan yang sudah ditambahkan. Akhirnya, saya bisa menggunakan perintah git push -u origin main untuk mengirimkan perubahan tersebut ke repositori GitHub. Dengan ini, proyek saya akan tercatat dengan baik dalam repositori dan siap untuk berkolaborasi dengan orang lain atau untuk keperluan penyimpanan dan dokumentasi.

J. Deployment ke Adaptable
Setelah berhasil mengembangkan aplikasi secara lokal, langkah pertama adalah mendeploy aplikasi ke server atau platform hosting yang dapat diakses secara online. Ini akan memungkinkan orang lain untuk mengakses aplikasi melalui internet.

K. Membuat README.MD
File ini berfungsi sebagai dokumentasi proyek yang berisi tautan langsung ke aplikasi yang sudah di-host di Adaptable, serta jawaban atas pertanyaan yang mungkin muncul terkait proyek tersebut. Setelah selesai, README.md harus ditambahkan, di-commit, dan di-push ke repositori GitHub proyek.

L. Menonaktifkan Lingkungan Virtual
Langkah terakhir adalah menonaktifkan lingkungan virtual yang mungkin telah saya gunakan selama proses pengembangan aplikasi. Ini penting untuk memastikan efisiensi sumber daya dan menghindari konsumsi daya yang tidak perlu setelah proyek selesai dan aplikasi telah di-deploy secara online.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![Gambar no 2 Gyan](https://ibb.co/wpKNYd7)
Ketika seorang klien mengirimkan permintaan ke URL http://localhost:8000/ dalam aplikasi Django, sistem akan mencocokkan URL tersebut dengan pola yang telah didefinisikan sebelumnya dalam file urls.py. Setelah cocok, server akan menjalankan fungsi tampilan (views) terkait, di mana logika bisnis dan persiapan data dilakukan, seringkali melibatkan akses ke model yang menggambarkan data dalam database. Setelah data diambil dan diproses, fungsi tampilan akan merender template (contohnya, "index.html") untuk menghasilkan tampilan akhir. Respons dari proses ini kemudian dikirimkan sebagai halaman web yang ditampilkan kepada klien, memungkinkan mereka melihat konten yang dihasilkan dinamis sesuai permintaan mereka.

3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Sebagai seseorang yang baru belajar django, saya menggunakan virtual environment karena beberapa alasan:
A. Isolasi Dependensi: Setiap proyek yang saya kerjakan mungkin memerlukan versi pustaka yang berbeda. Dengan menggunakan virtual environment, saya dapat mengisolasi dependensi proyek sehingga tidak saling bertabrakan.
B. Menghindari Konflik Sistem: Beberapa pustaka mungkin memerlukan versi yang berbeda dari pustaka sistem. Dengan menggunakan virtual environment, saya dapat menghindari konflik ini.
C. Reproduktivitas: Dengan menggunakan virtual environment, saya dapat dengan mudah mereproduksi lingkungan pengembangan di mesin lain.

Lalu sebenarnya saya tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment. Namun, hal ini tidak disarankan karena dapat menyebabkan konflik dependensi antara proyek dan sistem. Selain itu, tanpa virtual environment, akan sulit untuk memastikan bahwa aplikasi yang saya buat akan berjalan dengan benar di lingkungan lain karena versi pustaka yang digunakan mungkin berbeda.

4. 
Berikut adalah penjelasan tentang MVC, MVT, dan MVVM:
A. MVC (Model-View-Controller): MVC adalah pola desain yang memisahkan aplikasi menjadi tiga komponen logis utama: Model, View, dan Controller. Model mencakup semua data dan logika terkait. View adalah struktur, tata letak, dan penampilan dari apa yang dilihat pengguna di layar. Controller bertindak sebagai antarmuka antara Model dan View. Controller menerima input pengguna dari View, memprosesnya (sering melibatkan perubahan pada Model), dan memperbarui View sesuai.

B. MVT (Model-View-Template): MVT adalah pola desain perangkat lunak yang digunakan oleh framework web Django. Model bertindak sebagai antarmuka data user. View adalah antarmuka pengguna — apa yang user lihat di browser user ketika merender situs web. Template terdiri dari bagian statis dari output HTML yang diinginkan serta beberapa sintaks khusus yang menjelaskan bagaimana konten dinamis akan dimasukkan.

C. MVVM (Model-View-ViewModel): Ini adalah turunan dari pola MVC di mana Controller digantikan oleh ViewModel. ViewModel bertindak sebagai antarmuka dan menyajikan data dari Model dengan cara yang lebih mudah untuk dikelola dan dipresentasikan di View. Sering digunakan dalam aplikasi yang memerlukan pengikatan data dari Model ke View. MVVM adalah pola arsitektur dalam perangkat lunak komputer yang memfasilitasi pemisahan pengembangan antarmuka pengguna grafis (GUI; view) dari pengembangan logika bisnis atau logika back-end (model) sehingga view tidak bergantung pada platform model tertentu.

Perbedaan utama antara ketiganya adalah sebagai berikut:
- Dalam MVC, controller adalah titik masuk ke Aplikasi, sedangkan dalam MVVM, view adalah titik masuk ke Aplikasi.
- Dalam MVT, Django menggunakan template dalam kerangka kerjanya. Template bertanggung jawab untuk seluruh Antarmuka Pengguna sepenuhnya.
- Dalam MVVM, ViewModel bertindak sebagai pengubah nilai, artinya ViewModel bertanggung jawab untuk mengekspos objek data dari Model sedemikian rupa sehingga objek dapat dengan mudah dikelola dan dipresentasikan.

Django adalah framework pengembangan web yang mengikuti pola desain MVT (Model-View-Template). Berikut adalah bagaimana Django berhubungan dengan konsep-konsep ini:
Model: Dalam Django, model adalah representasi dari basis data. Ini adalah tempat saya mendefinisikan struktur data saya, dan Django akan membuat tabel basis data untuk saya.
View: View dalam Django bertanggung jawab untuk memproses permintaan dan meresponsnya dengan sebuah respons. View mengambil data dari model, menerapkan logika bisnis, dan kemudian meneruskannya ke template.
Template: Template dalam Django adalah bagian yang menangani bagaimana situs web saya ditampilkan atau bagaimana ia tampak di browser. Template biasanya berisi HTML yang dicampur dengan sintaks template Django.

Jadi, meskipun Django menggunakan pola MVT, konsep-konsep ini mirip dengan MVC dan MVVM. Dalam semua kasus, tujuannya adalah untuk memisahkan logika aplikasi (Model) dari presentasinya (View/Template) dan bagaimana data diproses (Controller/ViewModel). Perbedaan utama adalah bagaimana kerangka kerja ini mengimplementasikan konsep-konsep ini.