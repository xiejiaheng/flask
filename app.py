from flask import Flask,render_template,request,url_for,session,redirect
from exts import db
from flask_paginate import Pagination,get_page_parameter
import config
from models import User,goods
from functools import wraps


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

def login_required(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if session.get('id'):
            return func(*args,**kwargs)
        else:
            return redirect(url_for('login'))
    return wrapper

@app.route('/',methods=['GET','POST'])
def login():
    return render_template('login.html')

#登录
@app.route('/login',methods=['POST'])
def slogin():
    username = request.form['username']
    password = request.form['password']
    user = User.query.filter(User.user_name == username,User.password == password).first()

    if user:
        session['id'] = user.id
        return redirect(url_for('home'))
    else:
        return  render_template('login.html',cuowu='密码或账户输入错误')

# 上下文钩子
@app.context_processor
def my_context_processor():
    user_id = session.get('id')
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user:
            return {'user': user}
    return {}

#注销登录
@app.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('login'))

#商场概述
@app.route('/home')
@login_required
def home():
    return render_template('home.html')

#商品详情
@app.route('/shoopinfo')
def shoopinfo():
    u = goods.query.all()
    return render_template('shoopinfo.html',u=u)

#错误处理404
@app.errorhandler(404)
def internal_error(error):
    return render_template('404.html'), 404

#错误处理500
@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500

#查找
@app.route('/shoopinfo',methods=['POST'])
def afind():
    goodsname = request.form['bookpn']
    u = goods.query.filter(goods.goodsname == goodsname).all()
    return render_template('shoopinfo.html',u=u)




#添加商品
@app.route('/add')
def addpage():
    return render_template('add.html')
#添加商品
@app.route('/add',methods=['POST'])
def add():
    gdname = request.form['goodsname']
    gdtype = request.form['goodstype']
    gdghs = request.form['goodsghs']
    inprice = request.form['intoprice']
    ouprice = request.form['outprice']
    inv = request.form['inv']
    gd = goods.query.filter(goods.goodsname == gdname).first()
    if gd:
        return u'该商品已经存在'
    else:
        good = goods(goodsname=gdname, goodstype=gdtype,goodsghs=gdghs,intoprice=inprice,outprice=ouprice,inventory=inv)
        db.session.add(good)
        db.session.commit()
        return redirect(url_for('shoopinfo'))

#删除
@app.route('/shoopinfo/')
def delete():
    gdid = request.args.get('Gdid')
    article1 = goods.query.filter(goods.goodsid == gdid).first()
    db.session.delete(article1)
    db.session.commit()
    return redirect('/shoopinfo')

#改商品信息
@app.route('/shoopinfo/update/<goodsid>',methods = ['GET', 'POST'])
def update_note(goodsid):
    if request.method == 'GET':
        gd = goods.query.filter(goods.goodsid == goodsid).first()
        return render_template('update.html',gd = gd)
    else:
        gdname = request.form['goodsname']
        gdtype = request.form['goodstype']
        gdghs = request.form['goodsghs']
        inprice = request.form['intoprice']
        ouprice = request.form['outprice']
        inv = request.form['inv']
        book = goods.query.filter(goods.goodsid == goodsid).update({'goodsname':gdname,'goodstype':gdtype,'goodsghs':gdghs,'intoprice':inprice,'outprice':ouprice,'inventory':inv})
        db.session.commit()
        return redirect('/shoopinfo')


#员工详情
@app.route('/user')
def user():
    u = User.query.all()
    return render_template('user.html',u=u)

#删除
@app.route('/user/')
def deleteuser():
    gdid = request.args.get('uid')
    article1 = User.query.filter(User.id == gdid).first()
    db.session.delete(article1)
    db.session.commit()
    return redirect('/user')

#添加员工
@app.route('/adduser')
def adduser():
    return render_template('adduser.html')

#添加员工
@app.route('/adduser',methods=['POST'])
def adduser1():
    gdname = request.form['uname']
    gdtype = request.form['usex']
    gdghs = request.form['u_name']
    inprice = request.form['upd']
    ouprice = request.form['upt']
    inv = request.form['uphone']
    gd = User.query.filter(User.name == gdname).first()
    if gd:
        return u'该信息已经存在'
    else:
        good = User(name=gdname, sex=gdtype,user_name =gdghs,password=inprice,post=ouprice,phone=inv)
        db.session.add(good)
        db.session.commit()
        return redirect(url_for('user'))

# 改员工信息
@app.route('/user/upuser/<id>', methods=['GET', 'POST'])
def update_user(id):
    if request.method == 'GET':
        gd = User.query.filter(User.id == id).first()
        return render_template('upuser.html', gd=gd)
    else:
        gdname = request.form['goodsname']
        gdtype = request.form['goodstype']
        gdghs = request.form['goodsghs']
        inprice = request.form['intoprice']
        ouprice = request.form['outprice']
        inv = request.form['inv']
        Useru = User.query.filter(User.id == id).update({'name': gdname, 'sex': gdtype, 'user_name': gdghs, 'password': inprice, 'post': ouprice,'phone': inv})
        db.session.commit()
        print(ouprice)
        return redirect('/user')


if __name__ == '__main__':
    app.run()
