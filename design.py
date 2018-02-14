from PyQt4 import QtCore, QtGui
import SubscribeMailingList as SML
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.setGeometry(50, 50, 600, 300)
        self.setWindowTitle("Getting Started!")
        self.subscribeMailingList()
        self.show()
    
    def subscribeMailingList(self):
        label = QtGui.QLabel('Select Mailing Lists That You want to Subscribe!',self)
        label.resize(400, 20)
        label.move(50, 5)
        self.email = QtGui.QLineEdit('Enter Email ID', self)
        self.email.move(100, 30)
        self.email.resize(280,20)
        self.checkbox1 = QtGui.QCheckBox('debian-outreach',self)
        self.checkbox1.move(100,60)
        self.checkbox1.resize(200,20)
        self.checkbox2 = QtGui.QCheckBox('debian-user-digest',self)
        self.checkbox2.move(100,85)
        self.checkbox2.resize(200,20)
        self.subButton = QtGui.QPushButton('Subscribe', self)
        self.subButton.move(100,120)
        QtCore.QObject.connect(self.subButton, QtCore.SIGNAL('clicked()'), self.onClicked)
    
    def onClicked(self):
        subObj = SML.MailingList(str(self.email.text()))
        if(self.checkbox1.isChecked()):
            subObj.Subscribe('debian-outreach')
        if(self.checkbox2.isChecked()):
            subObj.Subscribe('debian-user-digest')
        
        message = QtGui.QMessageBox()
        message.setWindowTitle('Subscribed!')
        message.setText("Check Your Email to Confirms Subscriptions!")
        message.setIcon(QtGui.QMessageBox.Information)
        message.setStandardButtons(QtGui.QMessageBox.Ok)
        message.exec_()
        

        