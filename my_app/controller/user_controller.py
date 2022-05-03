from flask import render_template, request, redirect, url_for
from my_app.handler.tweets_handler import tweets_handler
from my_app.handler.database_handler import database_handler
from . import bp

@bp.route('/user_profile/<user_name>', methods=["GET"])
def user_profile(user_name):
    """
    It shows all the information of a specified user
    Args:
        user_name: the name of the user which information will be shown
    Returns:
        user_profile.html: if database accessing and reading were succesfully
        error: otherwise
    """
    db_handler = database_handler()
    user_info = db_handler.get_user_info(user_name)
    data={
        'user': user_info
    }
    
    return render_template('user_profile.html', data=data)

@bp.route('/show_tweets/<user_name>', methods=["GET"])
def show_tweets(user_name):
    """
    It shows the last five tweets of a specified user
    Args:
        user_name: the name of the user which tweets will be shown
    Returns:
        show_tweets.html: if database accessing and reading and tweets reading were succesfully
        error: otherwise
    """
    db_handler = database_handler()
    user_info = db_handler.get_user_info(user_name)
    user_name = user_info["twitter_user_name"]
    tw_handler = tweets_handler()
    tweets = tw_handler.get_tweets_from_name(user_name)
    
    data={
        'user': user_info,
        'tweets': tweets
    }
    
    return render_template('show_tweets.html', data=data)

@bp.route('/edit_user_profile/<user_name>', methods=["GET"])
def edit_user_profile(user_name):
    """
    It lets you edit the information stored in the database of a specified user
    Args:
        user_name: the name of the user which information will be edited
    Returns:
        edit_user_profile.html: if database accessing, reading and writting were succesfully
        error: otherwise
    """
    db_handler = database_handler()
    user_info = db_handler.get_user_info(user_name)
    user_name = user_info["twitter_user_name"]
    tw_handler = tweets_handler()
    tweets = tw_handler.get_tweets_from_name(user_name)
    
    data={
        'user': user_info,
        'tweets': tweets
    }
    
    return render_template('edit_user_profile.html', data=data)

@bp.route('/update_user_profile/<user_name>', methods=["POST"])
def update_user_profile(user_name):
    """
    It lets you update the information stored in the database of a specified user
    Args:
        user_name: the name of the user which information will be updated
        title: the title of the user which information will be updated
        url_image: the url_image of the user which information will be updated
        description: the description of the user which information will be updated
    Returns:
        edit_user_profile.html: if database accessing, reading and writting were succesfully
        error: otherwise
    """
    new_user_info = {
        'user_name' : user_name,
        'title' : request.form['user_title'],
        'image_url' : request.form['user_image'],
        'description' : request.form['user_description']
    }

    db_handler = database_handler()
    db_handler.update_user_info(new_user_info)

    return redirect(url_for("user.user_profile", user_name=user_name))
