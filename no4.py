class Buah:
    def __init__(self, inputNama, inputWarna, inputRasa):
        self.nama = inputNama
        self.warna = inputWarna
        self.rasa = inputRasa

    def info_buah(self):
        return f'Nama : {self.nama} , Warna : {self.warna} , Rasa : {self.rasa}'
    
class Mangga(Buah):
    def __init__(self,nama,warna,rasa,vitamin):
        super().__init__(nama,warna,rasa)
        Buah.__init__(self,nama,warna,rasa)
        self.vitamin = vitamin

    def info_Mangga(self):
        return f'{self.info_buah()}, vitamin : {self.vitamin}'
    
Mangga = Mangga('Mangga','Hijau','Asam','Vitamin C')
print(Mangga.info_Mangga())