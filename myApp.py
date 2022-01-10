from flask import Flask, render_template, request, redirect, url_for
import os, sys
app = Flask(__name__)

app.config["FILE_UPLOADS"] = "/home/haris/Project/uploads"
app.config["ALLOWED_FILE_EXTENSIONS"] = ["TXT"]
# import the path of the scripts 
app.config["FILE_SCRIPTS"] = "/home/haris/Project/scripts"
sys.path.insert(0,app.config["FILE_SCRIPTS"])
import editor

def allowedFile(filename):
    if not "." in filename:
        return False
    # split filename from the right at the . and get first element from the right
    ext = filename.rsplit(".", 1)[1]
    if ext.upper() in app.config["ALLOWED_FILE_EXTENSIONS"]:
        return True
    else:
        return False

@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def home_page():
    if request.method == "POST":
        if request.files:
            uploaded_file = request.files["file"]
            # if the file does not have a name
            if uploaded_file.filename == "":
                return redirect(request.url)
            # check if file extension is valid, must be txt
            if not allowedFile(uploaded_file.filename):
                print("File extension is not allowed")
                return redirect(request.url)

            uploaded_file.save(os.path.join(app.config["FILE_UPLOADS"], uploaded_file.filename))
            print("File has been saved.")
            # redirect to page where we output the results
            return redirect(url_for("file_output_page", filename = uploaded_file.filename))
    return render_template('home.html')

#@app.route("/file_output", methods=["GET", "POST"])
@app.route("/file_output/<filename>")
def file_output_page(filename):
    return render_template('file_output.html', file_output = editor.extractFile(app.config["FILE_UPLOADS"], filename))