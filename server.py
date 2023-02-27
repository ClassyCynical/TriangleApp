from flask import Flask, jsonify, request
from werkzeug.serving import run_simple

app = Flask(__name__)
# drivers = [
#    {
#       "name":"Aidan Williams",
#       "phone":"(980) 867-1653",
#       "address":"1210 Tomko Rd."
#    },
#    {
#       "name":"Alec Boron",
#       "phone":"(240) 586-4753",
#       "address":"1626 Patrick Henry Drive Apartment 144"
#    },
#    {
#       "name":"Alex Natt",
#       "phone":"(310) 874-4782",
#       "address":"1604 Bold Springs Cir"
#    },
#    {
#       "name":"Alexander Barnes",
#       "phone":"(571) 386-9595",
#       "address":"1756 Autumn Splendor Way"
#    },
#    {
#       "name":"Andrew Shore",
#       "phone":"(908) 200-9045",
#       "address":"720 Washington St SW"
#    },
#    {
#       "name":"Andrew Bryan",
#       "phone":"(973) 525-4589",
#       "address":"1606 Patrick Henry dr apt. 111"
#    },
#    {
#       "name":"Anthony Nostro",
#       "phone":"(570) 807-6491",
#       "address":"400 Hunt Club Rd, Apt 14307"
#    },
#    {
#       "name":"Arush Amin",
#       "phone":"(703) 939-1446",
#       "address":"107 - 1 Givens Lane"
#    },
#    {
#       "name":"Austin Moore",
#       "phone":"(703) 431-6711",
#       "address":"7300 Hunters mill rd apt b&d"
#    },
#    {
#       "name":"Blake Marterella",
#       "phone":"(703) 314-3044",
#       "address":"720 Washington Street SW (West AJ Rm: 7501)"
#    },
#    {
#       "name":"Brogan O'Connell",
#       "phone":"(561) 312-5876",
#       "address":"600 Washington St SW (Payne 124)"
#    },
#    {
#       "name":"Cason Kerrick",
#       "phone":"(757) 784-7242",
#       "address":"7500 Hunters Mill Road, Apt A"
#    },
#    {
#       "name":"Chris Crews",
#       "phone":"(301) 273-5877",
#       "address":"730 Golden Harvest Circle"
#    },
#    {
#       "name":"Christian Diaz",
#       "phone":"(703) 843-0583",
#       "address":"1204 Progress St NW Unit 7900A-A"
#    },
#    {
#       "name":"Cole Curtis",
#       "phone":"(703) 200-3678",
#       "address":"West Ambler Johnston Rm 7501"
#    },
#    {
#       "name":"Cole Gala",
#       "phone":"(704) 787-3846",
#       "address":"1626 Patrick Henry Drive Apt 144"
#    },
#    {
#       "name":"Connor Czap",
#       "phone":"(610) 425-2509",
#       "address":"301 Edge Way (Apt 504)"
#    },
#    {
#       "name":"Dag Attridge",
#       "phone":"(804) 347-0214",
#       "address":"9100 Hunters Mill Rd Apt B"
#    },
#    {
#       "name":"Dan Nguyen",
#       "phone":"(571) 888-2948",
#       "address":"406 Laurence Ln"
#    },
#    {
#       "name":"David, Encarnacion",
#       "phone":"(718) 702-2808",
#       "address":"1210 Tomko Rd."
#    },
#    {
#       "name":"Dawson, Bird",
#       "phone":"(716) 679-6663",
#       "address":"185 Kent St"
#    },
#    {
#       "name":"Dominic, Hanna",
#       "phone":"(774) 245-9761",
#       "address":"800 Patrick Henry Drive"
#    },
#    {
#       "name":"Edward, Seltzner",
#       "phone":"(608) 630-3750",
#       "address":"1210 Tomko Rd."
#    },
#    {
#       "name":"Evan, Flores",
#       "phone":"(787) 677-0071",
#       "address":"700 Washington St. SW East AJ Rm 3216"
#    },
#    {
#       "name":"Garrett, Weisberg",
#       "phone":"(561) 386-5531",
#       "address":"301 Edge Way (Apt 504)"
#    },
#    {
#       "name":"Gavin, Lopez",
#       "phone":"(240) 758-1411",
#       "address":"Pritchard Hall"
#    },
#    {
#       "name":"Griffin, Strickler",
#       "phone":"(443) 994-8876",
#       "address":"630 Washington St. SW"
#    },
#    {
#       "name":"Gus, von Reis",
#       "phone":"(858) 366-3483",
#       "address":"9100 Hunters Mill Rd Apt B"
#    },
#    {
#       "name":"Ilan, Litvak",
#       "phone":"(516) 727-2426",
#       "address":"Pritchard Hall 4096"
#    },
#    {
#       "name":"Jake, Horowitz",
#       "phone":"(908) 642-6338",
#       "address":"1907 Gardenspring Dr"
#    },
#    {
#       "name":"James, McKinley",
#       "phone":"(703) 364-9440",
#       "address":"601 Giles Rd."
#    },
#    {
#       "name":"Joseph, Kozianowski",
#       "phone":"(856) 266-5507",
#       "address":"11600 Foxtrail Lane Apt. I"
#    },
#    {
#       "name":"Joseph, McCabe",
#       "phone":"(508) 212-9826",
#       "address":"720 Washington St SW Rm 4105"
#    },
#    {
#       "name":"Josh, Klein",
#       "phone":"(571) 209-8386",
#       "address":"630 Washington St SW"
#    },
#    {
#       "name":"Judson, Murray",
#       "phone":"(615) 969-1015",
#       "address":"217 pheasant run Dr"
#    },
#    {
#       "name":"Kareem, Badr",
#       "phone":"(202) 412-9494",
#       "address":"400 Hunt Club road, Apt 14307"
#    },
#    {
#       "name":"Kenny, Williams",
#       "phone":"(757) 266-3060",
#       "address":"507 Golden Harvest Circle"
#    },
#    {
#       "name":"Lucas, Aparicio",
#       "phone":"(703) 401-8455",
#       "address":"240 West Campus Dr., Harper Hall, Room 3041"
#    },
#    {
#       "name":"Luke, Marks",
#       "phone":"(571) 364-4945",
#       "address":"9300 Hunters Mill Rd, Apt L"
#    },
#    {
#       "name":"Matt, Polanka",
#       "phone":"(937) 818-0243",
#       "address":"217 Pheasant Run Dr"
#    },
#    {
#       "name":"Matthew, Feldman",
#       "phone":"(704) 995-0503",
#       "address":"1200 Snyder Ln"
#    },
#    {
#       "name":"Matthew, Thompsen",
#       "phone":"(609) 577-6120",
#       "address":"506 Sunridge Dr"
#    },
#    {
#       "name":"Nate, Scollar",
#       "phone":"(443) 718-1146",
#       "address":"800 Patrick Henry Drive"
#    },
#    {
#       "name":"Nicholas, Meier",
#       "phone":"(609) 658-7928",
#       "address":"506 Sunridge Drive, Room 102 D"
#    },
#    {
#       "name":"Nick, Kochanski",
#       "phone":"(804) 840-3346",
#       "address":"200 Kent St"
#    },
#    {
#       "name":"Patrik, Kaufman",
#       "phone":"(224) 216-9347",
#       "address":"107 - 1 Givens Lane"
#    },
#    {
#       "name":"Pierce, Meissner",
#       "phone":"(919) 270-6056",
#       "address":"570 Washington St. SW"
#    },
#    {
#       "name":"Reginald, Nolan",
#       "phone":"(757) 751-7502",
#       "address":"2510 Ridge Rd."
#    },
#    {
#       "name":"Roggen, King",
#       "phone":"(610) 390-0280",
#       "address":"301 Edge Way (Apt 504)"
#    },
#    {
#       "name":"Ryan, Trcka",
#       "phone":"(719) 439-2210",
#       "address":"310 Pheasant Run Court"
#    },
#    {
#       "name":"Ryan, Walker",
#       "phone":"(443) 905-6810",
#       "address":"1200 Snyder Lane, Apt. 14307"
#    },
#    {
#       "name":"Suvasish, Pant",
#       "phone":"(571) 358-9914",
#       "address":"1826 Grayland St APT #5"
#    },
#    {
#       "name":"Tushar, Gayali",
#       "phone":"(804) 387-8973",
#       "address":"1626 Patrick Henry Drive Apt 143"
#    },
#    {
#       "name":"Tyler, Bryceland",
#       "phone":"(845) 608-2834",
#       "address":"1606 Patrick Henry dr apt.111"
#    },
#    {
#       "name":"Vincent, Basso",
#       "phone":"(804) 822-2323",
#       "address":"7300 Hunters Mill Rd Apt. B/D"
#    },
#    {
#       "name":"Prokesch, Youri",
#       "phone":"(412) 709-3181",
#       "address":"107 - 1 Givens Lane"
#    },
#    {
#       "name":"Weiss, Zach",
#       "phone":"(804) 525-0215",
#       "address":"1003 S Main St"
#    }
# ]

