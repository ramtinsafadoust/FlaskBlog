from flask import Flask

app=Flask(__name__)


@app.route('/')
def index():
    return "BLOG HOME"



from mod_Admin import admin
app.register_blueprint(admin)

