from PyQt5.QtWidgets import QMainWindow, QStackedWidget
from main.main_view import MainView

class App(QMainWindow):

	__instance = None

	@staticmethod
	def get_instance():
		if App.__instance == None:
			App.__instance = App()
		return App.__instance

	
	def __init__(self):
		super().__init__()
		self.init_ui()


	def init_ui(self):
		self.main_view = MainView()
		self.stacked = QStackedWidget()
		self.setCentralWidget(self.stacked)
		
		self.stacked.addWidget(self.main_view)
		self.stacked.setCurrentWidget(self.main_view)