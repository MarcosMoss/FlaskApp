from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from flaskblog import db, bcrypt
from flaskblog.models import User, Post
from flaskblog.users.forms import (RegistrationForm, LoginForm, UpdateAccountForm,
                                   RequestResetForm, ResetPasswordForm)
from flaskblog.users.utils import save_picture, send_reset_email


users = Blueprint('users', __name__)

@users.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password,name = form.name.data, surname = form.surname.data, gender = form.gender.data, home_number1 = form.home_number1.data, cell_phone = form.cell_phone.data, attending_school=form.attending_school.data, guardian_cell1 = form.guardian_cell1.data, guardian_cell2 = form.guardian_cell2.data,
        next_of_kin=form.next_of_kin.data, next_of_kin_number=form.next_of_kin_number.data, medical_dental_history=form.medical_dental_history.data,
        doctor=form.doctor.data, alternative_doctor=form.alternative_doctor.data, identity_number=form.identity_number.data, language=form.language.data, email2=form.email2.data, accountholder_cell=form.accountholder_cell.data,work_daytime_number=form.work_daytime_number.data, home_number2=form.home_number2.data,
        physical_address=form.physical_address.data, occupation=form.occupation.data, surname_and_initials=form.surname_and_initials.data, identity_number2=form.identity_number2.data, cellphone_number2=form.cellphone_number2.data, medical_aid_details=form.medical_aid_details.data,
        dependent_number=form.dependent_number.data, insurance_type=form.insurance_type.data, employer=form.employer.data, terms_acceptance=form.terms_acceptance.data,liabilty_acceptance=form.liabilty_acceptance.data)

        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form)


@users.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@users.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file

        current_user.name=form.name.data
        current_user.surname = form.surname.data
        current_user.home_number1=form.home_number1.data
        current_user.cell_phone = form.cell_phone.data
        current_user.guardian_cell1=form.guardian_cell1.data
        current_user.guardian_cell2=form.guardian_cell2.data
        current_user.next_of_kin = form.next_of_kin.data
        current_user.next_of_kin_number=form.next_of_kin_number.data
        current_user.name=form.name.data
        current_user.surname=form.surname.data
        current_user.home_number2=form.home_number2.data
        current_user.medical_dental_history=form.medical_dental_history.data
        current_user.doctor=form.doctor.data
        current_user.alternative_doctor=form.alternative_doctor.data
        current_user.identity_number=form.identity_number.data
        current_user.language=form.language.data
        current_user.accountholder_cell=form.accountholder_cell.data
        current_user.work_daytime_number=form.work_daytime_number.data
        current_user.postal_address=form.postal_address.data
        current_user.physical_address=form.physical_address.data
        current_user.occupation=form.occupation.data
        current_user.surname_and_initials=form.surname_and_initials.data
        current_user.identity_number2=form.identity_number2.data
        current_user.cellphone_number2=form.cellphone_number2.data
        current_user.medical_aid_details=form.medical_aid_details.data
        current_user.dependent_number=form.dependent_number.data
        current_user.insurance_type=form.insurance_type.data
        current_user.employer=form.employer.data
        current_user.email2 = form.email2.data
        current_user.email = form.email.data
        current_user.attending_school = form.attending_school.data
        db.session.commit()
        flash('Your account has been updated', 'success')
        return redirect(url_for('users.account'))

    elif request.method == 'GET':
        form.name.data=current_user.name
        form.surname.data = current_user.surname
        form.home_number1.data=current_user.home_number1
        form.cell_phone.data = current_user.cell_phone
        form.guardian_cell1.data=current_user.guardian_cell1
        form.guardian_cell2.data=current_user.guardian_cell2
        form.next_of_kin.data = current_user.next_of_kin
        form.next_of_kin_number.data=current_user.next_of_kin_number
        form.home_number2.data=current_user.home_number2
        form.medical_dental_history.data=current_user.medical_dental_history
        form.doctor.data=current_user.doctor
        form.alternative_doctor.data=current_user.alternative_doctor
        form.identity_number.data=current_user.identity_number
        form.language.data=current_user.language
        form.accountholder_cell.data=current_user.accountholder_cell
        form.work_daytime_number.data=current_user.work_daytime_number
        form.postal_address.data=current_user.postal_address
        form.physical_address.data=current_user.physical_address
        form.occupation.data=current_user.occupation
        form.surname_and_initials.data=current_user.surname_and_initials
        form.identity_number2.data=current_user.identity_number2
        form.cellphone_number2.data=current_user.cellphone_number2
        form.medical_aid_details.data=current_user.medical_aid_details
        form.dependent_number.data=current_user.dependent_number
        form.insurance_type.data=current_user.insurance_type
        form.employer.data=current_user.employer
        form.email2.data = current_user.email2
        form.attending_school.data = current_user.attending_school
        # current_user.email = form.email.data
        form.email.data = current_user.email

    image_file= url_for('static', filename='profile_pics/' + current_user.image_file )
    return render_template('account.html', title='Account', image_file=image_file, form=form)

@users.route("/user/<string:username>")
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user)\
        .order_by(Post.date_posted.desc())\
        .paginate(page=page, per_page=5)
    return render_template('user_posts.html', posts=posts, user=user)

@users.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instructions to reset your password.', 'info')
        return redirect(url_for('users.login'))
    return render_template('reset_request.html', title='Reset Password', form=form)


@users.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash('Your password has been updated! You are now able to log in', 'success')
        return redirect(url_for('users.login'))
    return render_template('reset_token.html', title='Reset Password', form=form)
