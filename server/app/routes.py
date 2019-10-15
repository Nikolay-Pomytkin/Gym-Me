from app import app, db
from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user, login_user, logout_user
from app.forms import RegistrationForm, LoginForm, WorkoutForm
from app.models import User

@app.route('/', methods=['GET', 'POST'])
def index():
    if current_user.is_authenticated:
        return render_template('base/index.html')
    return render_template('base/home.html')

@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(name = form.username.data, email = form.email.data)
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('user/register.html', form=form)

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    '''Login a new user.'''
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            user.authenticated = True
            db.session.add(user)
            db.session.commit()
            login_user(user, remember=True)
            flash(('Successfully logged in!',"success"))
            return redirect(url_for("index"))
    return render_template('user/login.html', form=form)

@app.route('/workout/new',  methods=['GET', 'POST'])
@login_required
def new_workout():
    '''Create a new workout.'''
    form = WorkoutForm()
    return render_template("workout/new_workout.html", form=form)

@app.route('/workout/<workout_id>')
@login_required
def workout(workout_id, methods=['GET']):
    '''Display workout by id.'''
    return ""

