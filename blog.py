from flask import *
import markdown
import os

# Create the Python3 Flask App
app = Flask(__name__)

# Functions
def read_markdown(file):
	with (open(app.root_path + '/markdown/'+file)) as markdown_file:
		content = markdown_file.read()
		return markdown.markdown(content)

# Define the endpoints
@app.route('/')
def index():
	return render_template('pages_template.html', content=read_markdown('index.md'))
@app.route('/blog/<name>')
def blog(name):
	# Show the Blog corresponding to the name
	return render_template('blog_template.html', content=read_markdown('blog/'+name+'.md'))

# Run the App
if __name__ == '__main__':
	app.run(debug=True)