from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import random

App = QApplication([])
Window = QWidget()
Window.setFixedSize(400, 400)

Soal = QLabel('Kapan indonesia merdeka?')
Jawab1 = QRadioButton('17 Agustus 1945')
Jawab2 = QRadioButton('10 Agustus 1947')
Jawab3 = QRadioButton('14 Agustus 1940')
Jawab4 = QRadioButton('17 Agustus 1948')

Box = QGroupBox('PILIH')
tombol = QPushButton('Jawab')

Hasil = QGroupBox('HASILNYA')
BENAR_DAN_SALAH = QLabel('Benar/Salah')
JAWABAN_BENAR = QLabel('INI JAWABAN BENARNYA!!')

garis_utama_hasil = QVBoxLayout()
garis_utama_hasil.addWidget(BENAR_DAN_SALAH)
garis_utama_hasil.addWidget(JAWABAN_BENAR, alignment = Qt.AlignHCenter)

Hasil.setLayout(garis_utama_hasil)

garis_utama = QVBoxLayout()
garis_J1 = QHBoxLayout()
garis_J2 = QHBoxLayout()

garis_J1.addWidget(Jawab1)
garis_J1.addWidget(Jawab2)

garis_J2.addWidget(Jawab3)
garis_J2.addWidget(Jawab4)

garis_utama.addLayout(garis_J1)
garis_utama.addLayout(garis_J2)
Box.setLayout(garis_utama)

garis_utama_jendela = QVBoxLayout()
garis_utama_jendela.addWidget(Soal, alignment = Qt.AlignHCenter)
garis_utama_jendela.addWidget(Box)
garis_utama_jendela.addWidget(Hasil)
garis_utama_jendela.addWidget(tombol)
Window.setLayout(garis_utama_jendela)

kelompok_radio = QButtonGroup()
kelompok_radio.addButton(Jawab1)
kelompok_radio.addButton(Jawab2)
kelompok_radio.addButton(Jawab3)
kelompok_radio.addButton(Jawab4)


def show_results():
    Box.hide()
    Hasil.show()
    tombol.setText('Soal selanjutnya')

class Question:
    def __init__(self, question, benar, salah1, salah2, salah3):
        self.question = question
        self.benar = benar
        self.salah1 = salah1
        self.salah2 = salah2
        self.salah3 = salah3

LIST_PERTANYAAN = list()
LIST_PERTANYAAN.append  (Question('KAPAN KAMU MENIKAH?', 'TAKDIR TUHAN', 'GATAU', 'KAPAN-KAPAN', 'GA NIKAH'))
LIST_PERTANYAAN.append  (Question('KAPAN TERAKHIR KAMU MANDI', '1 TAHUN LALU', '10 TAHUN LALU', 'GATAU', '100000 TAHUN LALU'))
LIST_PERTANYAAN.append  (Question('TANGGAL INDONESIA MERDEKA', '17 AGUSTUS', '10 AGUSTUS', 'GATAU', 'TRALALELO TRALALA'))
LIST_PERTANYAAN.append  (Question('APA ANOMALI TERKUAT', 'TUNG2 SAHUR', 'CAPUCINO ASASINO', 'GATAU', 'TRALALELO TRALALA'))
LIST_PERTANYAAN.append  (Question('5+5 =', '10', 'sepuluh', 'ten', 'Pratama'))
   
  



Window.total_soal = 0
Window.total_benar = 0

    
def show_question():
    Box.show()
    Hasil.hide()
    tombol.setText('Jawab')
    kelompok_radio.setExclusive(False)
    Jawab1.setChecked(False)
    Jawab2.setChecked(False)
    Jawab3.setChecked(False)
    Jawab4.setChecked(False)
    kelompok_radio.setExclusive(True)
def tekan():
    if tombol.text() == 'Jawab':
        #show_results()
        check_answer()
    else:
        next_question()


LIST_RADIO = [Jawab1,Jawab2,Jawab3,Jawab4]
def ask(pertanyaan):
    random.shuffle(LIST_RADIO)
    LIST_RADIO[0].setText(pertanyaan.benar)
    LIST_RADIO[1].setText(pertanyaan.salah1)
    LIST_RADIO[2].setText(pertanyaan.salah2)
    LIST_RADIO[3].setText(pertanyaan.salah3)
    Soal.setText(pertanyaan.question)
    JAWABAN_BENAR.setText(pertanyaan.benar)
    show_question()

def check_answer():
    if LIST_RADIO[0].isChecked():
        BENAR_DAN_SALAH.setText('Benarrr')
        Window.total_benar += 1
    else:
        BENAR_DAN_SALAH.setText('Salahh')
        

    show_results()
    print('===================')
    print('TOTAL BETUL =', Window.total_benar)
    print('PRESENTASE =', (Window.total_benar / Window.total_soal) * 100, '%')



#Window.INDEX_SAAT_INI = -1
#def next_question():
    #Window.INDEX_SAAT_INI += 1
   # if Window.INDEX_SAAT_INI >= len(LIST_PERTANYAAN):
        #Window.INDEX_SAAT_INI = 0
    #ask(LIST_PERTANYAAN[Window.INDEX_SAAT_INI])
    
def next_question():
    Window.total_soal += 1
    print('-----------------')
    print('Total soal =', Window.total_soal)
    print('-----------------')
    INDEX_SAAT_INI = random.randint(0, len(LIST_PERTANYAAN)-1)
    ask(LIST_PERTANYAAN[INDEX_SAAT_INI])



tombol.clicked.connect(tekan)
next_question()


Window.show()
App.exec_()