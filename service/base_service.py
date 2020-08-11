import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

class BaseService:

	def train(self, train_request):
		prediction_label = train_request.pred_column
		algorithm = train_request.algo
		test_size = (100 - train_request.train_split) / 100

		df = pd.read_csv(train_request.csv_path)

		X = np.array(df.drop([prediction_label], 1))
		y = np.array(df[prediction_label])

		X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size)

		model = self.get_models()[algorithm]()
		model.fit(X_train, y_train)

		accuracy = model.score(X_test, y_test)
		print('Accuracy: {}'.format(accuracy))


	def get_models(self):
		pass