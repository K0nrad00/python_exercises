from flask import Flask, render_template

app = Flask(__name__)

# print(__name__) #DEBUG

# NOTE: js command to type in the browser 'Console' that let's edit the content:
# document.body.contentEditable=true

@app.route("/")
def home():
    return render_template("index1.html")

# NOTE: /# work /#contact /twitter routes don't work  - no requirement

if __name__ == "__main__":
    app.run(debug=True)

