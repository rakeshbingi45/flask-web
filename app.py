from flask import Flask, render_template

app = Flask( __name__)

Electronics = [
  {
    'id' : '1',
    'name' : 'Swift',
    'price' : '100000',
  },
  {
    'id' : '2',
    'name' : 'Dell Pro',
    'price' : '120000',
  },
  {
    'id' : '3',
    'name' : 'HP Victus',
    'price' : '130000',
  }
]

@app.route('/')
def Hello_World():
  return render_template('home.html',laptops=Electronics)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)