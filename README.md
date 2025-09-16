Nama   : Pria Abhirama Dewa
NPM    : 2406358043
Kelas  : PBP D
Tautan : https://pria-abhirama-dribblezone.pbp.cs.ui.ac.id/

TUGAS 2
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)
    Pertama kita nyalain dulu python env nya lalu membuat project django baru dengan django-admin startproject (nama project) lalu kita semua terlebih dahulu seperti allowed host,env prod,env,database dan pws nya , setelah itu kita buat django start app main dan mengganti models dengan apa yag disuruh lalu kita routing main agar bisa dijalankan setelah itu kita buat fungsi dalam views untuk menampilkan nama apps dll setelah itu kita deploy ke pws

    Pertama, saya membuat direktori lokal dan repository github bernama dribble-zone, kemudian membuat virtual environment untuk mengisolasi proyek dari proyek lain. Lalu, saya melakukan instalasi dependencies yang dibutuhkan dan membuat proyek Django. Selanjutnya, saya menambahkan konfigurasi untuk development lokal dan production deployment melalui file .env dan .env.prod, serta memodifikasi settings.py untuk pengaturan perizinan akses.

    Setelah itu, saya membuat aplikasi main di direktori dribble-zone dengan menjalankan perintah python manage.py startapp main. Pada aplikasi main, saya membuat direktori templates dan menambahkan file main.html untuk kebutuhan Tugas 2. Kemudian, saya menambahkan konfigurasi routing di urls.py untuk aplikasi main, serta membuat fungsi show_main di views.py yang menampilkan template main.html berisi nama aplikasi, nama, dan kelas. Untuk melengkapinya, saya juga membuat file urls.py guna memetakan fungsi show_main ke aplikasinya.

    Selanjutnya saya membuat model Product dengan atribut berupa name (CharField), price (IntegerField), description (TextField), thumbnail (URLField), category (CharField), dan is_featured (BooleanField). Setelah model selesai dibuat, saya membuat project baru di PWS dan menyesuaikan environment dengan .env.prod. Pada settings.py, saya menambahkan URL deployment pria-abhirama-dribblezone.pbp.cs.ui.id. Setelah konfigurasi selesai, saya menjalankan perintah python manage.py makemigrations dan python manage.py migrate untuk mempersiapkan database. Terakhir, saya menyambungkan repository dengan PWS, menjalankan project command, melakukan build, dan melakukan push dengan perintah git push pws master untuk deployment.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
    Ketika client mengirimkan sebuah HTTP request ke server Django, permintaan tersebut akan diproses dengan mencocokkan URL yang diminta terhadap pola yang sudah didefinisikan di dalam file urls.py. File ini berfungsi sebagai pengatur route yang menghubungkan URL dengan fungsi di aplikasi 'main'. Setelah URL sesuai ditemukan, request diteruskan ke views.py, yang bertugas mengelola logika seperti sebuah fungsi. Pada tahap ini, views.py dapat mengambil atau memanipulasi data melalui models.py, yang merupakan komponen untuk mengatur serta mengelola data aplikasi melalui database. Setelah memperoleh data yang dibutuhkan, views.py akan merender template HTML dengan data tersebut, sehingga menghasilkan tampilan akhir yang siap dikirimkan ke client. Hasil akhirnya berupa response HTML yang telah diproses oleh Django dan ditampilkan di browser client.

    (https://drive.google.com/file/d/1U68KEgUZgsqV4Joz45wpokbj2RSpB0kc/view?usp=sharing)

3. Jelaskan peran settings.py dalam proyek Django!
    Setting.py mendefinisikan koneksi ke database, mendaftarkan semua aplikasi yang aktif (INSTALLED_APPS), dan mengelola pengaturan keamanan krusial seperti SECRET_KEY dan DEBUG. Selain itu, file ini juga mengontrol bagaimana template (HTML) ditemukan dan di-render, menangani lokasi file statis (CSS, JavaScript), dan menentukan konfigurasi URL utama, sehingga secara efektif menjadi pusat kendali yang menentukan seluruh perilaku dan arsitektur aplikasi web.

4. Bagaimana cara kerja migrasi database di Django?
    Migrasi di Django adalah proses untuk menjaga agar struktur database selalu sesuai dengan definisi model yang ada di aplikasi. Setiap kali models.py ditambahkan, diubah, atau ada atribut yang dihapus, Django tidak langsung mengubah database, tetapi menyimpannya dulu sebagai perubahan skema. Dengan perubahan itu kemudian diterjemahkan menjadi file migration, seperti catatan yang isinya instruksi tentang apa yang harus dilakukan pada database. Setelah file migrasi dibuat dengan perintah python manage.py makemigrations, langkah berikutnya adalah menerapkan perubahan tersebut ke database dengan perintah python manage.py migrate.

    Cara kerja migrasi di Django dapat dipahami sebagai jembatan antara kode Python pada models.py dengan struktur di dalam database. Ketika perintah python manage.py makemigrations dijalankan, Django akan membandingkan kondisi model saat ini dengan migrasi sebelumnya, lalu membuat file migrasi baru yang berisi perubahan dari sebuah model. File migrasi tersebut belum memengaruhi database, melainkan hanya mendokumentasikan rencana perubahan. Setelah itu, saat kita menjalankan python manage.py migrate, Django mengeksekusi isi file migrasi tersebut dengan menghasilkan query SQL yang sesuai dengan database yang digunakan, lalu menerapkannya langsung ke dalam database. Dengan cara tersebut, setiap perubahan data model tercatat, dapat dikelola bertahap, dan bisa di-rollback atau dijalankan ulang bila diperlukan.

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
    Menurut saya framework Django merupakan salah satu framework yang beginner-friendly. Selain itu, python juga sudah dipelajarai sejak semester 1. Strukturnya juga jelas dengan pola MVT (Model-View-Template) sehingga membantu pemula memahami pemisahan tugas dalam kode. Django juga merupakan framework full-stack yang dapat digunakan untuk mengembangkan sisi backend sekaligus menyediakan frontend melalui HTML. Hal tersebut membuat Django cocok sebagai langkah awal untuk memahami pengembangan perangkat lunak secara menyeluruh.

6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
    Tidak ada, asisten dosen tutorial 1 telah menjalankan perannya dengan sangat baik.

TUGAS 3
1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
    Dalam pengimplementasian sebuah platform, data delivery diperlukan untuk menjamin informasi yang disampaikan antar komponen sistem berjalan dengan sesuai. Komunikasi client-server dapat terjadi juga melalui data delivery yang memungkinkan pertukaran informasi antara frontend dan backend. Selain itu, data delivery juga penting untuk menjaga keamanan data serta memungkinkan integrasi sistem, yaitu tepatnya komunikasi antar microservices.

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
    Menurut saya, secara umum JSON lebih baik daripada XML karena sintaks yang lebih sederhana dan ukuran file yang lebih ringan sehingga mempercepat pertukaran data. Sementara, XML sintaksnya lebih rumit karena banyak tag yang membuatnya kurang enak saat dibaca. Kelebihan JSON tersebut juga lah yang membuatnya lebih populer dibanding XML. Selain itu, kemudahan penggunaan JSON dan dukungan yang luas di API modern membuat JSON lebih populer dibandingkan XML.  

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
    is_valid() merupakan method bawaan Django untuk form validation yang berperan dalam memeriksa apakah data yang diinput sesuai dengan aturan validasi yang telah ditentukan, baik validasi bawaan maupun validasi kustom yang kita definisikan sendiri. Jika data valid, method akan mengembalikan true, vice versa. Kita membutuhkan method is_valid() untuk menjamin data yang masuk konsisten, tidak salah format, dan tidak berpotensi menimbulkan bug serta celah keamanan.

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
    CSRF token adalah mekanisme keamanan yang penting dalam pengembangan berbasis platform. CSRF token akan menggenerate token unik untuk setiap session dan token disisipkan dalam form sebagai hidden fild kemudian server akan memverifikasi token saat menerima request POST. Tanpa CSRF token, penyerang dapat memanfaatkan celah keamanan untuk melakukan serangan Cross-Site Request Forgery (CSRF), yaitu serangan dimana penyerang mencoba membuat pengguna yang sudah login melakukan aksi tanpa sadar (misalnya mengirim form atau melakukan transaksi) melalui permintaan palsu. Oleh karena itu, CSRF token penting untuk memastikan form submission berasal dari situs yang sah dan melindungi dari request palsu situs lain.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    Pertama, saya membuat sebuah ProductForm yang nantinya digunakan sebagai form input saat menambahkan produk baru ke dalam sistem. Form tersebut kemudian dihubungkan dengan template create_product.html agar pengguna bisa mengisi data produk ketika ingin menambahkan produk. Selanjutnya, saya mengedit main.html agar dapat menampilkan daftar semua produk yang tersimpan beserta informasi pentingnya, lalu menambahkan product_detail.html untuk menampilkan detail lengkap dari sebuah produk tertentu. Selain itu, saya menambahkan fungsi pada views.py untuk menangani proses pembuatan produk baru serta fungsi lain untuk menyajikan data produk dalam format JSON maupun XML sehingga lebih fleksibel jika data ingin diakses sebagai API. Demi keamanan, saya menambahkan pengaturan CSRF_TRUSTED_ORIGINS agar form hanya menerima input dari sumber tepercaya dan tidak mudah dieksploitasi penyerang. Terakhir, saya membuat template utama base.html sebagai kerangka dasar agar semua halaman memiliki struktur yang konsisten dan lebih mudah dikelola.

6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
    Tidak ada, asisten dosen tutorial 2 telah menjalankan perannya dengan sangat baik.

7. Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md
    (https://drive.google.com/drive/folders/1mOFxfkNjR8Zsp0B7s7V_Ib51Kiu8yL_w?usp=sharing)