import PyQt5.QtWidgets as qtw
from model.train_request import TrainRequest

class CsvService:

	def get_file(self, callback):
		fname = qtw.QFileDialog.getOpenFileName(None, '*')
		callback(fname[0])
	

	def text_changed(self, text):
		TrainRequest.get_instance().csv_path = text