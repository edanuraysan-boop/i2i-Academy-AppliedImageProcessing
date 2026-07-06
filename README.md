# 🚗 Applied Image Processing - Plaka Tanıma Sistemi

## Proje Hakkında

Bu projede klasik görüntü işleme teknikleri kullanılarak bir araç görselindeki plaka otomatik olarak tespit edilmiştir. Görüntü OpenCV kütüphanesi ile işlenmiş, gri tona dönüştürülmüş, Gaussian Blur uygulanarak gürültü azaltılmış ve Canny Edge Detection yöntemi ile kenarlar belirlenmiştir. Daha sonra contour analizi kullanılarak plaka bölgesi tespit edilmiş ve orijinal görüntüden kırpılmıştır. Son olarak EasyOCR kütüphanesi ile plaka üzerindeki karakterler okunarak terminal ekranında görüntülenmiştir.

## Kullanılan Teknolojiler

- Python
- OpenCV
- EasyOCR
- NumPy
- Matplotlib

## Projede Yapılan İşlemler

- Araç görselinin okunması
- Görüntünün gri tona dönüştürülmesi (Grayscale)
- Gaussian Blur ile gürültünün azaltılması
- Canny Edge Detection ile kenarların tespit edilmesi
- Contour analizi ile plaka bölgesinin belirlenmesi
- Plakanın orijinal görüntüden kırpılması
- EasyOCR ile plaka üzerindeki metnin okunması
- Tanınan plakanın terminal ekranında gösterilmesi
- İşlenen görüntülerin ve kırpılan plakanın `output` klasörüne kaydedilmesi


## Örnek Çıktı

```text
Recognized License Plate: 34 EA 02
```

Program çalıştırıldıktan sonra **grayscale, blur, edge detection, plaka tespiti ve kırpılan plaka görselleri** `output` klasörüne kaydedilir. Tanınan plaka bilgisi ise terminal ekranında görüntülenir.