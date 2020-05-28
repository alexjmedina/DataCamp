# Import packages
from sqlalchemy import create_engine
import ____ as ____

# Create engine: engine


# Execute query and store records in DataFrame: df
df = pd.read_sql_query(____, ____)

# Print head of DataFrame
print(df.head())

# Open engine in context manager and store query result in df1
with engine.connect() as con:
    rs = con.execute("SELECT * FROM Album")
    df1 = pd.DataFrame(rs.fetchall())
    df1.columns = rs.keys()

# Confirm that both methods yield the same result
print(df.equals(df1))