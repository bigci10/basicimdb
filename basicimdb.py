import os 
import sys 
from PyQt5 import QtWidgets
from bs4 import BeautifulSoup
import requests

class imdb(QtWidgets.QWidget):
    
    def __init__(self):

        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.yazi_alani = QtWidgets.QTextEdit()
        self.takedata = QtWidgets.QPushButton('Data')
        self.exit = QtWidgets.QPushButton('Exit')
        self.search = QtWidgets.QPushButton('Search')

        v_box = QtWidgets.QVBoxLayout()

        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.takedata)
        v_box.addWidget(self.exit)
        v_box.addWidget(self.search)

        self.setLayout(v_box)

        self.show()

        self.setWindowTitle('IMDB')

        self.takedata.clicked.connect(self.webdata)
        self.exit.clicked.connect(self.exited)
      



    def exited(self):
         QtWidgets.qApp.quit()



    def webdata(self):


        url = "http://www.imdb.com/chart/top"
        response = requests.get(url)
        html_icerigi = response.content
        soup = BeautifulSoup(html_icerigi,"html.parser")
        
        basliklar = soup.find_all("td",{"class":"titleColumn"})
        ratingler = soup.find_all("td",{"class","ratingColumn imdbRating"})
        
  


        for i, j in zip(basliklar,ratingler):
            i = i.text
            j = j.text
            
            i = i.strip()
            i = i.replace("\n","")
            
            j = j.strip()
            
            j = j.replace("\n","")

            movies = (' {} , {}'.format(i,j))
            self.yazi_alani.setStyleSheet("color:red")
            self.yazi_alani.append(movies)
           


app = QtWidgets.QApplication(sys.argv)

ımbd = imdb()

sys.exit(app.exec_())