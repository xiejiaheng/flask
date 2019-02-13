from exts import db

class User(db.Model):
    __tablename__ = 'user'        #表名
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    user_name = db.Column(db.String(16))
    password = db.Column(db.String(16))
    name = db.Column(db.String(16))
    sex = db.Column(db.String(16))
    phone = db.Column(db.String(16))
    post = db.Column(db.String(16))

    def __init__(self, user_name,password,name,sex,phone,post):
        self.user_name = user_name
        self.password = password
        self.name = name
        self.sex = sex
        self.phone= phone
        self.post = post


class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    book_name = db.Column(db.String(16))
    book_price = db.Column(db.String(16))

    def __init__(self,book_name,book_price):
        self.book_name = book_name
        self.book_price = book_price

class goods(db.Model):
    __tablename__ = 'goodsinfo'

    goodsid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    goodsname = db.Column(db.String(16))
    goodstype = db.Column(db.String(16))
    goodsghs = db.Column(db.String(16))
    intoprice = db.Column(db.String(16))
    outprice = db.Column(db.String(16))
    inventory = db.Column(db.String(16))

    def __init__(self,goodsname,goodstype,goodsghs,intoprice,outprice,inventory):
        self.goodsname = goodsname
        self.goodstype = goodstype
        self.goodsghs = goodsghs
        self.intoprice = intoprice
        self.outprice = outprice
        self.inventory = inventory

