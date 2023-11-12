# Flask modules
from flask   import render_template, request
from jinja2  import TemplateNotFound

# App modules
from apps import app

#example
# from apps.view import user
from apps.view import options

# App main route + generic routing
@app.route('/')
def index():

    try:
        
        image_data = [
            {"url": "https://plus.unsplash.com/premium_photo-1666787754195-2a1ff4f79564?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"},
            {"url": "https://images.unsplash.com/photo-1682687220208-22d7a2543e88?q=80&w=1975&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"},
            {"url": "https://images.unsplash.com/photo-1699536813782-54998ebe0578?q=80&w=1964&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"},
            {"url": "https://images.unsplash.com/photo-1682687220336-bbd659a734e7?q=80&w=1975&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"}
        ]
    
        return render_template('index.html', image_data=image_data)
    
    except TemplateNotFound:
        print("404")
        # return render_template('home/page-404.html'), 404

@app.route('/test')
def test():

    try:

        return render_template( 'test.html')
    
    except TemplateNotFound:
        print("404")


@app.route('/b')
def b():

    try:

        return render_template( 'b.html')
    
    except TemplateNotFound:
        print("404")
