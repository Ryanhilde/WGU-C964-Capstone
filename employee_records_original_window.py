from PyQt5 import QtCore, QtGui, QtWidgets
import csv

from PyQt5.QtWidgets import QMessageBox

from employee_records_window import Ui_MainWindow
from company_records_window import Ui_MainWindow_Company
from employee_scatter_plot import Ui_Employee_Scatter_Plot
from company_scatter_plot import Ui_MainWindow_Company_Scatter_Plot

class Ui_MainWindow_employee_record(QtWidgets.QWidget):

    def __init__(self, fileName, parent=None):
        super(Ui_MainWindow_employee_record, self).__init__(parent)
        self.fileNameEmployee = "Read_Employee_Data.csv"
        self.fileNameAlteredEmployee = "Write_Employee_Data.csv"
        self.fileNameCompany = "Read_Company_Data.csv"
        self.fileNameAlteredCompany = "Write_Company_Data.csv"
        self.model = QtGui.QStandardItemModel(self)

        self.tableView = QtWidgets.QTableView(self)
        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.setFixedSize(800, 600)

        self.load_employee_data_button = QtWidgets.QPushButton(self)
        self.load_employee_data_button.setText("Click here to view the original employee data")
        try:
            self.load_employee_data_button.clicked.connect(self.on_pushButtonLoad_clicked_employee)
        except EnvironmentError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error! Please close existing window.")
            msg.setInformativeText('You can only have one window open at a time. Please close the existing window to continue!')
            msg.setWindowTitle("Error")
            msg.exec_()
            pass
        self.load_altered_employee_data_button = QtWidgets.QPushButton(self)
        self.load_altered_employee_data_button.setText("Click here to view the altered employee data")
        self.load_altered_employee_data_button.setGeometry(QtCore.QRect(11, 645, 800, 25))
        self.load_altered_employee_data_button.clicked.connect(self.on_pushButtonLoad_clicked_altered_employee)

        self.load_company_data_button = QtWidgets.QPushButton(self)
        self.load_company_data_button.setText("Click here to view the original company data")
        self.load_company_data_button.setGeometry(QtCore.QRect(11, 675, 800, 25))
        self.load_company_data_button.clicked.connect(self.on_pushButtonLoad_clicked_company)

        self.load_altered_company_data_button = QtWidgets.QPushButton(self)
        self.load_altered_company_data_button.setText("Click here to view the altered company data")
        self.load_altered_company_data_button.setGeometry(QtCore.QRect(11, 705, 800, 25))
        self.load_altered_company_data_button.clicked.connect(self.on_pushButtonLoad_clicked_altered_company)

        self.layoutVertical = QtWidgets.QVBoxLayout(self)
        self.layoutVertical.addWidget(self.tableView)
        self.layoutVertical.addWidget(self.load_employee_data_button)
        self.layoutVertical.addSpacing(220)
        self.welcomeLabel = QtWidgets.QLabel(self)
        self.welcomeLabel.setGeometry(QtCore.QRect(230, 735, 500, 25))
        self.navigationLabel = QtWidgets.QLabel(self)
        self.navigationLabel.setGeometry(QtCore.QRect(155, 760, 700, 25))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(16)
        self.welcomeLabel.setFont(font)
        self.welcomeLabel.setText("Welcome to the Differential Privacy Engine!")
        self.navigationLabel.setFont(font)
        self.navigationLabel.setText("To begin, please select a dataset you would like to work with.")

        self.employee_record_button = QtWidgets.QPushButton(self)
        self.employee_record_button.setText("Apply DP to Employee Records")
        self.employee_record_button.setGeometry(QtCore.QRect(11, 800, 450, 25))
        self.employee_record_button.clicked.connect(self.employee_one_openWindow)

        self.employee_scatter_plot_button = QtWidgets.QPushButton(self)
        self.employee_scatter_plot_button.setText("View a scatter plot comparision for Employee Records")
        self.employee_scatter_plot_button.setGeometry(QtCore.QRect(11, 830, 450, 25))
        self.employee_scatter_plot_button.clicked.connect(self.employee_one_scatter_plot_openWindow)

        self.company_record_button = QtWidgets.QPushButton(self)
        self.company_record_button.setText("Apply DP to Company Records")
        self.company_record_button.setGeometry(QtCore.QRect(420, 800, 380, 25))
        self.company_record_button.clicked.connect(self.company_one_openWindow)

        self.company_scatter_plot_button = QtWidgets.QPushButton(self)
        self.company_scatter_plot_button.setText("View a scatter plot comparision for Company Records")
        self.company_scatter_plot_button.setGeometry(QtCore.QRect(420, 830, 380, 25))
        self.company_scatter_plot_button.clicked.connect(self.company_one_scatter_plot_openWindow)



    def loadCsv(self, fileName):
        self.model.clear()
        with open(fileName, "r") as fileInput:
            for row in csv.reader(fileInput):
                items = [
                    QtGui.QStandardItem(field)
                    for field in row
                ]
                self.model.appendRow(items)

    @QtCore.pyqtSlot()
    def on_pushButtonLoad_clicked_employee(self):
        self.loadCsv(self.fileNameEmployee)

    @QtCore.pyqtSlot()
    def on_pushButtonLoad_clicked_altered_employee(self):
        self.loadCsv(self.fileNameAlteredEmployee)

    @QtCore.pyqtSlot()
    def on_pushButtonLoad_clicked_company(self):
        self.loadCsv(self.fileNameCompany)

    @QtCore.pyqtSlot()
    def on_pushButtonLoad_clicked_altered_company(self):
        self.loadCsv(self.fileNameAlteredCompany)

    def employee_one_openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def altered_employee_one_openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def employee_one_scatter_plot_openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Employee_Scatter_Plot()
        self.ui.setupUi(self.window)
        self.window.show()

    def company_one_openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow_Company()
        self.ui.setupUi(self.window)
        self.window.show()

    def altered_company_one_openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow_Company()
        self.ui.setupUi(self.window)
        self.window.show()


    def company_one_scatter_plot_openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui =  Ui_MainWindow_Company_Scatter_Plot()
        self.ui.setupUi(self.window)
        self.window.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName('Differential Privacy Engine')

    main = Ui_MainWindow_employee_record("data.csv")
    main.show()

    altered_employee_data = "Write_Employee_Data.csv"
    f = open(altered_employee_data, "w+")
    f.close()

    altered_company_data = "Write_Company_Data.csv"
    f = open(altered_company_data, "w+")
    f.close()

    sys.exit(app.exec_())
