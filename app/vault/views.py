from flask import Flask, render_template, request, flash, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length

from . import vault
from . forms import CredentialForm
from .. import db
from ..models import Credential, User



@vault.route('/add_credential', methods=['GET', 'POST'])
@login_required
def add_credential():
    form = CredentialForm()
    if form.validate_on_submit():
        # create a new credential and save it to the database
        credential = Credential(
            user_id=current_user.id,
            website=form.website.data,
            username=form.username.data,
            password=form.password.data
        )
        db.session.add(credential)
        db.session.commit()
        flash('Credential added successfully')
        return redirect(url_for('main.index'))
    
    return render_template('vault/add_credential.html', form=form)


@vault.route('/delete_credential/<int:credential_id>')
@login_required
def delete_credential(credential_id):
    # get the credential to delete from the database
    credential = Credential.query.filter_by(id=credential_id, user_id=current_user.id).first()
    if credential is None:
        flash('Credential not found')
    else:
        # delete the credential from the database
        db.session.delete(credential)
        db.session.commit()
        flash('Credential deleted successfully')
    return redirect(url_for('main.index'))


@vault.route('/edit_credential/<int:credential_id>', methods=['GET', 'POST'])
@login_required
def edit_credential(credential_id):
    # get the credential to edit from the database
    credential = Credential.query.filter_by(id=credential_id, user_id=current_user.id).first()
    if credential is None:
        flash('Credential not found')
        return redirect(url_for('index'))

    form = CredentialForm(
        website=credential.website,
        username=credential.username,
        password=credential.encrypted_password
    )
    if form.validate_on_submit():
        # update the credential and save it to the database
        credential.website = form.website.data
        credential.username = form.username.data
        credential.password = form.password.data
        db.session.commit()
        flash('Credential updated successfully')
        return redirect(url_for('index'))
    return render_template('vault/edit_credential.html', form=form)


@vault.route('/credentials')
@login_required
def view_credentials():
    credentials = Credential.query.filter_by(user_id=current_user.id).all()
    user = User.query.filter_by(id=current_user.id).first()

    # Get hashed master password
    master_password = user.password_hash
    return render_template('vault/credentials.html', credentials=credentials, master_password=master_password)