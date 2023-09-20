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




