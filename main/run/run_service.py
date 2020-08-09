from model.train_request import TrainRequest

class RunService:
	def run(self):
		req = TrainRequest.get_instance()
		print(req)