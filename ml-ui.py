from PyQt5.QtWidgets import QApplication
from app.app import App

def run():
	app = QApplication([])
	window = App.get_instance()
	window.setWindowTitle('ML UI')
	window.show()

	app.exec_()


if __name__ == '__main__':
	run()
