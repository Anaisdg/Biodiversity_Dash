from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import belly_button


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/names')
def names():
    names_data = belly_button.names()
    return render_template("names.html", names_data=names_data)

@app.route('/otu')
def otu():
    otu_data = belly_button.otu_list()
    return render_template("otu.html", otu_data=otu_data)

@app.route('/metadata/<sample>')
def metadata(sample):
    metadata_data  = belly_button.json(sample)
    values = list(metadata_data.values())
    keys = list(metadata_data.keys())
    return render_template("metadata.html", sample=sample, metadata_data=metadata_data, values=values, keys = keys)

@app.route('/wfreq/<sample2>')
def wfreq(sample2):
    wfreq_data  = belly_button.washing()[sample2]
    return render_template("wfreq.html", sample2=sample2, wfreq_data=wfreq_data)

@app.route('/samples/<sample3>')
def samples(sample3):
    samples_data = belly_button.samples_data(sample3)
    return render_template("samples.html", samples_data=samples_data)

if __name__ == "__main__":
    app.run(debug=True)
