import PyQt5.QtWidgets as qtw
from main.csv.csv_view import CsvView
from main.prediction.prediction_view import PredictionView
from main.train.train_view import TrainView
from main.run.run_view import RunView


class MainView(qtw.QMainWindow):

	def __init__(self, parent=None):
		super(MainView, self).__init__(parent)

		self.csv_view = CsvView()
		self.prediction_view = PredictionView()
		self.train_view = TrainView()
		self.run_view = RunView()

		self.setCentralWidget(self.create_view())
		self.show()


	def create_view(self):
		layout = qtw.QVBoxLayout()
		layout.addLayout(self.csv_view.create_view())
		layout.addLayout(self.prediction_view.create_view())
		layout.addLayout(self.train_view.create_view())
		layout.addLayout(self.run_view.create_view())
		
		layout.setContentsMargins(25, 25, 25, 25)
		layout.setSpacing(15)

		view = qtw.QWidget()
		view.setLayout(layout)
		return view
