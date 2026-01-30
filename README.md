**🍋 MangoScan**
 “Aplikasi AI untuk mendeteksi tingkat kematangan buah mangga menggunakan TensorFlow dan Gradio.”

### 2. Fitur Utama
- Training model CNN dengan dataset mangga.
- Prediksi tingkat kematangan (Mentah, Setengah Matang, Matang, Terlalu Matang, Busuk).
- Web demo dengan Gradio.

### 3. Struktur Project
```
MangoScan/
 ├── MangoScan.ipynb        # Notebook training
 ├── mangoscan.py           # Script inference + Gradio
 ├── MangoScanModel.h5      # Model hasil training (opsional, bisa link)
 ├── requirements.txt       # Dependensi
 └── README.md              # Dokumentasi
```
link drive h.5: https://drive.google.com/drive/folders/1BecC4iy2BTrLbs9waGsYr-cEXOAJl_Gw?usp=drive_link
### 4. Cara Install & Jalankan
```bash
# clone repo
git clone https://github.com/username/MangoScan.git
cd MangoScan

# install dependensi
pip install -r requirements.txt

# jalankan aplikasi
python mangoscan.py
```
Lalu buka di browser: `http://localhost:7860`

### 5. Cara Training Ulang (opsional)
- Jelaskan bahwa training ada di `MangoScan.ipynb` (Colab).
- Tambahkan link dataset kalau bisa.

### 6. Model (.h5)
- Kalau file `.h5` terlalu besar untuk GitHub, tulis di README:
  > “Model MangoScan disimpan di Google Drive: [link download]”  
  atau pakai Git LFS.

### 7. Contoh Pemakaian
- Screenshot Gradio interface.  
- Contoh output prediksi:  
  ```
  Prediksi: Matang (confidence: 0.92)
  ```

### 8. Lisensi (opsional)
- Misalnya MIT License, supaya orang lain bebas pakai.

---

## ✨ Contoh Draft README.md

```markdown
# 🍋 MangoScan

MangoScan adalah aplikasi AI untuk mendeteksi tingkat kematangan buah mangga secara otomatis menggunakan TensorFlow dan Gradio.

## Fitur
- Training CNN dengan dataset mangga
- Prediksi 5 kelas: Mentah, Setengah Matang, Matang, Terlalu Matang, Busuk
- Web demo interaktif dengan Gradio

## Struktur Project
- `MangoScan.ipynb` : Notebook training di Google Colab
- `mangoscan.py` : Script inference + Gradio interface
- `MangoScanModel.h5` : Model hasil training (download [di sini](link))
- `requirements.txt` : Dependensi Python

## Cara Jalankan
```bash
git clone https://github.com/username/MangoScan.git
cd MangoScan
pip install -r requirements.txt
python mangoscan.py
```

Buka di browser: `http://localhost:7860`

## Cara Training Ulang
Gunakan `MangoScan.ipynb` di Google Colab dengan dataset mangga.

## Lisensi
MIT License
```

---



https://drive.google.com/drive/folders/1BecC4iy2BTrLbs9waGsYr-cEXOAJl_Gw?usp=drive_link
