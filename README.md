# Latin'den Göktürkçe'ye Çevirici / Latin to Göktürk Converter

[Türkçe](#türkçe) | [English](#english)

---

<a name="türkçe"></a>
## 🇹🇷 Türkçe

Latin alfabesiyle yazılmış Türkçe metinleri Göktürk (Orhun) alfabesine çeviren bir Python kütüphanesi.

> [!WARNING]
> Bu proje hobi ve eğitim amaçlı hazırlanmıştır. Akademik veya profesyonel çalışmalar için %100 doğruluk garanti edilmez ve yeterince test edilmemiştir.

### Özellikler

- **Ünlü Uyumu**: Kalın ve ince ünlüleri ve bunlara bağlı ünsüz değişimlerini (örneğin kalın 'k' 𐰴, ince 'k' 𐰚) otomatik algılar.
- **Özel Karakterler**: 'ng' (ñ), 'nd', 'lt' gibi bitişik sesleri ve ligatürleri destekler.
- **Tarihsel Doğruluk**: "Türk" (𐱅𐰇𐰼𐰜) gibi kelimeler için tarihsel yazım kurallarını uygular.
- **Yabancı Kelimeler**: Yabancı kökenli veya uyumsuz kelimelerde (örn. "Kitap") yerel uyum kurallarını uygular.

### Kurulum

**GitHub üzerinden:**
```bash
pip install git+https://github.com/eokayakca/latin_to_gokturk.git
```

**Yerel olarak:**
```bash
git clone https://github.com/eokayakca/latin_to_gokturk.git
cd latin_to_gokturk
pip install .
```

### Kullanım

```python
from gokturk import LatinToGokturkConverter

converter = LatinToGokturkConverter()
text = "Türk milleti çalışkandır."
gokturk_text = converter.convert(text)
print(gokturk_text) 
# Çıktı: 𐱅𐰇𐰼𐰜 𐰢𐰃𐰠𐰠𐰜𐱅𐰃 𐰲𐰀𐰡𐰃𐱁𐰴𐰀𐰦𐰃𐰺
```

### Lisans

MIT

---

<a name="english"></a>
## 🇬🇧 English

A Python library to convert Turkish text from Latin alphabet to Göktürk (Orkhon) script.

> [!WARNING]
> This project is created for hobby and educational purposes. It is not guaranteed to be 100% accurate for academic or professional use and has not been extensively tested.

### Features

- **Vowel Harmony**: It finds back/front vowels and chooses the right consonants (for example, back 'k' 𐰴 or front 'k' 𐰚).
- **Special Characters**: It supports special letter groups like 'ng' (ñ), 'nd', 'lt'.
- **Historical Accuracy**: It uses historical spelling for words like "Türk" (𐱅𐰇𐰼𐰜).
- **Loanwords**: It works with words that have mixed vowels (like "Kitap").

### Installation

**From GitHub:**
```bash
pip install git+https://github.com/eokayakca/latin_to_gokturk.git
```

**Locally:**
```bash
git clone https://github.com/eokayakca/latin_to_gokturk.git
cd latin_to_gokturk
pip install .
```

### Usage

```python
from gokturk import LatinToGokturkConverter

converter = LatinToGokturkConverter()
text = "Türk milleti çalışkandır."
gokturk_text = converter.convert(text)
print(gokturk_text) 
# Output: 𐱅𐰇𐰼𐰜 𐰢𐰃𐰠𐰠𐰜𐱅𐰃 𐰲𐰀𐰡𐰃𐱁𐰴𐰀𐰦𐰃𐰺
```

### License

MIT
