from flask import Flask, render_template, jsonify
import json

app = Flask( __name__)

@app.route('/')
def index():
  with open('static/data/featured_products.json') as f:
    featured_products = json.load(f)
  return render_template('index.html',featured_products = featured_products)

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/categories/mobiles')
def mobiles():
    return render_template('mobiles.html')

@app.route('/categories/laptops')
def laptops():
    return render_template('laptops.html')

@app.route('/categories/audio')
def audio():
    return render_template('audio.html')

@app.route('/categories/monitors')
def monitors():
    return render_template('monitors.html')

@app.route('/categories/consoles')
def consoles():
    return render_template('consoles.html')

@app.route('/smartwatches')
def smartwatches():
    return render_template('smartwatches.html')
  
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)