drivers = [
        {
        "id": 1,
        "name":"Aidan Williams",
        "phone":"(980) 867-1653",
        "address":"1210 Tomko Rd."
    },
    {
        "id": 2,
        "name":"Alec Boron",
        "phone":"(240) 586-4753",
        "address":"1626 Patrick Henry Drive Apartment 144"
    },
]

@app.route('/drivers', methods=['GET'])
def get_drivers():
    sorted_drivers = sorted(drivers, key=lambda k: k['name'])
    drivers_formatted = [{'Name': driver['name'], 'Address': driver['address'], 'Phone Number': driver['phone']} for driver in sorted_drivers]
    return jsonify(drivers_formatted)

@app.route('/drivers', methods=['POST'])
def add_driver():
    driver = request.get_json()
    drivers.append(driver)
    return '', 204

@app.route('/drivers/<int:driver_id>', methods=['DELETE'])
def remove_driver(driver_id):
    if driver_id >= len(drivers):
        return 'Driver not found', 404
    drivers.pop(driver_id)
    return '', 204

@app.route('/drivers/<int:driver_id>', methods=['PUT'])
def update_driver(driver_id):
    if driver_id >= len(drivers):
        return 'Driver not found', 404
    driver = request.get_json()
    drivers[driver_id].update(driver)
    return '', 204

if __name__ == '__main__':
    run_simple('localhost', 8000, app, use_reloader=True, use_debugger=True)
