# Docker
Docker diasumsikan sudah terinstall

> Selalu ingat kalau mau keluar dari Linux gunakan exit
> Kalau keluar dari python gunakan Ctrl+D

## Cek jika docker sudah terinstall
Cek proses instalasi dengan menjalankan Docker Desktop kemudian jalankan

```BASH
# Terminal
docker run hello-world
```

## Download image ubuntu
```BASH
# Terminal
docker run -it ubuntu bash
```

## Ada ngetest hapus file di ubuntu Lalu coba diulang dijalankan
```BASH
# Terminal
# utk menampilkan daftar file 
ls

# menghapus semua file
rm -fr / --no-preserve-root

# Keluar dari ubuntu
exit
```

Kemudian ulang nyalain
```BASH
# Terminal
docker run -it ubuntu bash
```
Dapat dilihat, bahwa ubuntunya kembali ke bentuk semula.

## Download dan jalankan Image Python
```BASH
# Terminal
docker run -it python:3.9
```

Tekan Ctrl+D untuk keluar

## Menambahkan entry point, utk menginstall library
```BASH
# Terminal
docker run -it --entrypoint=bash python:3.9
```

## Menginstall pandas
Pandas diinstall di dalam container
```BASH
# Terminal
pip install pandas 
```

## Masuk ke python
```BASH
# Terminal
python
```

## Jalankan pandas yang sudah diinstall
```python
# Terminal
import pandas
pandas.__version__
```
Coba keluar dan ulangi tahap diatas
Dapat dilihat bahwa pandas jadi tidak terinstall ketika keluar.

Gimana kalau kita perlu pandas yang permanen?

## Tambahin pandas lewat Dockerfile
Bikin file Dockerfile di lokasi yg sama
```Dockerfile
# Dockerfile
FROM python:3.9

RUN pip install pandas
```

Test dengan command biasanya
```BASH
# Terminal
docker run -it python:3.9
```

## Tambahin entry point
```Dockerfile
# Dockerfile
FROM python:3.9

RUN pip install pandas

# Tambahkan bagian ini
ENTRYPOINT [ "bash" ]
```

Build containernya
```BASH
# Terminal
docker build -t test:pandas .
```

Coba tes jalankan
```BASH
# Terminal
docker run -it test:pandas
python
```
```python
import pandas
pandas.__version__
```

## Bikin file pipeline.py
Kemudian tuliskan isi file pipeline.py
```python
import pandas as pd

# Isi kodingan disini

print("selesai")
```

## Tambahkan perintah di Dockerfile
```Dockerfile
# Dockerfile
FROM python:3.9.1

RUN pip install pandas

# Tambahkan bagian ini
WORKDIR /app
COPY pipeline.py pipeline.py

ENTRYPOINT [ "bash" ]
```

## Build perubahan terbaru
```BASH
# Terminal
docker build -t test:pandas .
```

## Jalankan container yang sudah diperbaharui
```BASH
# Terminal
docker run -it test:pandas
```
Akan terlihat kalau directorynya skrg langsung di app

## Tambahin file pipeline.py
```python
# pipeline.py
import pandas as pd

# Tambahkan bagian ini
import sys
print(sys.argv)
day = sys.argv[1]
print(f'selesai di hari = {day}')

# print("selesai")
```

## Ubah di dockerfile juga
```dockerfile
# Dockerfile
FROM python:3.9

RUN pip install pandas

WORKDIR /app
COPY pipeline.py pipeline.py

# Ubah bagian ini
ENTRYPOINT [ "python", "pipeline.py" ]
```

## Test menjalankan perubahan
```BASH
# Terminal
docker build -t test:pandas .

docker run -it test:pandas 2024-04-29
```

## Ketik ini di bash
```BASH
# Terminal
docker run -it -e POSTGRES_USER="root" -e POSTGRES_PASSWORD="root" -e POSTGRES_DB="ny_taxi" -v c:/Koding/siput/de_zoomcamp_apri/docker/ny_taxi_postgres_data:/var/lib/postgresql/data -p 5433:5433 postgres:13
```

## Install pgcli
```BASH
# Terminal
pip install pgcli
```
Cek instalasi
```BASH
# Terminal
pgcli --help
```

## Jalankan pgcli
```BASH
# Terminal
pgcli -h localhost -p 5432 -u root -d ny_taxi
```