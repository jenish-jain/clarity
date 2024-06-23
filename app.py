from flask import Flask, render_template, request
import pandas as pd

transactions = pd.read_json("/Users/jenishjain/Desktop/workspace/tryouts/output.json")
transactions['time'] = pd.to_datetime(transactions['time'], format='%d-%m-%Y')
app = Flask(__name__)

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/table')
def table():
    monthYear = request.args.get('monthYear')
    if monthYear:
        year, month = map(int, monthYear.split('-'))
        filtered_transactions = transactions[(transactions['time'].dt.year == year) & (transactions['time'].dt.month == month)]
        transactions_list = filtered_transactions.to_dict('records')
    else:
        transactions_list = transactions.to_dict('records')
    
    return render_template('table.html', results=transactions_list, selectedMonthYear=monthYear)

if __name__ == '__main__':
    app.run(debug=True)