from model import ModelRegression
from flask import Flask, request, render_template, url_for
app = Flask(__name__)


@app.route('/')
def home():
    neighbourhood_cleansed = ['Ang Mo Kio', 'Bedok', 'Bishan', 'Bukit Batok', 'Bukit Merah', 'Bukit Panjang', 
                            'Bukit Timah', 'Central Water Catchment', 'Changi', 'Choa Chu Kang', 'Clementi', 
                            'Downtown Core', 'Geylang', 'Hougang','Jurong East', 'Jurong West', 'Kallang', 
                            'Lim Chu Kang', 'Mandai', 'Marina South', 'Marine Parade', 'Museum', 'Newton', 'Novena', 
                            'Orchard', 'Outram', 'Pasir Ris', 'Punggol', 'Queenstown', 'River Valley', 'Rochor', 
                            'Sembawang', 'Sengkang', 'Serangoon', 'Singapore River', 'Southern Islands', 'Sungei Kadut', 
                            'Tampines', 'Tanglin', 'Toa Payoh', 'Western Water Catchment', 'Woodlands', 'Yishun']

    room_type = ['Entire home/apt', 'Hotel room',
                 'Private room', 'Shared room']

    property_type = ['Boat', 'Campsite', 'Entire apartment', 'Entire chalet', 'Entire condominium', 
                        'Entire condominium (condo)', 'Entire guest suite', 'Entire house', 'Entire loft', 
                        'Entire place', 'Entire rental unit', 'Entire residential home', 'Entire serviced apartment', 
                        'Entire townhouse', 'Entire villa', 'Private room', 'Private room in apartment', 
                        'Private room in bed and breakfast', 'Private room in bungalow', 'Private room in condominium', 
                        'Private room in condominium (condo)', 'Private room in earth house', 'Private room in guest suite', 
                        'Private room in guesthouse', 'Private room in hostel', 'Private room in house', 
                        'Private room in lighthouse', 'Private room in loft', 'Private room in rental unit', 
                        'Private room in residential home', 'Private room in serviced apartment', 'Private room in tent', 
                        'Private room in townhouse', 'Private room in villa', 'Room in aparthotel', 'Room in apartment', 
                        'Room in bed and breakfast', 'Room in boutique hotel', 'Room in heritage hotel', 'Room in hostel', 
                        'Room in hotel', 'Room in serviced apartment', 'Shared room', 'Shared room in apartment', 
                        'Shared room in bed and breakfast', 'Shared room in boutique hotel', 'Shared room in bungalow', 
                        'Shared room in condominium', 'Shared room in earth house', 'Shared room in guesthouse', 
                        'Shared room in hostel', 'Shared room in house', 'Shared room in loft', 'Shared room in rental unit', 
                        'Shared room in townhouse', 'Tent', 'Tiny house']

    amenities = ['Lock on bedroom door', 'Gym', 'TV', 'Pool', 'Keypad', 'Crib', 'Free street parking', 'Hair dryer', 'Smoke alarm', 
                    'Pack \\u2019n Play/travel crib', 'Patio or balcony', 'Carbon monoxide alarm', 'Luggage dropoff allowed', 
                    'Indoor fireplace', 'Elevator', 'High chair', 'BBQ grill', 'Fire extinguisher', 'Bathtub', 
                    'Paid parking off premises', 'Cable TV','Kitchen', 'Baby bath','Shower gel','Hot tub',
                    'Free parking on premises','Shampoo','Dining table', 'Dryer', 'Cleaning before checkout',
                    'First aid kit','Cooking basics','Garden or backyard', 'Iron', 'Refrigerator', 'Long term stays allowed', 
                    'Hot water kettle', 'Microwave', 'Outdoor furniture', 'Hot water', 'Single level home', 'Toaster', 
                    'Clothing storage','Heating','Dishes and silverware', 'Wine glasses','Rice maker',
                    'Air conditioning','Private living room', 'Babysitter recommendations','Backyard','Stove', 
                    'Pocket wifi', 'Dedicated workspace', 'Window guards', 'Breakfast', 'Ethernet connection', 'Conditioner', 
                    'Paid parking on premises', 'Freezer', ' linens', 'Bed linens', 'Essentials', 'Portable fans', 
                    'Body soap', 'Oven', 'Safe', 'Sauna', 'Coffee maker', 'TV with standard cable', 'Building staff', 
                    'Bidet', 'Lake access', 'Host greets you', 'Hangers', 'Room-darkening shades', 'Record player', 
                    'Private patio or balcony', 'Baby monitor', 'Clothing storage: dresser', 'Lockbox', 'Piano', 
                    'Shared outdoor olympic-sized lap pool', 'Game console', 'Baking sheet', 'Keurig coffee machine', 
                    'Cleaning products', 'Shared outdoor lap pool', 'Bikes', 'Samsung refrigerator']
    neighbourhood_cleansedLen = len(neighbourhood_cleansed)
    room_typeLen = len(room_type)
    property_typeLen = len(property_type)
    amenitiesLen = len(amenities)
    # return str(ModelRegression.Regression([6, 2, 2, 1, 1, 1, 18, 91, 80, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0]))

    return render_template('index.html', neighbourhood_cleansed=neighbourhood_cleansed, room_type=room_type, property_type=property_type, amenities=amenities, amenitiesLen=amenitiesLen, room_typeLen=room_typeLen, property_typeLen=property_typeLen , neighbourhood_cleansedLen=neighbourhood_cleansedLen)


