import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def rastgele_koordinat_uret_ve_kaydet(nokta_sayisi, dosya_adi):
    # Belirtilen sayıda rastgele X ve Y koordinatları üret
    x_koordinatlari = np.random.randint(0, 1001, nokta_sayisi)
    y_koordinatlari = np.random.randint(0, 1001, nokta_sayisi)
    
    # Koordinatları bir DataFrame içine koy
    df = pd.DataFrame({'X': x_koordinatlari, 'Y': y_koordinatlari})
    
    # DataFrame'i belirtilen dosya adına Excel dosyası olarak kaydet
    df.to_excel(dosya_adi, index=False)

def koordinatlari_oku(dosya_adi):
    # Belirtilen Excel dosyasından koordinatları oku
    df = pd.read_excel(dosya_adi)
    
    # X ve Y koordinatlarını ayrı olarak geri döndür
    return df['X'], df['Y']

def koordinatlari_ciz(x_koordinatlari, y_koordinatlari, ızgara_boyutu):
    # Şekil boyutunu ayarla
    plt.figure(figsize=(10, 10))
    
    # Her eksen için ızgara sayısını hesapla
    eksen_basina_ızgara = 1000 // ızgara_boyutu
    
    # Renk haritasını oluştur ve 25 renge ayır
    renk_haritasi = plt.get_cmap('tab20')
    renkler = renk_haritasi(np.linspace(0, 1, 25))

    # Her ızgara hücresi için
    for i in range(eksen_basina_ızgara):
        for j in range(eksen_basina_ızgara):
            # Belirli ızgara hücresinde yer alan noktaları seç
            maske = (x_koordinatlari >= i * ızgara_boyutu) & (x_koordinatlari < (i + 1) * ızgara_boyutu) & \
                    (y_koordinatlari >= j * ızgara_boyutu) & (y_koordinatlari < (j + 1) * ızgara_boyutu)
            
            # Her hücreye bir renk ata
            renk_indeksi = i * eksen_basina_ızgara + j  
            plt.scatter(x_koordinatlari[maske], y_koordinatlari[maske], color=renkler[renk_indeksi], s=10, alpha=0.6)

    # Grafik sınırlarını ayarla
    plt.xlim(0, 1000)
    plt.ylim(0, 1000)
    
    # Eksen etiketlerini ve başlık ekle
    plt.xlabel('X Koordinatları')
    plt.ylabel('Y Koordinatları')
    plt.title(f'Rastgele Nokta Haritası')
    
    # Izgara çizgilerini göster
    plt.grid(True)
    
    # Grafiği göster
    plt.show()

# Rastgele nokta sayısını, dosya adını ve ızgara boyutunu belirle
nokta_sayisi = 1000
dosya_adi = 'koordinatlar.xlsx'
ızgara_boyutu = 200

# Rastgele koordinatları üret ve kaydet
rastgele_koordinat_uret_ve_kaydet(nokta_sayisi, dosya_adi)

# Kaydedilen dosyadan koordinatları oku
x_koordinatlari, y_koordinatlari = koordinatlari_oku(dosya_adi)

# Koordinatları çiz
koordinatlari_ciz(x_koordinatlari, y_koordinatlari, ızgara_boyutu)