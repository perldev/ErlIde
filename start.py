import sys
from PyQt4 import QtCore, QtGui
from mod.main import Ui_MainWindow 
from mod.my import MyForm



if __name__ == "__main__":
	    app = QtGui.QApplication(sys.argv)
    	    myapp = MyForm()
            myapp.show()
    	    sys.exit(app.exec_())
