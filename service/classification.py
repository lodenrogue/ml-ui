from service.base_service import BaseService
from sklearn.svm import SVC, LinearSVC
from sklearn.linear_model import SGDClassifier
from sklearn.ensemble import BaggingClassifier

class ClassificationService(BaseService):

	def __init__(self):
		self.models = {
			'SVC': SVC,
			'LinearSVC': LinearSVC,
			'SGDClassifier': SGDClassifier,
			'BaggingClassifier': BaggingClassifier
		}

	def get_models(self):
		return self.models