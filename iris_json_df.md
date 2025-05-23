```python
import pandas as pd
df = pd.read_json('iris.json')
print(df)
```

         sepalLength  sepalWidth  petalLength  petalWidth    species
    0            5.1         3.5          1.4         0.2     setosa
    1            4.9         3.0          1.4         0.2     setosa
    2            4.7         3.2          1.3         0.2     setosa
    3            4.6         3.1          1.5         0.2     setosa
    4            5.0         3.6          1.4         0.2     setosa
    ..           ...         ...          ...         ...        ...
    145          6.7         3.0          5.2         2.3  virginica
    146          6.3         2.5          5.0         1.9  virginica
    147          6.5         3.0          5.2         2.0  virginica
    148          6.2         3.4          5.4         2.3  virginica
    149          5.9         3.0          5.1         1.8  virginica
    
    [150 rows x 5 columns]



```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 150 entries, 0 to 149
    Data columns (total 5 columns):
     #   Column       Non-Null Count  Dtype  
    ---  ------       --------------  -----  
     0   sepalLength  150 non-null    float64
     1   sepalWidth   150 non-null    float64
     2   petalLength  150 non-null    float64
     3   petalWidth   150 non-null    float64
     4   species      150 non-null    object 
    dtypes: float64(4), object(1)
    memory usage: 6.0+ KB



```python

```
