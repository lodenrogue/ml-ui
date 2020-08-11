import PyQt5.QtWidgets as qtw
from model.train_request import TrainRequest

class DataService:

	def get_file(self, callback):
		fname = qtw.QFileDialog.getOpenFileName(None, '*')
		callback(fname[0])
	

	def file_path_changed(self, text):
		TrainRequest.get_instance().csv_path = text


	def get_columns(self, fname):
		with open(fname, 'r') as f:
			header = f.readline()
			
			if header is None:
				return []
			else:
				return header.replace('\n', '').split(',')


	def column_selection_changed(self, selection):
		TrainRequest.get_instance().pred_column = selection
