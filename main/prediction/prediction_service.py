import json

class PredictionService:
	__algorithms = None


	def __init__(self):
		if PredictionService.__algorithms is None:
			PredictionService.__algorithms = self.read_algorithms()


	def read_algorithms(self):
		with open('data/algorithms.json', 'r') as f:
			js = f.read()
			return json.loads(js)


	def get_pred_types(self):
		return list(PredictionService.__algorithms.keys())


	def get_algos(self, selected_pred_type):
		return PredictionService.__algorithms[selected_pred_type]
