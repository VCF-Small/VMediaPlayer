from PyQt5.QtWidgets import QFileDialog
from os.path import splitext


DarkStyleSheet = '''QSlider::groove { background-color: black;border: 0px solid #424242; height: 10px; border-radius: 4px;}QSlider::handle { background-color: red; border: 2px solid red; width: 16px; height: 20px; line-height: 20px; margin-top: -5px; margin-bottom: -5px; border-radius: 10px; }QSlider::handle:hover { border-radius: 10px;background-color:rgb(150, 50, 50)}QSlider::sub-page{background-color: red;border: 0px solid #424242; height: 10px; border-radius: 4px;}*{font: 8pt "MS Shell Dlg 2";}#Tool_Box QLabel{font: 10pt "MS Shell Dlg 2";}QGroupBox{color:white;}QPushButton{background-color:red;border:none;border-radius: 5px;}QPushButton:hover{background-color:rgb(200, 50, 50);border:none;}QPushButton:pressed{background-color:rgb(100, 50, 50);border:none;}#VMediaPlayer{background-color:rgb(30,30,30);}QLabel{background-color:red;border:none;border-radius: 5px;}QLabel#Video_Widget{background-color:rgb(30,30,30);border:none;border-radius: 5px;}QMenuBar{background:rgb(40,40,40);color:white;}QMenu{background:rgb(40,40,40);color:white;}'''
LightStyleSheet = '''QSlider::groove { background-color: black;border: 0px solid #424242; height: 10px; border-radius: 4px;}QSlider::handle { background-color: red; border: 2px solid red; width: 16px; height: 20px; line-height: 20px; margin-top: -5px; margin-bottom: -5px; border-radius: 10px; }QSlider::handle:hover { border-radius: 10px;background-color:rgb(150, 50, 50)}QSlider::sub-page{background-color: red;border: 0px solid #424242; height: 10px; border-radius: 4px;}QSlider::add-page{background-color: rgb(230,230,230);border: 0px solid #424242; height: 10px; border-radius: 4px;}*{font: 8pt "MS Shell Dlg 2";}QPushButton{background-color:red;border:none;border-radius: 5px;}QPushButton:hover{background-color:rgb(200, 50, 50);border:none;}QPushButton:pressed{background-color:rgb(100, 50, 50);border:none;}#VMediaPlayer{background-color:rgb(255,255,255);}QLabel{background-color:red;border:none;border-radius: 5px;}QLabel#Video_Widget{background-color:rgb(255,255,255);border:none;border-radius: 5px;}'''


def DarkMode(window):
    window.setStyleSheet(DarkStyleSheet)


def LightMode(window):
    window.setStyleSheet(LightStyleSheet)


def Open():
    src_path, _ = QFileDialog.getOpenFileName(
        filter="Media (*.mp4  *.mkv *.flv *.ts *.mts *.avi *.mp3 *.wav )")
    if(src_path != "" or src_path != None):
        return(src_path)