@app.route('/regression', methods=['POST'])
def regression():
    amenities = ['Lock on bedroom door', 'Gym', 'TV', 'Pool', 'Keypad', 'Crib', 'Free street parking', 'Hair dryer', 'Smoke alarm', 
                    'Pack \\u2019n Play/travel crib', 'Patio or balcony', 'Carbon monoxide alarm', 'Luggage dropoff allowed', 
                    'Indoor fireplace', 'Elevator', 'High chair', 'BBQ grill', 'Fire extinguisher', 'Bathtub', 
                    'Paid parking off premises', 'Cable TV','Kitchen', 'Baby bath','Shower gel','Hot tub',
                    'Free parking on premises','Shampoo','Dining table', 'Dryer', 'Cleaning before checkout',
                    'First aid kit','Cooking basics','Garden or backyard', 'Iron', 'Refrigerator', 'Long term stays allowed', 
                    'Hot water kettle', 'Microwave', 'Outdoor furniture', 'Hot water', 'Single level home', 'Toaster', 
                    'Clothing storage','Heating','Dishes and silverware', 'Wine glasses','Rice maker',
                    'Air conditioning','Private living room', 'Babysitter recommendations','Backyard','Stove', 
                    'Pocket wifi', 'Dedicated workspace', 'Window guards', 'Breakfast', 'Ethernet connection', 'Conditioner', 
                    'Paid parking on premises', 'Freezer', ' linens', 'Bed linens', 'Essentials', 'Portable fans', 
                    'Body soap', 'Oven', 'Safe', 'Sauna', 'Coffee maker', 'TV with standard cable', 'Building staff', 
                    'Bidet', 'Lake access', 'Host greets you', 'Hangers', 'Room-darkening shades', 'Record player', 
                    'Private patio or balcony', 'Baby monitor', 'Clothing storage: dresser', 'Lockbox', 'Piano', 
                    'Shared outdoor olympic-sized lap pool', 'Game console', 'Baking sheet', 'Keurig coffee machine', 
                    'Cleaning products', 'Shared outdoor lap pool', 'Bikes', 'Samsung refrigerator']
    paramList = []
    paramList.append(request.form['neighbourhood_cleansed'])
    paramList.append(request.form['room_type'])
    paramList.append(request.form['property_type'])
    paramList.append(request.form['accomodates'])
    paramList.append(request.form['bathrooms_text'])
    paramList.append(request.form['bedrooms'])
    paramList.append(request.form['beds'])
    paramList.append(request.form['number_of_reviews'])
    paramList.append(request.form['review_scores_rating'])

    for items in amenities:
        try:
            if request.form[items] == "1":
                paramList.append(1)
            else:
                paramList.append(0)
        except:
            print(items)
            paramList.append(0)

    result = ModelRegression.Regression(paramList)

    return render_template('result.html', svr=result['Super Vector Regression'])