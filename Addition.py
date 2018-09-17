from flask import Flask
app = Flask(__name__)

# Webservice for addition of two numbers
# Accept two variables via the URL
# example  http://localhost:5000/addition/2/10 gives output 20

@app.route('/addition/<int:a>/<int:b>')
def myFunc(a,b):
    
# Multiply two numbers and return them 
	return str(a + b);
  

# Convert them to string before returning

if __name__ == '__main__':
   app.run(debug = True)