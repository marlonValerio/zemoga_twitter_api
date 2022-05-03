from flask import Flask, render_template
from .handler.database_handler import database_handler

my_app=Flask(__name__)

@my_app.route('/')
def index():
    """
    Input endpoint. It shows you all the user stored in the database
    Returns:
        users_grid.html: if database accessing and reading were succesfully
        error: otherwise
    """
    db_handler = database_handler()
    users = db_handler.get_users()
    
    data={
        'users': users
    }

    return render_template('users_grid.html', data=data)

from .controller import user_controller
my_app.register_blueprint(user_controller.bp)