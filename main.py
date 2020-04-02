from flask import Flask, render_template, url_for, session, request, redirect, escape, jsonify
from util import json_response

import data_handler
import persistence
import os

app = Flask(__name__)

app.secret_key= os.urandom(24)

@app.route("/")
def index():
    """
    This is a one-pager which shows all the boards and cards
    """
    if 'username' in session:
        user = escape(session['username'])
        message = 'Logged in as ' + user
        return render_template('index.html', message = message)
    message = 'Not logged in'
    return render_template('index.html', message = message)


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        if request.form['password'] == request.form['password2']:
            form_data = {
                'username': request.form['username'],
                'password': persistence.hash_password(request.form['password'])
            }
            persistence.add_user(form_data)
            return redirect(url_for('index'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        input_pass = request.form['password_login']
        db_pass = persistence.login(request.form['username_login'])
        if persistence.verify_password(input_pass, db_pass['password']):
            session['username'] = request.form['username_login']
            return redirect(url_for('index'))


@app.route('/logout')
def logout():
    #remove username from session
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route("/get-boards")
@json_response
def get_boards():
    """
    All the boards
    """
    # if 'username' in session:
    #     user = escape(session['username']
    #     return persistence.get_user_boards(user)
    return persistence.get_public_boards()


@app.route("/get-cards/<int:board_id>")
@json_response
def get_cards_for_board(board_id: int):
    """
    All cards that belongs to a board
    :param board_id: id of the parent board
    """
    return data_handler.get_cards_for_board(board_id)


@app.route("/add-card", methods=['POST'])
def add_card():
    if request.method == 'POST':
        card_title = request.json['cardTitle']
        board_id = request.json['boardId']
        status_id = request.json['statusId']
        result = persistence.add_card(card_title,board_id,status_id)
        return jsonify(result)
    return redirect(url_for('index'))



def main():
    app.run(debug=True)

    # Serving the favicon
    with app.app_context():
        app.add_url_rule('/favicon.ico', redirect_to=url_for('static', filename='favicon/favicon.ico'))


if __name__ == '__main__':
    main()
