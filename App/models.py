from App import db,login_manager

from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model,UserMixin):
    id = db.Column(db.Integer(),primary_key=True)
    username = db.Column( db.String(30),unique=True,nullable=False)
    email =db.Column(db.String(100),unique=True,nullable=False)
    password = db.Column( db.String(40),nullable=False)
    own_products =db.relationship('Product',backref='owned_user')
     
    def __repr__(self):
        return f"{self.id} {self.username} {self.password}"

class Category(db.Model):
    id = db.Column( db.Integer(),primary_key=True)
    category_label = db.Column( db.String(30),nullable= False,unique=True)
    products = db.relationship("Product",backref="category",lazy=True)

class Product(db.Model):
    id = db.Column( db.Integer(),primary_key=True)
    product_name = db.Column( db.String(30),nullable= False,unique=True)
    description = db.Column( db.String(30),nullable= False)
    quantity =db.Column(db.Numeric(),nullable=False)
    price=db.Column(db.Numeric(),nullable=False)
    user_id = db.Column(db.Integer(),db.ForeignKey('user.id'))
    categorie_id = db.Column(db.Integer(),db.ForeignKey('category.id'),nullable=False)
    def __repr__(self):
        return f"name: {self.product_name}, quntity: {self.quantity} , price: {self.price}"



