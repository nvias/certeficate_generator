import os
import io
import csv
from flask import Flask, redirect, url_for, request, send_file, render_template, flash
from werkzeug.utils import secure_filename
from certificate_generator import generate_certificate, list_templates

app = Flask(__name__)
app.config["TEMPLATE_UPLOAD_FOLDER"] = "templates"
app.config["ALLOWED_EXTENSIONS"] = {"png", "jpg", "jpeg", "csv"}
app.secret_key = "your_secret_key"  # For flash messages

# Ensure directories exist
os.makedirs(app.config["TEMPLATE_UPLOAD_FOLDER"], exist_ok=True)


def allowed_file(filename):
    """Check if the file has an allowed extension."""
    return "." in filename and filename.rsplit(".", 1)[1].lower() in app.config["ALLOWED_EXTENSIONS"]


@app.route("/")
def home():
    """Homepage for uploading templates, CSV, and generating certificates."""
    templates = list_templates()
    return render_template("home.html", templates=templates)


@app.route("/upload-template", methods=["POST"])
def upload_template():
    """Handle uploading of certificate templates."""
    if "file" not in request.files:
        flash("No file part")
        return redirect(url_for("home"))

    file = request.files["file"]
    if file.filename == "":
        flash("No selected file")
        return redirect(url_for("home"))

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config["TEMPLATE_UPLOAD_FOLDER"], filename))
        flash("Template uploaded successfully!")
        return redirect(url_for("home"))

    flash("Invalid file format. Please upload a PNG or JPG file.")
    return redirect(url_for("home"))


@app.route("/generate-certificate", methods=["POST"])
def generate_certificate_endpoint():
    """Generate a single certificate."""
    name = request.form.get("name")
    standing = request.form.get("standing", None)
    template_path = request.form.get("template")

    if not name or not template_path:
        flash("Name and template are required.")
        return redirect(url_for("home"))

    output_path = generate_certificate(name, template_path, standing=standing)

    return send_file(output_path, as_attachment=True, attachment_filename=f"{name}.png")


@app.route("/upload-csv", methods=["POST"])
def upload_csv():
    """Handle uploading of a CSV file and batch generate certificates."""
    if "file" not in request.files:
        flash("No file part")
        return redirect(url_for("home"))

    file = request.files["file"]
    if file.filename == "":
        flash("No selected file")
        return redirect(url_for("home"))

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join("uploads", filename)
        os.makedirs("uploads", exist_ok=True)
        file.save(filepath)

        templates = list_templates()
        template_path = request.form.get("template")
        if not template_path:
            flash("Please select a template.")
            return redirect(url_for("home"))

        # Generate certificates for each entry in the CSV
        with open(filepath, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name = row.get("name")
                standing = row.get("standing", None)
                generate_certificate(name, template_path, standing=standing)

        flash("Certificates generated successfully!")
        return redirect(url_for("home"))

    flash("Invalid file format. Please upload a CSV file.")
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
