import pandas
import numpy

# modelop.init
def begin():
    pass

# modelop.score
def action(data):
  
    # input data should be a dictionary, such as {"a":1, "b": "foo"}
  
    data = pandas.DataFrame([data])

    print("Pandas Version: ", pandas.__version__, flush=True)
    print()
    print("Numpy  Version: ", numpy.__version__, flush=True)
    print()

    print("\nData Shape: ", data.shape, flush=True)
    print()
    print("\nData Types: ", data.dtypes.to_dict(), flush=True)
    print()
    print("\nSample Rows: ", data.head(), flush=True)
    print()
    print("\nNulls per Column: ", data.isna().sum().to_dict(), flush=True)
    print()

    yield data.to_dict(orient='records')
