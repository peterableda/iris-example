# Read the fitted model from the file model.pkl
# and define a function that uses the model to
# predict petal width from petal length

import pickle
import time

model = pickle.load(open('model.pickle', 'rb'))

def run(args):
  iris_x = float(args.get('length'))
  time.sleep(5)
  result = model.predict(iris_x)
  return result[0][0]
