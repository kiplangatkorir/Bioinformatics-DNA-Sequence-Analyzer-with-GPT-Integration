from flask import render_template, request
from app import app
from app.dna_analyzer import analyze_dna_sequence
from app.gpt_integration import gpt_analysis

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    dna_sequence = request.form['dna_sequence']
    analysis_result = analyze_dna_sequence(dna_sequence)
    gpt_result = gpt_analysis(dna_sequence)
    return render_template('result.html', analysis_result=analysis_result, gpt_result=gpt_result)
