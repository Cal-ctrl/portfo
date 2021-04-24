from flask import Flask, render_template, url_for, request, redirect
import os
import csv
app = Flask(__name__)

@app.route('/') # the home route
def my_home():
    return render_template('index.html') # needs to be in a templates dir

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as data_file:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(data_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'something went wrong'
