from flask import Flask,render_template,request
import sqlite3 as sq
from ecomm import  userproduct 
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('project_login.html')


@app.route('/tlogin',methods=['GET','POST'])
def valid_hai():
    if request.method=='POST':
        conn=sq.Connection('product.db')
        user=request.form['user']
        pas=request.form['pass']
        cur=conn.execute('select * from user where username=? and password=?',(user,pas))
        if len(list(cur))==0:
            return render_template('project_login.html')
        else:
            l=userproduct(user)
            return render_template('e-comm.html',l=l)
            #return render_template('ecomm.py')``
        conn.close()

if __name__=='__main__':
    app.run(debug=True,port=3000)

