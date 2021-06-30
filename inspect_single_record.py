import pandas
import numpy

# modelop.init
def begin():
    pass

# modelop.score
def action(data):
    
    print("\nData Received: ", data, flush=True)
    print(flush=True)
  
    # input data should be a dictionary, such as {"a":1, "b": "foo"}
  
    data = pandas.DataFrame([data])

    print("Pandas Version: ", pandas.__version__, flush=True)
    print(flush=True)
    print("Numpy  Version: ", numpy.__version__, flush=True)
    print(flush=True)

    print("\nData Shape: ", data.shape, flush=True)
    print(flush=True)
    print("\nData Types: ", data.dtypes.to_dict(), flush=True)
    print(flush=True)
    print("\nSample Rows: ", data.head(), flush=True)
    print(flush=True)
    print("\nNulls per Column: ", data.isna().sum().to_dict(), flush=True)
    print(flush=True)

    yield data.to_dict(orient='records')
