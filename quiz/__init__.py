
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'btEjYQQonbKyuYL_FgFID9ywlldk_wgaEXmcMOoFpd4LJVM3UHy-AlmsOutey6Q3BAZR5-_dpg'


from quiz import routes
