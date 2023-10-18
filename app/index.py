from flask import Blueprint, render_template

index_blueprint = Blueprint('index', __name__)
@index_blueprint.route("/")
def index():
    nama = 'Dr. Hendra, S.Si., M.Kom'
    nip = '197601022002121001'
    mk = ['pemrograman web','pemrograman web lanjutan','jaringan komputer','pengantar sistem informasi']
    return render_template('index.html', znama=nama, znip=nip, zmk = mk)
