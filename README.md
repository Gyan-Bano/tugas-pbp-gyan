# TUGAS PEMROGRAMAN BERBASIS PLATFORM
Gyanamurti Adhikara Bano
2206082266

link: https://libralogia.adaptable.app/

## TUGAS 2
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step
    1. Membuat dan Aktifkan Virtual Environment
        Pada langkah pertama ini, saya akan membuat dan mengaktifkan virtual environment. Virtual environment adalah lingkungan terisolasi di komputer saya yang memungkinkan saya mengisolasi proyek Python dari proyek lain dan mengelola dependensi proyek secara terpisah. Ini memungkinkan saya untuk menjaga kebersihan dan independensi proyek saya. Saya dapat memulainya dengan membuka terminal atau command prompt di komputer saya dan navigasi ke direktori proyek yang ingin saya gunakan. Setelah berada di direktori tersebut, saya membuat virtual environment dengan perintah python -m venv myenv, di mana myenv adalah nama lingkungan virtual yang bisa saya ubah sesuai keinginan. Kemudian, saya mengaktifkan lingkungan virtual dengan menggunakan perintah yang sesuai untuk sistem operasi saya (dalam kasus ini Windows).

    2. Membuat Proyek Django Baru
        Setelah virtual environment saya aktif, langkah berikutnya adalah menginstall requirements.txt pada langkah ini akan menginstall beberapa hal meliputi django, gunicorn, whitenoise, psycopg2-binary, requests dan,urllib3 yang semuanya akan berguna dalam proyek kali ini. Lalu dilanjutkan dengan membuat proyek Django baru. Proyek Django adalah kerangka kerja web yang akan saya gunakan untuk membangun aplikasi web saya. Saya dapat melakukan ini dengan perintah django-admin startproject tugas_pbp_gyan, di mana tugas_pbp_gyan adalah nama proyek yang akan saya buat. Ini akan menciptakan struktur dasar proyek Django saya.

    3. Membuat Aplikasi Main
        Dalam Django, aplikasi adalah komponen yang dapat digunakan untuk mengelompokkan fungsionalitas dalam proyek saya. Dalam langkah ini, saya membuat aplikasi dengan nama "main" yang akan saya gunakan untuk mengelola buku dalam perpustakaan saya. Untuk melakukannya, saya perlu masuk ke direktori proyek saya dan menjalankan perintah python manage.py startapp main. Ini akan menciptakan struktur dasar aplikasi "main" dalam proyek saya.

    4. Konfigurasi Routing
        Routing adalah cara Django mengarahkan permintaan web dari pengguna ke fungsi yang sesuai dalam aplikasi saya. Pada langkah ini, saya perlu mengkonfigurasi routing dalam proyek saya. Saya membuka file mylibrary/urls.py dan menambahkan routing untuk aplikasi "main" dengan perintah path('', include('main.urls')). Ini akan memetakan permintaan web yang datang tanpa path tambahan ke aplikasi "main" yang akan saya konfigurasi selanjutnya.

    5. Membuat Model "Item"
        Langkah ini berfokus pada pembuatan model Django untuk menggambarkan entitas "Item" dalam aplikasi pengelolaan buku perpustakaan saya. Model ini didefinisikan dalam file main/models.py dan mencakup atribut seperti "name" (nama buku), "amount" (jumlah buku), "description" (deskripsi buku), "image_url" (URL gambar buku), "author" (nama penulis), "year" (tahun penerbitan), "publisher" (nama penerbit), "genre" (genre buku), dan "rating" (peringkat buku). Atribut-atribut ini akan digunakan untuk menyimpan informasi rinci tentang buku dalam basis data. Setelah model didefinisikan, saya membuat migrasi menggunakan perintah python manage.py makemigrations main untuk menghasilkan file migrasi, lalu menerapkannya ke database dengan perintah python manage.py migrate, sehingga tabel yang sesuai dengan model "Item" akan dibuat dalam database. Dengan demikian, struktur data yang komprehensif untuk buku dalam perpustakaan telah diatur dalam proyek Django saya.

    6. Membuat View
        Pada langkah ini, saya membuat view Django yang bertugas menangani permintaan web dari pengguna dan menghasilkan respons untuk ditampilkan. Proses ini dimulai dengan membuka file main/views.py dan menambahkan fungsi show_main di dalamnya. Fungsi show_main ini dirancang untuk menampilkan informasi pribadi saya, seperti nama dan kelas, kepada pengguna. Ketika fungsi ini menerima permintaan HTTP dari pengguna sebagai argumen, ia akan menghasilkan respons yang nantinya akan diarahkan ke sebuah template HTML yang telah saya buat sebelumnya, yaitu main.html. Saya menggunakan modul render yang disediakan oleh Django untuk menghasilkan respons ini dengan cara merender template HTML yang akan digunakan untuk menampilkan informasi. Dalam contoh ini, informasi nama dan kelas saya disediakan secara statis di dalam fungsi, namun dalam implementasi aplikasi yang sebenarnya, saya mungkin akan mengambil data tersebut dari database atau sumber data lain sesuai dengan kebutuhan aplikasi.

    7. Konfigurasi Routing Aplikasi Main
        Routing atau pemetaan URL adalah cara Django mengarahkan permintaan web dari pengguna ke fungsi view yang sesuai. Dalam langkah ini, saya membuka file main/urls.py dan menambahkan konfigurasi routing untuk aplikasi "main." Saya mendefinisikan bahwa permintaan yang datang ke URL utama (misalnya, http://localhost:8000/) akan diarahkan ke fungsi show_main yang telah saya buat dalam views. Ini dilakukan dengan menggunakan path('', views.show_main, name='show_main'), yang berarti ketika pengguna mengakses URL utama, Django akan memanggil fungsi show_main dan mengembalikan responsnya.

    8. Testing Django
        Tutorial ini memberikan pengantar tentang penggunaan unit testing dalam Django, pentingnya pengujian untuk memastikan bahwa kode berfungsi sesuai harapan, dan bagaimana mengimplementasikannya. Langkah pertama melibatkan pembuatan dua tes dalam berkas tests.py yang memeriksa akses URL dan penggunaan template pada halaman /main/. Langkah kedua adalah menjalankan tes dengan perintah python manage.py test, yang memberikan laporan tentang berapa banyak tes yang dijalankan dan jika semuanya berhasil. Ini adalah praktik yang sangat berguna dalam pengembangan aplikasi Django untuk memastikan fungsionalitas yang andal dan mendeteksi masalah yang mungkin timbul selama perubahan kode.

    9. Menambahkan, Mendorong, dan Melakukan Commit ke Repositori GitHub
        Setelah berhasil melakukan pengujian, langkah pertama adalah mengunggah proyek saya ke repositori Library-Inventory di GitHub. Sebelum melakukan unggahan, pastikan saya telah membuat file .gitignore untuk menentukan file dan direktori yang harus diabaikan oleh Git, seperti file sementara atau yang berisi informasi rahasia. Setelah itu, lanjutkan dengan menggunakan perintah git add . untuk menambahkan semua perubahan ke dalam staging area, lalu gunakan git commit -m "Pesan commit saya" untuk membuat commit yang berisi perubahan yang sudah ditambahkan. Akhirnya, saya bisa menggunakan perintah git push -u origin main untuk mengirimkan perubahan tersebut ke repositori GitHub. Dengan ini, proyek saya akan tercatat dengan baik dalam repositori dan siap untuk berkolaborasi dengan orang lain atau untuk keperluan penyimpanan dan dokumentasi.

    10. Deployment ke Adaptable
        Setelah berhasil mengembangkan aplikasi secara lokal, langkah pertama adalah mendeploy aplikasi ke server atau platform hosting yang dapat diakses secara online. Ini akan memungkinkan orang lain untuk mengakses aplikasi melalui internet.

    11. Membuat README.MD
        File ini berfungsi sebagai dokumentasi proyek yang berisi tautan langsung ke aplikasi yang sudah di-host di Adaptable, serta jawaban atas pertanyaan yang mungkin muncul terkait proyek tersebut. Setelah selesai, README.md harus ditambahkan, di-commit, dan di-push ke repositori GitHub proyek.

    12. Menonaktifkan Lingkungan Virtual
        Langkah terakhir adalah menonaktifkan lingkungan virtual yang mungkin telah saya gunakan selama proses pengembangan aplikasi. Ini penting untuk memastikan efisiensi sumber daya dan menghindari konsumsi daya yang tidak perlu setelah proyek selesai dan aplikasi telah di-deploy secara online.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
    ![PBP tugas 2 nomor 2 Gyan](https://github.com/Gyan-Bano/tugas-pbp-gyan/assets/124954416/187eb104-b6e6-49f4-bab6-273c8b89bc9b)
    Ketika seorang klien mengirimkan permintaan ke URL http://localhost:8000/ dalam aplikasi Django, sistem akan mencocokkan URL tersebut dengan pola yang telah didefinisikan sebelumnya dalam file urls.py. Setelah cocok, server akan menjalankan fungsi tampilan (views) terkait, di mana logika bisnis dan persiapan data dilakukan, seringkali melibatkan akses ke model yang menggambarkan data dalam database. Setelah data diambil dan diproses, fungsi tampilan akan merender template (contohnya, "index.html") untuk menghasilkan tampilan akhir. Respons dari proses ini kemudian dikirimkan sebagai halaman web yang ditampilkan kepada klien, memungkinkan mereka melihat konten yang dihasilkan dinamis sesuai permintaan mereka.

3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
    Sebagai seseorang yang baru belajar django, saya menggunakan virtual environment karena beberapa alasan:
    - Isolasi Dependensi: Setiap proyek yang saya kerjakan mungkin memerlukan versi pustaka yang berbeda. Dengan    menggunakan virtual environment, saya dapat mengisolasi dependensi proyek sehingga tidak saling bertabrakan.
    - Menghindari Konflik Sistem: Beberapa pustaka mungkin memerlukan versi yang berbeda dari pustaka sistem. Dengan menggunakan virtual environment, saya dapat menghindari konflik ini.
    - Reproduktivitas: Dengan menggunakan virtual environment, saya dapat dengan mudah mereproduksi lingkungan      pengembangan di mesin lain.

    Lalu sebenarnya saya tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment. Namun, hal ini tidak disarankan karena dapat menyebabkan konflik dependensi antara proyek dan sistem. Selain itu, tanpa virtual environment, akan sulit untuk memastikan bahwa aplikasi yang saya buat akan berjalan dengan benar di lingkungan lain karena versi pustaka yang digunakan mungkin berbeda.

4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
Berikut adalah penjelasan tentang MVC, MVT, dan MVVM:
   1. Membuat dan Aktifkan Virtual Environment
        MVC adalah pola desain yang memisahkan aplikasi menjadi tiga komponen logis utama: Model, View, dan Controller. Model mencakup semua data dan logika terkait. View adalah struktur, tata letak, dan penampilan dari apa yang dilihat pengguna di layar. Controller bertindak sebagai antarmuka antara Model dan View. Controller menerima input pengguna dari View, memprosesnya (sering melibatkan perubahan pada Model), dan memperbarui View sesuai.  

   2. MVT (Model-View-Template): 
        MVT adalah pola desain perangkat lunak yang digunakan oleh framework web Django. Model bertindak sebagai antarmuka data user. View adalah antarmuka pengguna — apa yang user lihat di browser user ketika merender situs web. Template terdiri dari bagian statis dari output HTML yang diinginkan serta beberapa sintaks khusus yang menjelaskan bagaimana konten dinamis akan dimasukkan.

   3. MVVM (Model-View-ViewModel):  
        Ini adalah turunan dari pola MVC di mana Controller digantikan oleh ViewModel. ViewModel bertindak sebagai antarmuka dan menyajikan data dari Model dengan cara yang lebih mudah untuk dikelola dan dipresentasikan di View. Sering digunakan dalam aplikasi yang memerlukan pengikatan data dari Model ke View. MVVM adalah pola arsitektur dalam perangkat lunak komputer yang memfasilitasi pemisahan pengembangan antarmuka pengguna grafis (GUI; view) dari pengembangan logika bisnis atau logika back-end (model) sehingga view tidak bergantung pada platform model tertentu.

    Perbedaan utama antara ketiganya adalah sebagai berikut:
    - Dalam MVC, controller adalah titik masuk ke Aplikasi, sedangkan dalam MVVM, view adalah titik masuk ke Aplikasi.
    - Dalam MVT, Django menggunakan template dalam kerangka kerjanya. Template bertanggung jawab untuk seluruh Antarmuka Pengguna sepenuhnya.
    - Dalam MVVM, ViewModel bertindak sebagai pengubah nilai, artinya ViewModel bertanggung jawab untuk mengekspos objek data dari Model sedemikian rupa sehingga objek dapat dengan mudah dikelola dan dipresentasikan.

    Django adalah framework pengembangan web yang mengikuti pola desain MVT (Model-View-Template). Berikut adalah bagaimana Django berhubungan dengan konsep-konsep ini:
    Model: Dalam Django, model adalah representasi dari basis data. Ini adalah tempat saya mendefinisikan struktur data saya, dan Django akan membuat tabel basis data untuk saya.
    View: View dalam Django bertanggung jawab untuk memproses permintaan dan meresponsnya dengan sebuah respons. View mengambil data dari model, menerapkan logika bisnis, dan kemudian meneruskannya ke template.
    Template: Template dalam Django adalah bagian yang menangani bagaimana situs web saya ditampilkan atau bagaimana ia tampak di browser. Template biasanya berisi HTML yang dicampur dengan sintaks template Django.

    Jadi, meskipun Django menggunakan pola MVT, konsep-konsep ini mirip dengan MVC dan MVVM. Dalam semua kasus, tujuannya adalah untuk memisahkan logika aplikasi (Model) dari presentasinya (View/Template) dan bagaimana data diproses (Controller/ViewModel). Perbedaan utama adalah bagaimana kerangka kerja ini mengimplementasikan konsep-konsep ini.

## TUGAS 3
1. Apa perbedaan antara form POST dan form GET dalam Django?
    - Form Post  
    Form POST adalah metode pengiriman data yang digunakan dalam pengembangan web, di mana data atau nilai dikirimkan langsung ke server. Kelebihan dari metode ini adalah data yang dikirimkan tidak ditampilkan di URL, sehingga lebih aman untuk mengirimkan data yang penting atau rahasia, seperti password. Dalam Django, form login dikembalikan menggunakan metode POST, di mana browser mengemas data formulir, mengenkodnya untuk transmisi, mengirimkannya ke server, dan kemudian menerima kembali responsnya. Metode POST menggunakan variabel $_POST untuk menampung data/nilai.  
    <!-- Add an empty line here -->
    Form POST dapat dibayangkan seperti seorang kurir yang mengirimkan paket rahasia. Paket ini dikirim langsung ke tujuan tanpa orang lain tahu apa isinya, karena semua informasi penting disimpan dengan aman di dalam paket dan tidak ditampilkan di luar. Ini seperti saat kita mengirimkan password atau data penting lainnya melalui form login di Django. Browser kita akan mengemas data tersebut, mengenkodnya, dan mengirimkannya langsung ke server.

    - Form Get  
    Di sisi lain, Form GET adalah metode lain yang digunakan dalam pengiriman data formulir. Berbeda dengan form POST, form GET menampilkan data yang dikirimkan dalam URL. Hal ini berarti bahwa data yang dikirimkan dapat dilihat oleh siapa saja yang melihat URL. Dengan metode GET, browser mengemas data yang dikirimkan menjadi string, dan menggunakan ini untuk membuat URL. Meskipun kurang aman dibandingkan dengan metode POST, metode GET sangat berguna untuk mengambil data dari server. Metode GET menggunakan variabel $_GET untuk menampung data/nilai.  
    <!-- Add an empty line here -->
    Form GET seperti seorang pemandu wisata yang membawa kita berkeliling kota. Pemandu wisata ini akan menunjukkan semua tempat yang Anda kunjungi dan semua yang Anda lakukan akan tercatat dalam buku harian perjalanan Anda. Dalam hal ini, buku harian perjalanan adalah URL kita. Semua data yang dikirimkan akan ditampilkan di URL. Meskipun ini mungkin tidak seaman metode POST, metode GET sangat berguna saat kita hanya perlu mengambil data dari server.

2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
    - XML (Extensible Markup Language)  
    XML adalah bahasa markup yang digunakan untuk membuat dokumen yang dapat dibaca oleh manusia maupun mesin. XML biasanya digunakan untuk mengirim data yang kompleks dan sangat terstruktur seperti dokumen atau laporan keuangan. Selain itu, XML juga sering digunakan untuk pertukaran data dalam aplikasi bisnis dan enterprise. XML memerlukan lebih banyak spasi memori daripada JSON, karena XML memiliki tag yang membungkus setiap elemen datanya dan tag tersebut memakan ruang.
    
    - JSON (JavaScript Object Notation)  
    JSON adalah format data ringkas dan ringan yang digunakan untuk pertukaran data antar client dan server. Sama halnya dengan XML, JSON juga dapat digunakan untuk mengirim data yang kompleks seperti struktur data dari REST API2. Meskipun terkesan ringan dan mudah digunakan, JSON memiliki keamanan data yang lebih baik dibandingkan XML. JSON dianggap lebih efisien karena data direpresentasikan sebagai objek JavaScript, dan dengan demikian beberapa bit dilewatkan melalui kabel. Lebih sedikit waktu mesin diperlukan untuk pemrosesan data.

    - HTML (HyperText Markup Language)  
    HTML adalah bahasa markup standar untuk dokumen yang dirancang untuk ditampilkan di browser web. HTML tidak dirancang untuk pertukaran data, tetapi untuk menampilkan data dengan fokus pada bagaimana data tampak bagi pengguna akhir. HTML menggunakan tag untuk membuat elemen seperti teks, gambar, dan hyperlink lainnya menjadi output yang dapat ditampilkan oleh browser web.

3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
    Ada beberapa alasan yang mendasari penggunaan JSON dalam pertukaran data antara aplikasi web modern.
    - Ringan: JSON adalah format yang ringan, yang berarti membutuhkan lebih sedikit bandwidth dan mempercepat waktu transmisi data.
    - Mudah Dibaca dan Ditulis: JSON mudah dibaca dan ditulis oleh manusia, yang memudahkan pengembang dalam memahami dan menganalisis data selama proses pengembangan dan debugging.
    - Mudah Dipahami oleh Mesin: JSON mudah dipahami oleh mesin, yang memungkinkan data JSON diolah dengan mudah di berbagai platform.
    - Fleksibilitas dalam Representasi Data: JSON dapat merepresentasikan berbagai jenis data dengan format yang konsisten, termasuk tipe data dasar seperti string, angka, boolean, serta struktur yang lebih kompleks seperti objek dan array.
    - Kompatibilitas Lintas Platform: JSON didukung oleh sebagian besar bahasa pemrograman modern, sehingga data dalam format JSON dapat dengan mudah diolah dan dimanipulasi di berbagai platform dan lingkungan.
    - Efisiensi dalam Pertukaran Data: Karena format JSON bersifat ringan dan terstruktur, data dapat dikirim dengan cepat melalui jaringan dan diurai dengan mudah oleh klien.
    - Struktur Kode yang Lebih Sederhana: Berbeda dengan XML dan format lainnya yang memiliki fungsi serupa, JSON memiliki struktur data yang sederhana dan mudah dipahami.
    - Pertukaran Data yang Efisien: Salah satu fungsi utama JavaScript Object Notation adalah untuk memfasilitasi pertukaran data yang efisien antara server dan klien.

    Secara keseluruhan, JSON adalah format data yang kuat dan serbaguna yang cocok untuk berbagai aplikasi, termasuk pertukaran data antara aplikasi web modern.

4.  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step
    - Membuat Forms.py dan Mendefinisikan Form  
    Pertama, saya akan membuat file forms.py dalam proyek web saya. Di sini, saya mendefinisikan sebuah form yang akan digunakan untuk mengambil input dari pengguna. Form ini biasanya mengambil atribut dari model yang telah saya definisikan dalam models.py. Ini memungkinkan saya untuk mengumpulkan data dari pengguna.
    - Migrasi Basis Data  
    Sebelum saya dapat menggunakan model baru atau menerapkan perubahan lainnya pada basis data, saya perlu menjalankan perintah migrate untuk memigrasikan perubahan tersebut ke dalam basis data.   
    - Membuat Fungsi untuk Merender Formulir  
    Selanjutnya, saya akan membuat fungsi di dalam file views.py yang saya sebut create_product. Fungsi ini bertujuan untuk merender tampilan formulir yang telah saya buat sebelumnya. Ini memungkinkan pengguna untuk mengisi formulir dan menambahkan produk baru ke dalam basis data.
    - Membuat Template HTML untuk Formulir  
    Saya akan membuat sebuah file HTML yang akan digunakan sebagai template untuk formulir yang akan dirender oleh fungsi create_product. Dalam file HTML ini, saya akan menambahkan kode HTML yang sesuai untuk menampilkan formulir dengan bidang yang diperlukan.
    - Membuat Tombol atau Tautan pada Halaman Utama  
    Di dalam file HTML utama saya, saya akan menambahkan tombol atau tautan yang akan mengarahkan pengguna ke halaman yang berisi formulir untuk menambahkan produk.    
    - Membuat Fungsi untuk Format XML dan JSON  
    Saya akan membuat empat fungsi tambahan di dalam views.py untuk menampilkan data dalam format XML dan JSON. Fungsi-fungsi ini akan menggunakan serializer untuk mengubah data dari basis data ke dalam format XML dan JSON sesuai dengan kebutuhan.
    - Fungsi untuk Data per ID  
    Untuk mengambil data berdasarkan ID tertentu, saya akan membuat fungsi yang serupa dengan fungsi sebelumnya untuk melihat data dalam format XML dan JSON. Namun, kali ini saya akan menerapkan filter untuk mengambil data berdasarkan primary key (ID) yang diinginkan.
    - Routing URL  
    Setelah membuat fungsi-fungsi tersebut, saya akan menambahkan rute (URL) untuk masing-masing fungsi ke dalam file urls.py. Ini akan mengaitkan URL dengan fungsi yang sesuai dalam views.py.
    - Pengujian Lokal  
    Setelah melakukan routing, saya dapat menguji masing-masing fungsi dengan menjalankan aplikasi saya secara lokal di komputer. Saya akan mengakses halaman-halaman yang telah saya buat untuk melihat, menambahkan, dan mengakses data dalam format HTML, XML, dan JSON sesuai dengan fungsinya.

    Screnshoot:
    - HTML Main:
    ![Screenshot HTML Gyan](https://github.com/Gyan-Bano/tugas-pbp-gyan/assets/124954416/d3a2d281-200e-48cb-b16b-e17623cab880)
    - HTML Create Product:
    ![Screenshot HTML Create Product Gyan](https://github.com/Gyan-Bano/tugas-pbp-gyan/assets/124954416/cf6bd52d-172d-44e9-b44d-0d7206696769)
    - XML:
    ![Screenshot XML Gyan](https://github.com/Gyan-Bano/tugas-pbp-gyan/assets/124954416/895e299c-9ecf-4fc7-8760-a58be0672724)
    - JSON:
    ![Screenshot JSON Gyan](https://github.com/Gyan-Bano/tugas-pbp-gyan/assets/124954416/af27aeb3-0546-46c0-8af9-25cbee382947)
    - XML ID:
    ![Screenshot XML Gyan ID](https://github.com/Gyan-Bano/tugas-pbp-gyan/assets/124954416/97fc40ef-d572-4db8-a8ca-cd2890773929)
    - JSON ID:
    ![Screenshot JSON Gyan ID](https://github.com/Gyan-Bano/tugas-pbp-gyan/assets/124954416/eab23c67-7ee1-472a-a6cb-400bb49b0f6e)

## TUGAS 4
Untuk tugas 4 saya membuat dua akun:
- Akun pertama, username: testakun1, password: Abcd1234!, Akun inventori ini berisi buku kalkulus purcell.
- Akun pertama, username: testakun2, password: ABcd1234!, Akun inventori ini berisi buku laskar pelangi dan buku harry potter dan batu bertuah.
1. Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
Django UserCreationForm adalah formulir yang digunakan untuk membuat pengguna baru dalam aplikasi web Django. Formulir ini terdiri dari tiga bidang yang meliputi username, password1, dan password2 (pada dasarnya digunakan untuk konfirmasi dari password1).

Kelebihan:
- Django UserCreationFOrm adalah bagian dari sistem otentikasi pengguna bawaan Django yang dirancang untuk memenuhi kebutuhan umum proyek.
- Formulir ini memudahkan pembuatan pengguna baru dengan otentikasi dan validasi password.
- Django UserCreationForm memiliki fungsi save() yang memungkinkan penyimpan instance pengguna ke dalam database.
- Validasi yang kuat. Django UserCreationForm melakukan validasi yang kuat terhadap input pengguna, seperti memastikan bahwa password memiliki panjang minimal 8 karakter dan tidak mengandung karakter khusus.

Kekurangan: 
- Tidak dapat digunakan untuk membuat pengguna dengan model custom. Jika kita menggunakan model custom untuk pengguna, maka kita perlu membuat form custom sendiri.
- Tidak dapat digunakan untuk membuat pengguna dengan izin khusus. Jika kita ingin membuat pengguna dengan izin khusus, maka kita perlu menambahkan kode tambahan ke aplikasi.

2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
Autentikasi adalah proses verivikasi identitas pengguna. Autentikasi akan memastikan bahwa pengguna adalah siapa saja yang mereka klaim. Misalkan ketika pengguna mencoba masuk untuk login ke aplikasi web, sistem akan meminta username dan password. Sistem kemudian akan memeriksa apakah kombinasi username dan password pengguna tersebut valid.

Di sisi lain, otorisasi adalah proses penentuan apa yang dapat dilakukan oleh pengguna yang telah diautentikasi sebelumnya. Misalnya, beberapa pengguna mungkin memiliki izin untuk mengakses halaman tertentu ataupun melakukan tindakan tertentu (seperti mengedit atau menghapus objek dari inventori), sementara pengguna lain mungkin tidak.

Kedua konsep ini penting karena mereka membantu menjaga keamanan aplikasi web. Autentikasi membantu mencegah akses yang tidak sah dengan memastikan bahwa hanya pengguna yang memiliki kredensial yang valid yang dapat masuk ke sistem. Sementara itu, otorisasi membantu mencegah penyalahgunaan sistem dengan membatasi apa yang dapat dilakukan oleh setiap pengguna.

3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?

Cookie adalah file teks kecil yang disimpan di komputer pengguna oleh situs web yang mereka kunjungi. Cookie dapat digunakan untuk menyimpan berbagai macam informasi, seperti pengaturan pengguna, preferensi, atau status login.

Dalam konteks aplikasi web, cookie dapat digunakan untuk mengelola data sesi pengguna. Sesi adalah periode waktu di mana pengguna berinteraksi dengan situs web. Selama sesi, pengguna dapat melakukan berbagai tindakan, seperti login, menambahkan item ke keranjang belanja, atau membuat komentar.

Django menggunakan cookie untuk menyimpan ID sesi pengguna. ID sesi adalah nilai unik yang digunakan untuk mengidentifikasi pengguna selama sesi. Django menggunakan ID sesi untuk menyimpan informasi tentang pengguna, seperti status login, pengaturan, dan preferensi. Berikut adalah contoh Django menggunakan cookie untuk mengelola data sesi pengguna:
- Saat pengguna login, Django akan membuat ID sesi baru dan menyimpannya di cookie.
- Setiap kali pengguna mengirimkan permintaan ke situs web, Django akan memeriksa cookie untuk ID sesi.
- Jika ID sesi ditemukan, Django akan menggunakan ID sesi tersebut untuk mengidentifikasi pengguna.
- Django akan menggunakan ID sesi untuk menyimpan informasi tentang pengguna, seperti status login, pengaturan, dan preferensi.

Dengan menggunakan cookie, Django dapat mengelola data sesi pengguna dengan cara yang efisien dan aman.

4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
Penggunaan cookie secara default relatif aman dalam pengembangan web, tetapi ada beberapa risiko potensial yang harus diwaspadai, antara lain:
- Kebocoran data, cookie dapat berisi informasi yang sensitif misalkan nama pengguna, kata sandi, atau informasi sensitif lainnya. Jika cookie diretas, informasi sensitif ini dapat jatuh ke tangan orang yang tidak berwenang, terutama saat dikirimkan dengan koneksi HTTP yang tidak aman. 
- Pelacaakan pengguna, cookie dapat digunakan untuk melacak perilaku pengguna pada situs web. Pelacakan ini dapat digunakan untuk menargetkan iklan atau untuk mengumpulkan data tentang pengguna. 
- Keamanan, cookie rentan terhadap serangan seperti cross-site scripting (XSS) dan session hijacking.
Oleh karena itu, ada beberapa cara untuk menggunakan cookie secara aman:
- Gunakan cookie hanya untuk menyimpan informasi yang diperlukan.
Mengenkripsi cookie, gunakan prokol enkripsi yang kuat, seperti HTTPS, untuk melindungi cookie dari penyadapan.
5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- Membuat fungsi Register: Untuk membuat fungsi registrasi, hal pertama yang saya lakukan adalah menambahkan beberapa import library, salah satunya UserCreationForm pada view.py di directory main,lalu saya membuat fungsi register di dalamnya.
```
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```
Fungsinya adalah untuk memungkinkan pembuatan akun pengguna setelah pengguna mengeklik tombol "submit" di halaman web. Setelah menambahkan fungsi ini, langkah selanjutnya adalah membuat berkas HTML yang disebut register.html dalam direktori main/templates untuk mengatur tampilan halaman pendaftaran. Langkah terakhir adalah menghubungkan jalur (path) dalam file "urls.py" yang terletak di direktori main"dengan fungsi pendaftaran tersebut.
- Membuat fungsi Login: Selanjutnya saya melanjutkan dengan membuat fungsi login dengan import library authenticate dan login  yang juga dilakukan pada views.py.
```
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:show_main')
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
```

Fungsinya adalah untuk memungkinkan pengguna untuk login dengan mengidentifikasi mereka melalui nama pengguna dan kata sandi yang mereka masukkan. Setelah itu, saya membuat berkas HTML bernama login.html di dalam folder main/templates untuk mengatur tampilan halaman login. Terakhir, saya menambahkan jalur (path) dalam file urls.py di direktori main yang mengarah ke fungsi login tersebut.

Agar hanya pengguna yang sudah login yang dapat mengakses halaman utama, saya menambahkan aturan dengan menggunakan @login_required(login_url='/login').

- Membuat fungsi Logout: 
Untuk membuat fungsi logout, langkah-langkahnya serupa dengan pembuatan fungsi Register, yaitu dengan mengimpor library logout ke dalam views.py.
```
def logout_user(request):
    logout(request)
    return redirect('main:login')
```

Kemudian, saya membuat fungsi logout di views.py yang berperan dalam menghapus sesi login pengguna dan mengalihkan mereka kembali ke halaman login. Pada halaman utama (main page), saya menambahkan tombol logout. Terakhir, saya menambahkan jalur (path) dalam file urls.py di direktori "main" yang menghubungkan ke fungsi logout ini.
- Menggunakan cookies untuk last login: Dalam fungsi show_main di views.py, saya mengubah bagian "Name" dalam konteks menjadi request.user.username untuk membuat nama di halaman utama menjadi dinamis dan sesuai dengan pengguna yang terotorisasi. Selanjutnya, untuk menerapkan cookies yang berisi informasi waktu terakhir login di halaman utama, saya menambahkan kode response.set_cookie('last_login', str(datetime.datetime.now())). Hal ini bertujuan untuk membuat dan menambahkan cookie bernama last_login pada respons.

Selain itu, saya juga memodifikasi fungsi logout_user untuk menghapus cookie last_login saat pengguna logout. Terakhir, untuk menampilkan data waktu terakhir login di halaman utama, saya memodifikasi berkas main.html dan menambahkan data last_login ke dalam konteks pada fungsi show_main.
- Menghubungkan product dengan user: Tujuannya dalam menghubungkan Item dengan User adalah untuk memastikan bahwa setiap pengguna hanya memiliki akses ke Item yang mereka tambahkan ke dalam akun mereka sendiri. Dalam berkas models.py, saya menambahkan kode user = models.ForeignKey(User, on_delete=models.CASCADE) yang digunakan untuk membuat koneksi antara satu pengguna dengan Item, sehingga Item yang dikaitkan dengan pengguna tersebut dapat diidentifikasi sebagai milik pengguna yang melakukan permintaan untuk menambahkan produk.

Selanjutnya pada views.py untuk memfilter produk saya menambahkan kode  products = Product.objects.filter(user=request.user) agar produk yang muncuk sesuai dengan akun user, lalu pada fungsi create_product dimodifikasi dengan kode 
```
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('main:show_main')  
    else:
        form = ProductForm()
    
    context = {'form': form}
    return render(request, 'create_product.html', context)
```
- Pengumpulan: Setelah saya melakukan semua langkah - langkah tersebut untuk membuat mekanisme login, logout, pembuatan akun, serta penggunaan cookies saya melakukan add, commit, dan push ke repositori github yang saya buat pada branch baru.

## TUGAS 5
1. Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.
Dalam CSS, selector digunakan untuk memilih elemen HTML yang ingin kita beri style. Ada beberapa jenis selector, dan berikut adalah penjelasan dan manfaat dari masing-masing:
- Element Selector: Selector ini memilih elemen berdasarkan nama elemen HTML. Misalnya, p { color: red; } akan menerapkan warna merah ke semua elemen <p>. Manfaatnya adalah dapat mengubah style semua elemen dengan jenis yang sama sekaligus. Ini dapat digunakan saat kita ingin menerapkan style yang sama ke semua elemen dengan jenis yang sama.
- Class Selector: Selector ini memilih elemen berdasarkan nilai atribut class. Misalnya, .myClass { color: red; } akan menerapkan warna merah ke semua elemen dengan class “myClass”. Manfaatnya adalah dapat mengubah style beberapa elemen sekaligus tanpa harus sama jenisnya.Ini dapat digunakan saat kita ingin menerapkan style yang sama ke beberapa elemen yang berbeda.
- ID Selector: Selector ini memilih elemen berdasarkan nilai atribut id. Misalnya, #myID { color: red; } akan menerapkan warna merah ke elemen dengan id “myID”. Manfaatnya adalah dapat mengubah style satu elemen spesifik. Ini dapat digunakan saat kita ingin menerapkan style khusus ke satu elemen saja.
- Attribute Selector: Selector ini memilih elemen berdasarkan atribut dan nilai atributnya. Misalnya, input[type="text"] { color: red; } akan menerapkan warna merah ke semua elemen input dengan tipe “text”. Manfaatnya adalah dapat mengubah style elemen berdasarkan atributnya. Ini dapat digunakan saat kita ingin menerapkan style ke elemen dengan atribut tertentu.
- Pseudo-class Selector: Selector ini memilih elemen berdasarkan status tertentu, seperti hover, focus, atau checked. Misalnya, a:hover { color: red; } akan menerapkan warna merah ke link saat mouse diarahkan ke atasnya. Manfaatnya adalah dapat mengubah style elemen berdasarkan interaksi pengguna atau status tertentu. Ini dapat digunakan saat kita ingin memberikan feedback visual kepada pengguna saat mereka berinteraksi dengan elemen.
- Pseudo-element Selector: Selector ini memilih bagian spesifik dari elemen, seperti ::before atau ::after. Misalnya, p::first-line { color: red; } akan menerapkan warna merah ke baris pertama dari setiap paragraf. Manfaatnya adalah dapat mengubah style bagian spesifik dari suatu elemen. Ini dapat digunakan saat kita ingin menambah atau mengubah style bagian tertentu dari suatu elemen.
2. Jelaskan HTML5 Tag yang kamu ketahui.
Berikut adalah beberapa contoh dari HTML5 Tag yang sering digunakan dalam pengembangan web:
- ```<!DOCTYPE html>```: Ini bukan tag sebenarnya, tetapi deklarasi dokumen yang digunakan untuk menandakan bahwa halaman web adalah halaman HTML5. Ini diletakkan di bagian atas halaman HTML.
- ```<html>```: Tag ini membungkus seluruh halaman HTML dan menandakan awal dari dokumen HTML.
- ```<head>```: Bagian ini berisi informasi meta mengenai halaman, tautan ke file eksternal (seperti CSS dan JavaScript), judul halaman, dan informasi metadata lainnya.
- ```<meta>```: Digunakan untuk menyisipkan metadata ke dalam halaman web, seperti karakter encoding, deskripsi halaman, dan panduan penjelajahan.
- ```<title>```: Digunakan untuk menentukan judul halaman web yang akan ditampilkan di bilah judul browser atau tab.
- ```<link>```: Digunakan untuk menghubungkan dokumen HTML dengan file eksternal, seperti file CSS untuk styling.
- ```<style>```: Ini adalah tag yang digunakan untuk menambahkan CSS langsung ke dalam halaman HTML. Biasanya ditempatkan dalam bagian ```<head>```.
- ```<script>```: Tag ini digunakan untuk menambahkan kode JavaScript ke dalam halaman HTML.
- ```<body>```: Bagian utama halaman web yang berisi konten yang akan ditampilkan kepada pengguna, seperti teks, gambar, tautan, dan elemen-elemen lainnya.
- ```<header>```: Ini adalah elemen yang biasanya digunakan untuk bagian atas halaman atau bagian kepala halaman web, yang sering berisi judul, logo, tautan navigasi, dan elemen-elemen lainnya.
- ```<nav>```: Digunakan untuk mengelompokkan tautan navigasi ke dalam sebuah menu. Biasanya digunakan di bagian header atau footer.
- ```<main>```: Menunjukkan konten utama dalam halaman web, yang harus ada dalam setiap halaman HTML5.
- ```<h1>``` sampai ```<h6>```: Mendefinisikan judul.
- ```<p>```: Mendefinisikan paragraf.
- ```<a>```: Membuat hyperlink.
- ```<section>```: Digunakan untuk mengelompokkan konten yang memiliki hubungan tematik dalam halaman, seperti bab dalam buku atau blok artikel dalam blog.
- ```<article>```: Mendefinisikan sebuah artikel independen yang dapat berdiri sendiri dalam halaman web, seperti sebuah posting blog atau berita.
- ```<img>```: Digunakan untuk menambahkan gambar.
- ```<video>``` dan ```<audio>```: Digunakan untuk menambahkan media video dan audio.
- ```<aside>```: Digunakan untuk konten yang terkait dengan konten di sekitarnya, tetapi bukan bagian integral dari konten utama, seperti sidebar.
- ```<footer>```: Biasanya digunakan di bagian bawah halaman web dan berisi informasi penulis, tautan ke halaman terkait, atau informasi hak cipta.
- ```<table>```: Digunakan untuk membuat tabel.
- ```<div>```: Meskipun ini bukan elemen HTML5, ```<div>``` masih sering digunakan untuk mengelompokkan dan mengatur elemen-elemen HTML untuk tujuan styling dan pemrograman.
3. Jelaskan perbedaan antara margin dan padding.
Margin dan padding adalah dua properti penting dalam CSS yang digunakan untuk mengatur tata letak elemen-elemen HTML di dalam halaman web. Mereka memiliki perbedaan yang signifikan dalam cara mereka memengaruhi tata letak elemen-elemen tersebut:
Margin:
- Margin adalah jarak di luar elemen: Margin adalah ruang di luar batas luar elemen HTML. Margin digunakan untuk mengatur jarak antara elemen tersebut dan elemen-elemen di sekitarnya, baik vertikal maupun horizontal.
- Margin tidak memiliki latar belakang atau warna: Margin adalah area transparan, yang berarti elemen-elemen di belakangnya akan terlihat melalui area margin. Kita tidak dapat memberikan warna atau latar belakang pada margin.
Padding:
- Padding adalah ruang di dalam elemen: Padding adalah ruang di dalam batas elemen HTML. Padding digunakan untuk mengatur jarak antara konten elemen dan batasnya sendiri, baik vertikal maupun horizontal.
- Padding dapat memiliki latar belakang atau warna: Padding adalah area yang dapat memiliki warna atau latar belakang. Kita dapat memberikan warna atau latar belakang pada padding, yang akan mempengaruhi area di sekitar konten elemen.
Perbedaan utama antara margin dan padding adalah lokasi mereka di sekitar elemen dan apakah mereka dapat memiliki latar belakang atau tidak. Margin digunakan untuk mengatur jarak di luar elemen, sementara padding digunakan untuk mengatur jarak di dalam elemen. Kita dapat memanfaatkan keduanya secara bersamaan untuk mengontrol tata letak dan tampilan elemen-elemen di halaman web Kita.
4. Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
Tailwind CSS dan Bootstrap adalah dua framework CSS yang populer dan sering digunakan dalam pengembangan web. Mereka memiliki pendekatan yang berbeda dalam cara mereka memungkinkan pengembang untuk merancang tampilan dan tata letak halaman web. 
Tailwind CSS:
Konsep Dasar: Tailwind CSS adalah framework CSS "utility-first," yang berarti ia memberikan sejumlah besar kelas utilitas yang memungkinkan kita merancang tampilan dengan menggabungkan kelas-kelas ini dalam HTML. kita membangun tampilan dari komponen-komponen kecil menggunakan kelas-kelas ini.

Kustomisasi yang Lebih Luas: Tailwind memungkinkan tingkat kustomisasi yang lebih besar dibandingkan dengan Bootstrap. Kita dapat dengan mudah menyesuaikan tampilan dengan mengedit file konfigurasi Tailwind atau menambahkan kelas-kelas tambahan.

Ukuran yang Lebih Kecil: Tailwind cenderung menghasilkan ukuran file CSS yang lebih kecil dibandingkan dengan Bootstrap karena hanya mengompilasi kelas yang digunakan dalam proyek kita.

Kesulitan Pembelajaran: Tailwind memiliki kurva pembelajaran yang mungkin lebih tinggi karena kita perlu memahami banyak kelas utilitas dan cara menggabungkannya.

Bootstrap:

Komponen yang Lebih Kaya: Bootstrap menyediakan kumpulan komponen siap pakai, seperti navbar, card, modal, dll. Ini mempermudah pengembangan jika kita ingin menggunakan komponen-komponen ini tanpa harus merancang ulang.

Desain Responsif: Bootstrap dirancang dengan responsif dalam pikiran dan menyediakan grid system yang kuat serta kelas-kelas yang mendukung tata letak responsif.

Keseluruhan Desain yang Konsisten: Bootstrap menyediakan desain yang konsisten dan estetika yang baik secara default. Ini bisa menjadi pilihan yang baik jika kita ingin tampilan yang konsisten tanpa banyak penyesuaian.

Kurva Pembelajaran yang Lebih Cepat: Bootstrap mungkin memiliki kurva pembelajaran yang lebih cepat karena kita perlu memahami lebih sedikit kelas-kelas daripada Tailwind.

Kapan sebaiknya menggunakan Bootstrap:
- Jika kita membutuhkan komponen-komponen yang kaya dan siap pakai.
- Jika kita ingin desain yang konsisten dan estetika yang baik tanpa banyak penyesuaian.
- Jika kita ingin pengembangan yang lebih cepat dengan kurva pembelajaran yang lebih mudah.
Kapan sebaiknya menggunakan Tailwind CSS:
- Jika kita ingin tingkat kustomisasi yang tinggi dan lebih kontrol atas tampilan kita.
- Jika kita ingin menghasilkan ukuran file CSS yang lebih kecil.
- Jika kita siap untuk memahami dan menggunakan kelas-kelas utilitas yang banyak.
- Pilihan antara Tailwind CSS dan Bootstrap tergantung pada kebutuhan proyek kita, tingkat kustomisasi yang kita butuhkan, dan preferensi pribadi kita dalam pengembangan web.
5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Dikarenakan pada tugas sebelumnya saya sudah menambahkan beberapa fitur seperti delete product serta penambahan serta pengurangan item stock, pada tugas ini saya melanjutkannya dengan beberapa hal yang dimulai dari:
- Penambahan Framework Bootstrap: Saya memulai dengan menambahkan framework Bootstrap ke seluruh halaman aplikasi. Hal ini dilakukan dengan memasukkan tautan ke file CSS dan JavaScript Bootstrap di dalam tag ```<head>```.
- Penyusunan Konten yang Lebih Menarik: Selanjutnya, saya mengatur ulang tampilan konten pada setiap halaman agar terlihat lebih menarik. Dengan menggunakan kelas-kelas Bootstrap, seperti margin dan padding, saya memberikan tampilan yang lebih terstruktur dan estetis pada halaman-halaman tersebut.
- Penggantian Tabel dengan Card: Untuk meningkatkan tampilan aplikasi, saya memutuskan untuk mengganti elemen tabel yang sebelumnya digunakan dengan elemen card dari Bootstrap. Ini memberikan tampilan yang lebih modern, bersih, dan lebih sesuai dengan tren desain saat ini.
- Pemberian Warna pada Inventori Terakhir: Agar objek inventori terakhir lebih mudah dikenali, saya menambahkan logika untuk memberikan warna berbeda pada card tersebut. Dengan menggunakan {% if forloop.last %}...{% endif %}, saya menerapkan properti-properti CSS khusus ke card terakhir dalam daftar.
- Penambahan Navbar: Untuk meningkatkan navigasi dan kenyamanan pengguna, saya menambahkan navbar ke setiap halaman, kecuali halaman login dan registrasi. Navbar ini menyediakan akses cepat ke berbagai fitur penting seperti tombol log out dan tombol tambah koleksi buku.
- Penggunaan JavaScript untuk Toggle Informasi Tambahan: Terakhir, saya menggunakan JavaScript untuk membuat tombol "Show More" yang dapat mengontrol visibilitas informasi tambahan pada setiap card. Dengan mengklik tombol ini, pengguna dapat dengan mudah melihat atau menyembunyikan detail tambahan, serta tampilan card akan lebih bersih karena tidak semua elemen langsung ditampilkan diawal.