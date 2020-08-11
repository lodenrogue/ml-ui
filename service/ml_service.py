from service.regression import RegressionService
from service.classification import ClassificationService

class MLService:

	def __init__(self):
		self.regression_service = RegressionService()
		self.classificaton_service = ClassificationService()


	def train(self, train_request):
		pred_type = train_request.pred_type

		if pred_type == 'Regression':
			return self.regression_service.train(train_request)

		elif pred_type == 'Classification':
			return self.classificaton_service.train(train_request)

		else:
			return 'Unknown prediction type {}'.format(pred_type)