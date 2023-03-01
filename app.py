from flask import *
import json
import random
import datetime
from database import Visitors,Visitors_Daily

timestart = datetime.datetime.now()

app = Flask(__name__)
app.secret_key="asdasdasdasdasdsadas"

def get_vistors_count():
    visitors_count = 0
    data = Visitors.select().where(Visitors.id == "all")
    for x in data:
        visitors_count = int(x.visitors_count)
    return visitors_count

def get_vistors_daily_count():
    visitors_count = 0
    data = Visitors_Daily.select().where(Visitors_Daily.id == "daily")
    for x in data:
        visitors_count = int(x.visitors_count)
    return visitors_count

def get_vistors_time():
    time = None
    data = Visitors.select().where(Visitors.id == "all")
    for x in data:
        time = x.time
    return time

def get_vistors_daily_time():
    time = None
    data = Visitors_Daily.select().where(Visitors_Daily.id == "daily")
    for x in data:
        time = x.time
    return time

@app.route("/")
def index():
    with open("products.json","r+",encoding="UTF-8") as f:
        products = json.load(f)
        random.shuffle(products)
    product_types = list(set([product['urun'] for product in products]))
    

    last_visit = get_vistors_time().strftime("%H:%M:%S  %d-%m-%y")

    difference_time = (datetime.datetime.now() - get_vistors_daily_time())
    if difference_time.total_seconds() >= 86400:
        #print(difference_time.total_seconds())
        Visitors_Daily.update({Visitors_Daily.visitors_count: 0, Visitors_Daily.time:datetime.datetime.now() }).where(Visitors_Daily.id == "daily").execute()

    if "initial" not in session:
        session["initial"] = "1"
        Visitors.update({Visitors.visitors_count: get_vistors_count()+1, Visitors.time:datetime.datetime.now() }).where(Visitors.id == "all").execute()
        Visitors_Daily.update({Visitors_Daily.visitors_count: get_vistors_daily_count()+1 }).where(Visitors_Daily.id == "daily").execute()

    all_visitors_count =  get_vistors_count()
    daily_visitors_count = get_vistors_daily_count()

    return render_template("index.html",
                        products=products,
                        product_types=product_types,
                        all_visitors_count = all_visitors_count,
                        daily_visitors_count = daily_visitors_count,
                        last_visit = last_visit
                        )


@app.route("/remove-daily-visitors-count")
def remove_daily_count():
    Visitors_Daily.update({Visitors_Daily.visitors_count: 0 }).where(Visitors_Daily.id == "daily").execute()
    return "<h1>Günlük ziyaretçi sayısı silindi</h1>"

@app.route("/remove-all-visitors-count")
def remove_all_visitors_count():
    Visitors.update({Visitors.visitors_count: 0, Visitors.time:datetime.datetime.now() }).where(Visitors.id == "all").execute()
    return "<h1>Tüm zamanlara ait ziyaretçi sayısı silindi</h1>"

@app.route("/<x>")
def error404(x):
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)