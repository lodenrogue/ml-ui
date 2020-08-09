import PyQt5.QtWidgets as qtw

class FileService:

	def get_file(self, callback):
		fname = qtw.QFileDialog.getOpenFileName(None, '*')
		callback(fname[0])