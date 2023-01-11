class Waktu:
    def _init_(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def tampil():
        hour = int(input("Jam : "))
        minute = int(input("Menit : "))
        second = int(input("Detik : "))

        if hour <= 24 and minute <= 59 and second <= 59:
            print(hour, ":", minute, ":", second)
        else:
            print("Salah")
    
    tampil()
