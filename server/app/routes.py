from app import app, db
from flask import render_template, redirect, url_for
from flask_login import login_required, current_user, login_user
from app.forms import RegistrationForm, LoginForm
from app.models import User

@app.route('/', methods=['GET', 'POST'])
def index():
    if current_user.is_authenticated:
        return render_template('home.html')
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if user.check_password(form.password.data):
                user.authenticated = True
                db.session.add(user)
                db.session.commit()
                login_user(user, remember=True)
                print('user logged in')
                return redirect(url_for("index"))
    return render_template('index.html', form=form)

@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(name = form.username.data, email = form.email.data)
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('/'))
    return render_template('register.html', form=form)


@app.route("/logout", methods=["GET"])
@login_required
def logout():
    """Logout the current user."""
    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    return redirect(url_for('index'))