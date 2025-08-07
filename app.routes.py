# app/routes.py
from flask import Blueprint, render_template, request, redirect, url_for, session

app = Blueprint('routes', __name__)

# Full list of supported protocols and expected auth code lengths
PROTOCOLS = {
    "POS Terminal -101.1 (4-digit approval)": 4,
    "POS Terminal -101.4 (6-digit approval)": 6,
    "POS Terminal -101.6 (Pre-authorization)": 6,
    "POS Terminal -101.7 (4-digit approval)": 4,
    "POS Terminal -101.8 (PIN-LESS transaction)": 4,
    "POS Terminal -201.1 (6-digit approval)": 6,
    "POS Terminal -201.3 (6-digit approval)": 6,
    "POS Terminal -201.5 (6-digit approval)": 6
}

@app.route('/')
def index():
    return redirect(url_for('routes.login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'admin123':
            session['user'] = username
            return redirect(url_for('routes.select_protocol'))
        else:
            error = "Invalid credentials."
    return render_template('login.html', error=error)

@app.route('/protocol', methods=['GET', 'POST'])
def select_protocol():
    if request.method == 'POST':
        selected_protocol = request.form['protocol']
        session['protocol'] = selected_protocol
        session['authcode_length'] = PROTOCOLS.get(selected_protocol, 4)
        return redirect(url_for('routes.enter_amount'))
    return render_template('protocol.html', protocols=PROTOCOLS)

@app.route('/amount', methods=['GET', 'POST'])
def enter_amount():
    if request.method == 'POST':
        session['amount'] = request.form['amount']
        session['currency'] = request.form['currency']
        session['wallet_info'] = request.form.get('wallet_info', 'Not Set')
        return redirect(url_for('routes.enter_auth'))
    return render_template('amount.html')

@app.route('/auth', methods=['GET', 'POST'])
def enter_auth():
    authcode_length = session.get('authcode_length', 4)
    if request.method == 'POST':
        entered_code = request.form['authcode']
        if len(entered_code) != authcode_length:
            error = f"Auth code must be {authcode_length} digits."
            return render_template('auth.html', error=error, expected_length=authcode_length)
        session['authcode'] = entered_code
        return redirect(url_for('routes.success'))
    return render_template('auth.html', expected_length=authcode_length)

@app.route('/success')
def success():
    return render_template('success.html',
        protocol=session.get('protocol'),
        amount=session.get('amount'),
        currency=session.get('currency'),
        authcode=session.get('authcode'),
        wallet=session.get('wallet_info', 'Not Available')
    )
