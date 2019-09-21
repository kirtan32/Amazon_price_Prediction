import sqlite3 as sql
from pandas import read_csv
from sklearn.tree import DecisionTreeRegressor
def prid():
    df = read_csv('product_with_vender.csv')
    x = df.iloc[:,[1,3]].values
    y = df.iloc[:,2].values
    reg = DecisionTreeRegressor()
    reg.fit(x,y)
    #from sklearn.metrics import r2_score,mean_absolute_error
    #r2_score(y,reg.predict(x))

def userproduct(name):
    try:
        conn=sql.connect("product.db")
        #cursor1=conn.execute("select * from user where username=?",(name,))
        cursor2 = conn.execute("select product_name,seller_price,amazon_price,image from user_product where username = ?",(name,))
        return list(cursor2)
    except Exception as e:
        return e
    finally:
        conn.close()
