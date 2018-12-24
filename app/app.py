#!flask/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, send_file
from forms import AlignmentForm, ConversionForm, BufferForm, BrothForm, \
 OligoForm, TranslateForm
from calculator import protein_mole, buffer_mass, broth_mehod
from biohack import Alignment, Oligo, Translate

app = Flask(__name__)
app.config['SECRET_KEY'] = '_5#y2L"F4Q8zxec]/'


@app.route('/')
def index():
    return render_template('index.html', title='Biohack')


@app.route('/about')
def about():
    return render_template('about.html', title='About biohack')


@app.route('/tools')
def tools():
    return render_template('tools.html', title='Tools of biohack')


@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', title="Taeyoon's portfolio")


@app.route('/temp')
def temp():
    return render_template('cal_temp.html', title="temp page for test")


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html', title='404 error'), 404


@app.errorhandler(500)
def internal_server_error(error):
    app.logger.error('Server Error: %s', (error))
    return render_template('500.html'), 500


@app.route('/alignment', methods=['GET', 'POST'])
def alignment():
    form = AlignmentForm()
    result = None
    if form.validate_on_submit():
        target = ''.join(form.target_seq.data.split())
        query = ''.join(form.query_seq.data.split())
        Alignment(target, query)
        result = 'Download'
    return render_template(
            'seq_alignment.html', title='Sequence alignment',
            form=form, result=result)


@app.route('/getfile')  # this is a job for GET, not POST
def getfile():
    return send_file(
        'static/alignment_result.txt',
        mimetype='text/*',
        attachment_filename='alignment_result.txt',
        as_attachment=True)


@app.route('/molar', methods=['GET', 'POST'])
def calculate():
    form = ConversionForm()
    result = None
    if form.validate_on_submit():
        mass_unit = float(form.mass_unit.data)
        volume_unit = float(form.volume_unit.data)
        molecular_weight = form.molecular_weight.data
        mass = form.mass.data
        volume = form.volume.data
        result = protein_mole(mass, molecular_weight,
                              mass_unit) * 1000 / (volume * volume_unit)
    return render_template(
            'cal_molar.html', form=form, result=result,
            title='Protein molar calculator')


@app.route('/buffer', methods=['GET', 'POST'])
def make_buffer():
    form = BufferForm()
    result = None
    if form.validate_on_submit():
        molecular_weight = form.molecular_weight.data
        molar_concentration = form.molar.data
        molar_concentration_unit = form.molar_unit.data
        volume = form.volume.data
        volume_unit = form.volume_unit.data
        result_mg = buffer_mass(molar_concentration, molar_concentration_unit,
                                volume, volume_unit, molecular_weight)
        result_g = result_mg / 1000
        result = {'g': result_g, 'mg': result_mg}
    return render_template(
        'cal_buffer.html', form=form, result=result,
        title='Buffer calculator')


@app.route('/broth', methods=['GET', 'POST'])
def make_broth():
    form = BrothForm()
    result = None
    # print form.errors
    # if form.is_submitted():
    #     print "submitted"
    # if form.validate():
    #     print "valid"
    # print(form.errors)
    if form.validate_on_submit():
        broth_type = int(form.broth_type.data)
        volume = float(form.volume.data)
        volume_unit = float(form.volume_unit.data)
        result = broth_mehod(broth_type, volume * volume_unit)
        # print result
    return render_template(
            'cal_broth.html', form=form, result=result,
            title='Broth calculator')


@app.route('/oligo', methods=['GET', 'POST'])
def oligo():
    form = OligoForm()
    result = None
    if form.validate_on_submit():
        dna = ''.join(form.target_seq.data.split())
        result = Oligo(dna)
    return render_template(
            'cal_oligo.html', form=form, result=result,
            title='Oligo calculator')


@app.route('/translate', methods=['GET', 'POST'])
def trans():
    form = TranslateForm()
    result = None
    if form.validate_on_submit():
        dna = ''.join(form.target_seq.data.split())
        result = Translate(dna)
    return render_template(
            'cal_translate.html',
            form=form, result=result, title='Protein Translator')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
