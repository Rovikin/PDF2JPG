import os
from pdf2image import convert_from_path

# Path default untuk folder input dan output
DEFAULT_FOLDER = '/sdcard'

def convert_pdf_to_jpg(pdf_name):
    pdf_path = os.path.join(DEFAULT_FOLDER, pdf_name)
    
    # Cek apakah file PDF ada
    if not os.path.isfile(pdf_path):
        print(f'File tidak ditemukan: {pdf_path}')
        return
    
    # Mengambil nama file tanpa ekstensi
    base_name = os.path.splitext(pdf_name)[0]

    # Mengatur resolusi (dpi) untuk gambar yang dihasilkan
    images = convert_from_path(pdf_path, dpi=300)  # Menggunakan 300 dpi untuk resolusi tinggi
    
    for i, image in enumerate(images):
        image_path = os.path.join(DEFAULT_FOLDER, f'{base_name}_page_{i + 1}.jpg')
        image.save(image_path, 'JPEG')
        print(f'Page {i + 1} saved as {image_path}')

def main():
    print('Masukkan nama file PDF yang akan diproses:')
    pdf_name = input('Nama file PDF (misalnya rak_buku_mama_rara.pdf): ').strip()
    
    convert_pdf_to_jpg(pdf_name)
    print('Konversi selesai!')

if __name__ == '__main__':
    main()