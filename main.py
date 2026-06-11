import time

class Pomodoro:
    def __init__(self, toplam_saniye):
        self.toplam_saniye = toplam_saniye

    def start_pomodoro(self):
        while self.toplam_saniye > 0:
            dk = self.toplam_saniye // 60
            sn = self.toplam_saniye % 60
            
            # end="\r" ile aynı satırda güncelliyoruz
            print(f"Kalan süre: {dk:02d}:{sn:02d}", end="\r")
            
            time.sleep(1)
            self.toplam_saniye -= 1
        
        print("\nSüre doldu! Mola vakti! 🎉")

    @staticmethod
    def cikis(sure=5):
        print("Çıkılıyor", end="")
        for i in range(sure):
            time.sleep(0.5)
            print(".", end="", flush=True)
        print("\nGörüşürüz ! ")

# Ana program döngüsü
while True:
    print("\n------- PYTHON POMODORO --------")
    print("Çıkmak için 'q' tuşuna basın.")
    soru = input("Toplam saniye giriniz: ")

    if soru.lower() == 'q':
        Pomodoro.cikis()
        break
    
    try:
        saniye = int(soru)
        timer = Pomodoro(saniye)
        timer.start_pomodoro()
    except ValueError:
        print("Lütfen geçerli bir sayı giriniz veya çıkış için 'q' tuşuna basın.")
