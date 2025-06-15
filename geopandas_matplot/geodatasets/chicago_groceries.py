import geodatasets
import pandas as pd
import geopandas
import matplotlib.pyplot as plt

chicago = geopandas.read_file(geodatasets.get_path("geoda.chicago_commpop"))
groceries = geopandas.read_file(geodatasets.get_path("geoda.groceries"))
# examine the chicago dataframe
chicago.head(17)
groceries.head()
chicago.plot();
groceries.plot()
# plot by population
chicago.plot(column="POP2010");
chicago.plot(
    column='POP2010',
    legend=True,
    legend_kwds={"label": "population in 2010", "orientation": "horizontal"},
);

