from model.train_request import TrainRequest

class TrainService:

	def train_split_changed(self, text):
		value = None if text == '' else int(text)
		TrainRequest.get_instance().train_split = value