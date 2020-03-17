from . import admin
from flask import session





@admin.route('/')
def index():
    return 'HELLO from admin Index'



@admin.route('/login/')
def login():
    print(session)
    return "1"