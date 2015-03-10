# -*- coding: utf-8 -*-
from flask import render_template
from app import app


@app.route('/')

def index():
	texts = {'title':'Tanie Dedykowane Serwery VPS w Chmurze - skyhost.com.pl','promo_text':'Proste i Wydajne Serwery VPS dla Twoich stron.'}
	return render_template('index.html', texts = texts)

@app.route('/vps')

def vps():

	tariffs = [
				{'name': 'HDD VPS 1x',
				 'price': '27',
				 'ram': '512',
				 'cpu': '1x Intel Xeon 3,7 Ghz (1 rdzeń)',
				 'hdd': '25',
				 'traffic': '40'
				},
				{'name': 'HDD VPS 2x',
				 'price': '52',
				 'ram': '1024',
				 'cpu': '2x Intel Xeon 3,7 Ghz (2 rdzeń)',
				 'hdd': '50',
				 'traffic': '80'
				},
				{'name': 'HDD VPS 3x',
				 'price': '65',
				 'ram': '1548',
				 'cpu': '3x Intel Xeon 3,7 Ghz (3 rdzeń)',
				 'hdd': '75',
				 'traffic': '100'
				},
				{'name': 'HDD VPS 4x',
				 'price': '85',
				 'ram': '2048',
				 'cpu': '4x Intel Xeon 3,7 Ghz (4 rdzeń)',
				 'hdd': '120',
				 'traffic': '100'
				}
	]

	texts = {'title':'Tanie Dedykowane Serwery VPS w Chmurze - skyhost.com.pl','promo_text':'Proste i Wydajne Serwery VPS dla Twoich stron.'}

	return render_template('vps.html', tariffs = tariffs , texts=texts)

@app.route('/login', methods=['GET', 'POST'])
def login():
	pass
	# error = None
	# if request.method == 'POST':





