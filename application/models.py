# coding:utf-8
from application.exts import db


# 管理员表
class Admin(db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_pwd(self, pwd):
        if pwd == self.password:
            return True
        return False

    def __repr__(self):
        return self.username, self.password


# 还款表
class Debt(db.Model):
    __tablename__ = 'debt'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    credit_id = db.Column(db.String(30), db.ForeignKey('credit.credit_id'), nullable=True)
    debt_date = db.Column(db.Date, nullable=False)
    sum_money = db.Column(db.DECIMAL(15, 1), nullable=False)

    def __init__(self, credit_id, debt_date, sum_money):
        self.credit_id = credit_id
        self.debt_date = debt_date
        self.sum_money = sum_money

    def __repr__(self):
        return self.sum_money


# 消费表
class Consume(db.Model):
    __tablename__ = 'consume'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    credit_id = db.Column(db.String(30), db.ForeignKey('credit.credit_id'), nullable=True)
    consume_date = db.Column(db.Date, nullable=False)
    sum_money = db.Column(db.DECIMAL(15, 1), nullable=False)
    Ctype = db.Column(db.String(20), nullable=False)

    def __init__(self, credit_id, Ctype, consume_date, sum_money):
        self.credit_id = credit_id
        self.Ctype = Ctype
        self.consume_date = consume_date
        self.sum_money = sum_money

    def __repr__(self):
        return '<Consume %d>' % self.credit_id


# 信用卡表
class Credit(db.Model):
    __tablename__ = 'credit'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    credit_id = db.Column(db.String(30), nullable=False, unique=True)
    limit = db.Column(db.String(20), nullable=False)
    overMoney = db.Column(db.String(20), nullable=False)
    creditName = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(110), db.ForeignKey('user.phone'), nullable=True)
    vailDate = db.Column(db.Date)
    cdt_status = db.Column(db.SmallInteger, nullable=False)  # 0 为冻结 1 为正常
    idCard = db.Column(db.String(24), nullable=False)
    email = db.Column(db.String(24))
    # 还款表关系
    debts = db.relationship('Debt', backref='credit', lazy='dynamic')
    consumes = db.relationship('Consume', backref='credit', lazy='dynamic')
    deals = db.relationship('Deal', backref='credit', lazy='dynamic')

    def __init__(self, email, creditid, limit, overmoney, creditname, phone, vaildate, cdtstatus, idcard):
        self.credit_id = creditid
        self.limit = limit
        self.overMoney = overmoney
        self.creditName = creditname
        self.phone = phone
        self.vailDate = vaildate
        self.cdt_status = cdtstatus
        self.idCard = idcard
        self.email = email

    def __repr__(self):
        return self.creditName, self.overMoney, \
               self.credit_id, self.limit, self.vailDate, self.cdt_status


# 交易表
class Deal(db.Model):
    __tablename__ = 'deal'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    credit_id = db.Column(db.String(30), db.ForeignKey('credit.credit_id'), nullable=True)
    sum_money = db.Column(db.DECIMAL(15, 1), nullable=False)
    deal_date = db.Column(db.Date, nullable=False)
    deal_type = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)

    def __init__(self, credit_id, deal_date, deal_type, sum_money, description):
        self.credit_id = credit_id
        self.sum_money = sum_money
        self.deal_date = deal_date
        self.deal_type = deal_type
        self.description = description

    def __repr__(self):
        return '<Deal %d>' % self.credit_id


# 用户表
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(110), nullable=True, unique=True)  # 外键必须在主表中唯一或者为主键
    name = db.Column(db.String(100), default='')
    age = db.Column(db.Integer, default=0)
    sex = db.Column(db.SmallInteger, default=1)  # 1 为男 0 为女
    email = db.Column(db.String(20), default='')
    job = db.Column(db.String(10), default='')
    idCard = db.Column(db.String(24), default='')
    address = db.Column(db.String(30), default='')
    applycard = db.relationship('ApplyCard', backref='user')

    def __repr__(self):
        return self.username, self.id, self.phone, self.name, self.age, \
               self.sex, self.email, self.job, self.idCard, self.address

    def check_pwd(self, pwd):
        if pwd == self.password:
            return True
        return False


# 银行信息表
class BankInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    posturl = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date)

    def __init__(self, title, posturl, date):
        self.title = title
        self.posturl = posturl
        self.date = date


# 申请表
class ApplyCard(db.Model):
    __tablename__ = 'applycard'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    limit = db.Column(db.String(100), nullable=False)
    idcard = db.Column(db.String(24), nullable=False)
    phone = db.Column(db.String(110), db.ForeignKey('user.phone'))

    def __init__(self, name, limit, idcard, phone):
        self.name = name
        self.limit = limit
        self.idcard = idcard
        self.phone = phone

    def __repr__(self):
        return '<ApplyCard %s>' % self.name
