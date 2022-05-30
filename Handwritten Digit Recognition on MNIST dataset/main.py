from scipy.io import arff
import pandas as pd

data = arff.loadarff('mnist_784.arff')
df = pd.DataFrame(data[0])

df.head()
