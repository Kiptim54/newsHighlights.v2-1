from flask import render_template,request,redirect,url_for
from . import main
from flask import render_template
    
@main.route('/')
def index():
    '''
    function renders the landing page with news sources
    '''
    title = "NewsHighlighs | Home"

    return render_template('index.html', title=title)

@main.route('/articles')
def articles():
    '''
    function shows the news articles
    '''
    title= "NewsHighlighs | Articles"
    return render_template('articles.html', title =title)
