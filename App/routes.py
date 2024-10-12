from App import app,db,bcrypt
from flask import render_template,url_for,flash,get_flashed_messages,redirect
from App.forms import LoginForm,RegisterForm,ProductForm
from App.models  import Product,User,Category
from flask_login import login_user,logout_user,login_required


@app.route('/')
@app.route('/home')
def home():
    return render_template('Home.html')



@app.route('/shop')
@login_required
def market():
    items =Product.query.all()
    return render_template('market.html',items=items)


@app.route('/login',methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if bcrypt.check_password_hash(password=form.password.data,pw_hash=user.password):
                flash(f"welcome {user.username}",category='success')
                login_user(user)
                return redirect(url_for('market'))
            else :
                flash("password is incorrect. try again",category='danger')
        else:
            flash('this account is not found . sign up',category='danger')
            return redirect(url_for('register'))
        
    return render_template('login.html',form=form)

@app.route('/register',methods=["GET","POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,email=form.email.data,password=bcrypt.generate_password_hash(form.password.data).decode('utf-8'))
        db.session.add(user)
        db.session.commit()
        flash(message="your account is created . please log in ",category="success")
        return redirect(url_for("login"))
    if form.errors !={}:
        for err in form.errors.values():
            flash(err,category='danger')
    return render_template('register.html',form=form)


@app.route('/logout')
def logout():
    flash('you are logout ',category='info')
    logout_user()
    return redirect(url_for('home'))



@app.route('/add',methods=['GET','POST'])
def add_product():
    categorys = Category.query.all()
    form =ProductForm()
    return render_template('add.html',form=form,categorys=categorys)


@app.route('/update/<id>')
def update_page(id):
    return "update"


@app.route('/delete/<id>')
def delete_page(id):
    return "update"