# 🚗 Applied Image Processing - Plaka Tanıma Sistemi

## Proje Hakkında

Bu projede klasik görüntü işleme teknikleri kullanılarak bir araç görselindeki plaka tespit edilmiştir. Görüntü OpenCV kütüphanesi ile işlenmiş, plaka bölgesi belirlenerek orijinal görselden kırpılmış ve EasyOCR kütüphanesi kullanılarak plaka üzerindeki karakterler okunmuştur.

Proje, görüntü işleme ve optik karakter tanıma (OCR) yöntemlerini bir arada kullanarak araç plakasını otomatik olarak algılamayı amaçlamaktadır. Tanınan plaka bilgisi terminal ekranında gösterilirken, kırpılan plaka görseli de `output` klasörüne kaydedilmektedir.

---

## Kullanılan Teknolojiler

- Python
- OpenCV
- EasyOCR
- NumPy
- Matplotlib

---

## Projede Yapılan İşlemler

- Araç görselinin okunması
- Görüntünün gri tona dönüştürülmesi
- Gaussian Blur ile gürültünün azaltılması
- Canny Edge Detection ile kenar tespiti yapılması
- Contour analizi ile plaka bölgesinin bulunması
- Plakanın orijinal görselden kırpılması
- EasyOCR ile plaka üzerindeki yazının okunması
- Tanınan plakanın terminale yazdırılması
- Kırpılan plaka görselinin `output` klasörüne kaydedilmesi
