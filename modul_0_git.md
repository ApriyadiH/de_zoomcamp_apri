# Modul 0 Git dan Github
## 1. Teori
### Git
Git adalah alat untuk mengatur versi dari suatu aplikasi. Bahasa inggrisnya adalah __Version Control__. Aplikasi yang mengatur versi disebut juga Version Control System (VCS)

Link Dokumentasi: [Dokumentasi Git](https://git-scm.com/doc)
Link belajar lainnya:
- [Web Programming Unpas](https://www.youtube.com/playlist?list=PLFIM0718LjIVknj6sgsSceMqlq242-jNf)

### Versi/Version
Dalam mengembangkan software, terkadang kita terus mengetik dan terjadi kesalahan yang fatal. Sialnya Undo tidak dapat menyelamatkannya. Dari kejadian tersebut, kita mulai membuat copy-an file sebagai back-up. Jika suatu hari terjadi kecelakaan lagi, kita dapat menyalin ulang file back-up. 

File copy-an biasanya diberi nama khusus untuk membedakan file yg lebih tua dan yg lebih baru. Biasanya dengan angka. Misalnya v1.0.0. Hal inilah yang disebut dengan __versi__.

### Github
__Github__ adalah platform untuk berbagi Repository dan kolaborasi developer. Github juga memiliki berbagai fitur lainnya seperti membuat halaman statis (bisa digunakan untuk membuat halaman portfolio).

### Gabungan Git + Github
Git dan Github merupakan __dua hal yang berbeda__. Kamu dapat menggunakan Git dan Github secara terpisah. Tetapi dengan menggabungkan keduanya, prosesnya akan jauh lebih baik. Git memungkinkan kita menggunakan perintah Git di terminal dan Github mempermudah berbagi kode lewat internet. Gabungan keduanya digunakan untuk berbagi kode, mengembangkan fitur eksperimental dan kolaborasi.

### Commit
Git menyimpan rekaman perubahan pada suatu file dalam bentuk __commit__. Jika terjadi kesalahan, kita dapat mundur dan kembali ke commit sebelumnya. Jika ingin membuat fitur baru, kita dapat membuat cabang pada suatu commit.

Commit akan disusun pada suatu garis yang bisa dicabangkan. Jika kamu membuat branch baru, maka garis tersebut akan dicabangkan. Cabang juga dapat disatukan jika diperlukan.

### Branch
__Branch__ merupakan pointer yang menunjuk pada cabang dari suatu commit. Seperti label yang ditempelkan pada suatu commit. Suatu cabang dapat menjadi cabang anonim jika tidak memiliki pointer branch. Tetapi biasanya cabang akan memiliki setidaknya satu pointer branch.

Ketika kita membuat commit baru, pointer branch akan ikut berpindah dan menempel pada commit terbaru pada suatu cabang.

### Pointer
__Pointer__ adalah penunjuk lokasi saat ini dan nama branch. Pointer akan menunjuk dan menempel pada commit. Posisi saat ini disebut dengan __HEAD__. Ketika kita berpindah ke cabang lain, maka pointer HEAD akan dipindahkan. 

Sebenarnya nama branch juga bekerja seperti pointer. Ketika kita membuat branch baru, sebenarnya kita membuat cabang dari commit saat ini. Commit baru tersebut akan diberi pointer nama branch.

__Umumnya__ HEAD akan menunjuk kepada pointer yang juga memiliki pointer nama branch. Namun pada kondisi tertentu (misalnya mundur ke commit yang lama), HEAD akan dipindahkan ke commit yg lama. Commit lama tersebut tidak memiliki pointer nama branch. Kondisi ini disebut dengan __detached HEAD__.

### Branch Master/Main
Secara bawaan, garis commit yang pertama kali dibuat akan memiliki pointer branch dengan nama Master/Main. Github versi lama akan menggunakan nama Master, tetapi yang terbaru akan menggunakan Main. Kedua branch tersebut akan berperan sebagai branch utama. Branch yang berisi versi stabil dan tidak memiliki error.

Umumnya branch utama di remote dan di local akan dibuat sama/sinkron. Perubahan terbaru akan dikembangkan di branch lain. Setelah fitur baru selesai dikembangkan, fitur tersebut akan dikirim ke branch utama remote. Kemudian branch utama di local akan mengambil perubahan terbaru dari branch utama remote.

### Repository (Repo)
__Repository__ merupakan tempat yang menampung Commit dan file kode. Repository biasanya disingkat repo. Penyimpanan Repo di Github dilakukan lewat web dan disimpan di cloud.

Karena penyimpanan yang tersimpan di cloud, hal ini sangat mempermudah proses pengiriman Commit dan pengambilan commit dengan internet. 

### Remote
__Remote__ merupakan repo yg disimpan diluar komputer local.  Github menyediakan cloud untuk menyimpan repo dan merupakan salah satu contoh Remote. Secara bawaan, remote akan memiliki nama __origin__.

### Gambaran proses
Dimulai dengan membuat repo di github. Repo yang tersimpan didalam cloud tersebut akan disebut dengan remote. Kemudian salinan remote akan disimpan di komputer local. Pengembangan kode dilakukan di local masing-masing. Jika ingin disimpan, maka commit akan dibuat. 

Terkadang developer ingin mengembangkan fitur baru, sehingga dibuat branch. Setelah branch dibuat, developer akan memindahkan pointer menuju commit yang memiliki pointer branch yg sesuai. Kemudian bekerja disana. Setelah selesai, dibuatlah commit baru. 

Beberapa developer akan melakukan proses pengiriman commit dari local masing-masing menuju remote. Diperlukan proses penyamaan kode di remote. Setelah kode di remote sama, perubahan terbaru akan ditarik kembali ke local. Proses pengembangan akan dilanjutkan dengan kode terbaru. 

## 2. Instalasi
### Download VS Code
Developer menuliskan kodenya di aplikasi khusus yang biasanya disebut dengan code editor. IDE (Integrated Development Environment) seperti code editor namun memiliki fitur yang lebih banyak. 

Saya menyarankan pembaca untuk menggunakan Visual Studio Code (VS Code)
Link: [Download VS Code](https://code.visualstudio.com/download)

### Instalasi VS Code
Tahapan instalasi cukup sederhana, tidak ada opsi tambahan yang perlu dicentang/ditambahkan sebenarnya.
1. Terima Lisensi.
2. Pilih lokasi file vs code.
3. Kemudian opsi untuk menu di Start, bisa ditambahkan atau diganti namanya.
4. Kemudian ada opsi tambahan. Tidak ada yg perlu diubah dan opsi yang tersedia juga dapat dipilih semua (tidak ada perubahan yg berbahaya)
5. Laporan instalasi akan ditampilkan (menampilkan opsi yang dipilih) dan kamu dapat menekan tombol install.
6. Tunggu prosesnya
7. Setelah itu selesai dengan menekan tombol Finish.
8. Setelah membuka vs code, kalian dapat memilih beberapa pengaturan (misalnya tema warna, dll).

### Download dan Instalasi Git
Link: [Download Git](https://git-scm.com/downloads)

Setelah mengunduh, proses instalasi umumnya hanya mengikuti bawaaan dari Git kecuali pada satu tahapan yang bertuliskan "Choosing the default editor used by Git", saya sarankan menggunakan VS code namun kalian selalu bisa memilih yang lain.

### Membuat Akun Github


Proses instalasi tidak terlalu rumit, sehingga tidak akan dibahas disini.

Setelah selesai, pastikan git terinstall dengan menjalankan perintah berikut
```Bash
git version
```
Hasil yang diharapkan seperti dibawah (angka mungkin berbeda)
```
git version 2.44.0.windows.1
```

## Membuat akun Github
Link: [Github](https://github.com/)
Proses pembuatan akun tidak terlalu rumit, sehingga tidak akan dibahas disini.



## Praktik
### Membuat Repository di Github
### Clone Repository (git clone)
### Forking 
### Mengubah folder menjadi Repository (git init)
### git config
### git status
### git help
### git log & graph
### git branch
### git checkout
### git add
### git rm
### git commit
### git push
### merge
### konflik
### git fetch dan git pull
### Github page


## Membuat Repository(Repo)
Repo merupakan tempat menyimpan Commit. Repository dibuat menggunakan Github.

- Setelah kamu membuat akun, cari tombol berwarna hijau "Create Repository" atau "New"
- Kemudian kamu bisa mengisi nama repo, deskripsi singkat, dll.
- Repo Public dapat dilihat semua org, Repo Private tidak bisa dilihat. Kamu selalu memegang kendali commit.
- README file adalah file tulisan yang akan selalu ditampilkan (di bagian bawah) ketika kamu membuka repo. Digunakan untuk menjelaskan repo tersebut.
- .gitignore merupakan file yang berisi daftar hal-hal yang akan dikecualikan ketika kamu mengirim commit. Jika bingung, kamu bisa memilih None dan membuatnya sendiri nanti.
- License adalah lisensi, aturan mengenai pendistribusian kode dan pemakaian. Kamu selalu bisa menambahkannya nanti. Silahkan dibaca lebih lanjut, tetapi umumnya adalah:
    - MIT License: umumnya mengizinkan pengunaan selama mencantumkan pemberitahuan hak cipta dari repomu.
    - Apache License: mirip seperti MIT License, tetapi melindungi hak paten dan kontribusi.
    - Unlicense/None: jika tidak memilih, maka hukum hak cipta yang umum akan berlaku. Hukum hak cipta lebih tertutup dibandingkan 2 diatas. Orang lain hanya dapat melihat. Pemakaian dan penyebaran terbatas pada pemilik asli.
- Github umumnya digunakan untuk berbagi kode, sehingga lisensi yang lebih longgar lebih umum digunakan untuk proyek open source. Intinya disesuaikan dengan kebutuhan. Cek link ini untuk mempelajari lisensi lebih lanjut [Choose A License](https://choosealicense.com/)

## Menghubungkan Repository dengan folder local
Repository Github tersimpan di cloud. Untuk mempermudah proses kalian perlu menghubungkan folder di perangkat kalian dan repo di github.

Setelah kalian membuat repo github, github juga sudah menyediakan instruksi seperti berikut.
```Bash
echo "# nama-repo" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/nama-user/nama-repo.git
git push -u origin main
```
Informasi tambahan:
- Perintah diatas dapat dijalankan melalui terminal VS Code (Ctrl + Shift + `)
- Pastikan kalian menjalankan perintah tersebut di lokasi folder yang tepat.
![Path](/images/m0path.png)
- Jika tidak berada di folder yang tepat kalian dapat berpindah dengan perintah dibawah
```Powershell 
# mundur ke folder sebelumnya
cd .. 
# menuju folder dgn nama "nama_folder"
cd nama_folder
# melihat daftar folder yang ada
ls 
```

## Git Clone
__Clone__ merupakan proses memindahkan copy-an repo dari cloud github menuju perangkat local kalian. Data seperti riwayat commit, file, dll akan disalin juga.

Terkadang kita melanjutkan project dari repo yang sudah ada sebelumnya dan sudah dikerjakan oleh orang lain. Untuk itulah Git Clone digunakan.

Proses Clone akan membuat folder yang namanya sama dengan repo, kemudian mengunduh semua file yang ada. Ketika melakukan proses clone, pastikan kalian berada di lokasi folder yang diinginkan.

![Git Clone](/images/m0clone.png)

Salin link tersebut dan gunakan dengan git clone. Mungkin kamu juga akan diminta untuk melakukan login ke akun github lewat browser.

```Bash
git clone https://github.com/nama_user/nama_repo.git
```

## Branch
![Branch](/images/m0branch.png)
Ketika repo baru telah selesai dibuat, kita akan mendapatkan branch __Main__. Main adalah branch utama dan biasanya diisi dengan versi yang stabil.

Terkadang kita ingin mengembangkan fitur baru, tetapi tidak ingin mengganggu kode yang sudah ada. Fitur branch dapat digunakan pada situasi ini.

Kita dapat membuat branch baru, mengembangkan fitur baru di branch baru, kemudian jika fitur telah selesai dikembangkan, kita dapat menggabungkannya dengan branch Main. Sehingga Main akan memiliki fitur baru tersebut.

Saat kolaborasi antar developer, terkadang kita membuat beberapa branch. Masing-masing branch akan dipegang oleh masing-masing developer.

```Bash
# Periksa lokasi kalian (misalnya masih di Branch Main)
# PENTING selalu periksa lokasi branch saat ini
git status
# Melihat daftar branch
git branch
# membuat branch, kalian masih berada di Branch yg lama
git branch nama_branch
# pindah ke branch yang diinginkan
git checkout nama_branch
# Mulai mengerjakan
```

## Notasi di VS Code
File di VS Code akan diberikan kode huruf di kanan, kode tersebut adalah
- A = added, file baru dibuat dan belum ada sebelumnya.
- M = modified, terdapat perubahan di file.
- U = untracked, file berganti posisi.
- C = conflict, file memiliki konflik perubahan.
- D = deleted, file dihapus
- R = renamed, nama file berubah.
- Tidak ada huruf - sama dgn repo atau tidak ada perubahan.

## Git Add, Commit dan Push
Setelah kalian menambahkan file atau baris kode baru, kalian bisa mengirim perubahan tersebut ke branch yang sesuai.

Utk commit pertama, mungkin kalian perlu menuliskan email dan nama user. Jika flag --global tidak dicantumkan, maka kalian akan diminta untuk menulis email dan username setiap mengerjakan repo baru.
```Bash
# Untuk melakukan commit, kalian harus mengirimkan informasi username dan email.
git config --global user.email "nama_email@email.com"
git config --global user.name "nama_username"
```

```Bash
# Tambahkan semua file ke staging area
git add .
# Bisa juga menambahkan satu per satu
git add nama_file
# Setelah menambahkan file ke staging area, periksa kembali.
# Pastikan file sudah benar dan tidak ada konflik.

# lakukan commit dan gunakan pesan commit yang singkat, jelas dan tidak asal-asalan. Hal ini akan sangat membantumu.
git commit -m "pesan commit"
# commit dikirim
git push -u origin nama_branch
```
> Pastikan menggunakan bahasa yang jelas dan mudah dipahami pada commit.

Proses dapat dianalogikan seperti kurir paket. 
- Kamu memasukkan file tertentu dari komputer local menuju staging area. Hal ini seperti memasukkan paket ke dalam mobil van.
- Kemudian melakukan commit. Hal ini seperti memeriksa kembali barang sudah sesuai.
- Kemudian push adalah proses pengantaran.

Jika terdapat paket yang tidak sesuai (file yang memiliki konflik), maka proses pengiriman tidak akan bisa dilakukan. Kamu harus memperbaiki konflik terlebih dahulu.

## Git Fetch dari Branch
__Fetch__ digunakan untuk mengambil perubahan terbaru dari suatu repo. Hal ini umum dilakukan sebelum melakukan Push dan Merge.
```Bash
git fetch origin nama_branch
```

## Git Merge
__Merge__ merupakan proses penggabungan 2 buah branch. Setelah proses merge terjadi, kedua branch akan memiliki konten yg sama/berada di commit yg sama.

Terdapat beberapa strategi merge
- Manual Merge. Memiliki kendali penuh.
```Bash
# Pastikan berada di branch yang tepat
git status
# Pindah jika diperlukan
git checkout nama_branch
# Menggabungkan branch
git merge nama_branch_yg_ingin_digabungkan
# Mengatur konflik
# setelah selesai, lakukan push seperti biasa
git add .
git commit -m "pesan_commit"
git push -u origin "nama_branch"
```
- Fast-Forward Merge. Digunakan untuk commit yg linear. Proses yang terjadi hanyalah memindahkan pointer.
```Bash
# Memeriksa lokasi branch saat ini
git status
# Pindah jika tidak berada di branch yang lama.
git checkout nama_branch_lama
# Lakukan merge
git merge nama_branch_terbaru
# Jika diperlukan, hapus branch sementara.
git branch -d branch_yg_ingin_dihapus 
```


## Forking, Pull Request
__Forking__ merupakan proses menyalin repo dari akun org lain menuju akun milikmu. Salinan repo tersebut dapat kamu ubah sesuai kebutuhan dan "tersambung" dengan repo aslinya. Hal ini umum dilakukan jika kamu ingin menjadi kontributor pada suatu repo yang sifatnya open source.

![Forking](/images/m0fork.png)

Setelah forking, kamu dapat menambah fitur/memperbaiki fitur yang ada. Setelah itu kamu akan mengirim __pull request__. Pull request merupakan peemberitahuan kepada pemilik repo asli untuk melakukan "Pull" dari repo milikmu yang memiliki fitur baru. Pull akan dijelaskan lebih lanjut di bagian lain.

Forking merupakan fitur khusus dari Github, namun Git tetap memiliki kumpulan fitur yang dapat digunakan untuk menjalankan forking.

