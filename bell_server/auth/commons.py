from functools import wraps
from flask import g, request, redirect, url_for, request

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        cur = g.db.execute('select count(*) from token where user_token = ?'
                ,[request.headers.get('token')])
        if request.headers.get('token') is None:
            print("No token")

        g.db.commit()
        result = cur.fetchone()

        if result[0] == 0:
            return "Incorrect token", 404
        else:
            return f(*args, **kwargs)
    return decorated_function
