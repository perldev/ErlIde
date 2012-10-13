from main import Ui_MainWindow
from PyQt4 import QtCore,QtGui
from tabs import open_tab
 
# Import the compiled UI module
#  from windowUi import Ui_MainWindow

# Create a class for our main window
class MyForm(QtGui.QMainWindow):
     def showOpenFileDialog(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file','/home')
        open_tab(self.ui.tabWidget, str(fname))
            
       
      
     def fill_events(self):
            self.ui.actionOpen.triggered.connect(self.showOpenFileDialog)
            

  
     def __init__(self):
         QtGui.QMainWindow.__init__(self)
          # This is always the same
         self.ui=Ui_MainWindow()
         self.ui.setupUi(self)
         self.fill_events()