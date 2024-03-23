# Modul 0 Git dan Github

# Git
Git merupakan alat untuk mengatur versi dari suatu aplikasi. Bahasa inggrisnya adalah __Version Control__. Git merupakan Version Control System (VCS)

Link Dokumentasi: [Dokumentasi Git](https://git-scm.com/doc)
Git menawarkan panduan berupa buku (e-book) dan dokumentasi teknikal software seperti pada umumnya.
Link belajar lainnya:
- [Web Programming Unpas](https://www.youtube.com/playlist?list=PLFIM0718LjIVknj6sgsSceMqlq242-jNf)


## Versi/Version
Dalam mengembangkan software, terkadang kita terus mengetik dan terjadi kesalahan yang fatal. Sialnya Undo tidak dapat menyelamatkannya. Dari kejadian tersebut, kita mulai membuat copy-an file sebagai back-up. Jika suatu hari terjadi kecelakaan lagi, kita dapat menyalin ulang file back-up. 

File copy-an biasanya diberi nama khusus untuk membedakan file yg lebih tua dan yg lebih baru. Biasanya dengan angka. Misalnya Microsoft Office 2007, terdapat angka 2007. Hal inilah yang disebut dengan __versi__.

## Commit
Git merupakan alat yang mempermudah kita dalam merekam jejak perubahan pada suatu file. Jika terjadi kesalahan, kita dapat mundur ke versi stabil sebelumnya. Selain itu, hal ini sangat membantu kita jika ingin membuat fitur baru yang memiliki resiko. Setiap perubahan akan disimpan sebagai __commit__. 

Commit tidak bekerja seperti file yang di-save, tetapi commit hanya merekam perubahan. Sehingga jika kita bekerja dengan file berukuran besar, setiap commit tidak akan memakan penyimpanan yang banyak.

## Kolaborasi
Terkadang kita bekerja dalam tim. Git hadir dan memungkinkan kita berbagi Commit dan memiliki sistem integrasi yang baik.

Dengan sistem dari Git, kita dapat dengan mudah melihat siapa yang mengubah file dan kapan dilakukan. Terdapat juga pesan/komentar yang dapat ditambahkan. Isi pesan yang baik akan membantu proses pengembangan.

# Github
Github adalah platform untuk berbagi Repository dan kolaborasi developer. Github juga memiliki berbagai fitur lainnya seperti membuat halaman statis (bisa digunakan untuk membuat halaman portfolio).

## Repository (Repo)
Repository merupakan tempat yang menampung Commit dan file kode. Repository kadang disingkat repo. Penyimpanan Repo di Github dilakukan lewat web dan disimpan di cloud.

Karena penyimpanan yang tersimpan di cloud, hal ini sangat mempermudah proses pengiriman Commit dan pengambilan commit dengan internet. 

## Gabungan Git + Github
Kamu dapat menggunakan Git dan Github secara terpisah. Tetapi dengan menggabungkan keduanya, prosesnya akan jauh lebih mudah. Git memungkinkan kita menggunakan perintah Git di terminal dan Github mempermudah berbagi kode lewat internet.

# Praktik
## Instalasi
Jika belum memiliki code editor atau IDE (Integrated Development Environment) atau aplikasi untuk menulis kode, saya menyarankan untuk menggunakan Visual Studio Code (VS Code)

Link Download:
- [Download VS Code](https://code.visualstudio.com/download)
- [Download Git](https://git-scm.com/downloads)

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

Proses dapat dianalogikan seperti kang paket. 
- Kamu memasukkan file tertentu dari komputer local menuju staging area. Hal ini seperti memasukkan paket ke dalam mobil van.
- Kemudian melakukan commit. Hal ini seperti memeriksa kembali barang sudah sesuai.
- Kemudian push adalah proses pengantaran.

Jika terdapat paket yang tidak sesuai (file yang memiliki konflik), maka proses pengiriman tidak akan bisa dilakukan. Kamu harus memperbaiki konflik terlebih dahulu.

## Git Pull & Merging Branch
Pull adalah proses memindahkan commit/perubahan dari branch lain menuju branch yang saat ini kamu tempati.



## Forking, Pull Request
__Forking__ merupakan proses menyalin repo dari akun org lain menuju akun milikmu. Salinan repo tersebut dapat kamu ubah sesuai kebutuhan dan "tersambung" dengan repo aslinya. Hal ini umum dilakukan jika kamu ingin menjadi kontributor pada suatu repo yang sifatnya open source.

![Forking](/images/m0fork.png)

Setelah forking, kamu dapat menambah fitur/memperbaiki fitur yang ada. Setelah itu kamu akan mengirim __pull request__. Pull request merupakan peemberitahuan kepada pemilik repo asli untuk melakukan "Pull" dari repo milikmu yang memiliki fitur baru. Pull akan dijelaskan lebih lanjut di bagian lain.

Forking merupakan fitur khusus dari Github, namun Git tetap memiliki kumpulan fitur yang dapat digunakan untuk menjalankan forking.

