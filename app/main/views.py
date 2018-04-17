from flask import render_template,request,redirect,url_for
from . import main
from flask import render_template
    
@main.route('/')
def index():
    '''
    function renders the landing page
    '''
    title = "NewsHighlighs | Home"

    return render_template('index.html', title=title)