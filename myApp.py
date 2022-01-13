from flask import Flask, render_template, request, redirect, url_for
import os, sys
app = Flask(__name__)

app.config["FILE_UPLOADS"] = "/var/www/html/FlaskDir/uploads"
app.config["ALLOWED_FILE_EXTENSIONS"] = ["TXT"]
# import the path of the scripts 
app.config["FILE_SCRIPTS"] = "/var/www/html/FlaskDir/scripts"
sys.path.insert(0,app.config["FILE_SCRIPTS"])
import editor # the python script that makes all the magic happen

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
            # first delete any .txt files that exist in uploads
            editor.clearUploads(app.config["FILE_UPLOADS"])
            # no continue to work on the file user is currently uploading
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

@app.route("/file_output/<filename>")
def file_output_page(filename): 
    return render_template('file_output.html', file_output = editor.extractFile(app.config["FILE_UPLOADS"], filename))
    

@app.route("/file_output")
def empty_file_output_page():
    return render_template('file_output.html')

if __name__ == "__main__":
    app.run()
