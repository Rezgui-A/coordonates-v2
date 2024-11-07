from PyQt5 import QtWidgets, uic
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('GUI.ui', self)

        self.Adress1.clicked.connect(self.buttonDDtoDMS) 
        self.Adress2.clicked.connect(self.buttonDMStoDD)
        self.show()

    def buttonDDtoDMS(self):
        Lat = self.LatitudeLE.text()
        Long = self.LongitudeLE.text()
        self.DMSResLE.clear()
        if(not(SyntaxVerif(Lat) and SyntaxVerif(Long) )):
                self.DMSResLE.setText("Error")
        else:
 
            Lat = SyntaxFix(Lat)
            Long = SyntaxFix(Long)
            self.DMSResLE.setText(DDtoDMS(Lat,Long))
    def buttonDMStoDD(self):
        DLat = self.DMS1D.text()
        DLong = self.DMS2D.text()
        MLat = self.DMS1M.text()
        MLong = self.DMS2M.text()
        SLat = self.DMS1S.text()
        SLong = self.DMS2S.text()
        self.DMSResLE_2.clear()
        if(not(SyntaxVerif(DLat) and SyntaxVerif(DLong) and SyntaxVerif(MLat) and SyntaxVerif(MLong) and SyntaxVerif(SLat) and SyntaxVerif(SLong))):
            self.DMSResLE_2.setText("Error")
        else:
            DLat = SyntaxFix(DLat)
            DLong = SyntaxFix(DLong)
            MLat = SyntaxFix(MLat)
            MLong = SyntaxFix(MLong)
            SLat = SyntaxFix(SLat)
            SLong = SyntaxFix(SLong)
            if(self.N.isChecked()):
                if(self.W.isChecked()):
                    self.DMSResLE_2.setText(str(DMStoDD(DLat,MLat,SLat)) +"N,"+str(DMStoDD(DLong,MLong,SLong)) +"W")
                elif(self.E.isChecked()):
                    self.DMSResLE_2.setText(str(DMStoDD(DLat,MLat,SLat)) +"N,"+str(DMStoDD(DLong,MLong,SLong)) +"E")
                else:
                    self.DMSResLE_2.setText(str(DMStoDD(DLat,MLat,SLat)) +"N,"+str(DMStoDD(DLong,MLong,SLong)) +" ")
            elif(self.S.isChecked()):
                if(self.W.isChecked()):
                    self.DMSResLE_2.setText(str(str(DMStoDD(DLat,MLat,SLat)) +"S,"+str(DMStoDD(DLong,MLong,SLong)) +"W"))
                elif(self.E.isChecked()):
                    self.DMSResLE_2.setText(str(str(DMStoDD(DLat,MLat,SLat)) +"S,"+str(DMStoDD(DLong,MLong,SLong)) +"E"))
                else:
                    self.DMSResLE_2.setText(str(DMStoDD(DLat,MLat,SLat)) +","+str(DMStoDD(DLong,MLong,SLong)) +"S")
            elif(self.W.isChecked()):
                self.DMSResLE_2.setText(str(str(DMStoDD(DLat,MLat,SLat)) +","+str(DMStoDD(DLong,MLong,SLong)) +"W"))
            elif(self.E.isChecked()):
                self.DMSResLE_2.setText(str(str(DMStoDD(DLat,MLat,SLat)) +","+str(DMStoDD(DLong,MLong,SLong)) +"E"))
            else:
                self.DMSResLE_2.setText(str(str(DMStoDD(DLat,MLat,SLat)) +","+str(DMStoDD(DLong,MLong,SLong)) +" "))
                

def DDtoDMS(Lat,Long): 
    return str(int(float(Lat))) +"°" +str(abs(round(float(Lat)%1*60,2))) +"'" +str(abs(round((float(Lat)%1*60%1*60),2)))+ '",'+str(int(float(Long))) +"°" +str(abs(round(float(Long)%1*60,2))) +"'" +str(abs(round(float(Long)%1*60%1*60,2)))+ '"'

def SyntaxVerif(c):
    b = True
    for i in range(len(c)):
        if(not(c[i] in["1","2","3","4","5","6","7","8","9","0",",","."," "])):
            b = False
    return b

def SyntaxFix(c):
    if c == "":
        return "0"
    else:
        ch = ""
        for i in range(len(c)):
            if(c[i] !=" " and c[i] !=","):
                ch = ch +c[i]
            elif (c[i]==" "):
                ch = ch+ ""
            else :
                ch = ch+ "."
            
    return ch
def DMStoDD(D,M,S):
    return float(D) + float(M)/60 + float(S)/3600
app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()


