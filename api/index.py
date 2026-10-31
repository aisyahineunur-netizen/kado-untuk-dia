from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    pesan_error = None
    akses_diberikan = False
    nama = ""

    if request.method == 'POST':
        nama = request.form.get('nama', '').strip()
        tgl_jadian = request.form.get('tgl_jadian','').strip()
        makanan_fav = request.form.get('makanan_fav', '').lower().strip()

        if tgl_jadian == "04-09" and "ayam geprek" in makanan_fav:
            akses_diberikan = True
        else:
            pesan_error = "ACCESS DENIED! Jawaban kamu masih ada yang salah. Ingat-ingat ya 😡"

    return render_template('index.html', error=pesan_error, sukses=akses_diberikan)
    
app = app

if __name__== '__main__':
    app.run(debug=True)
