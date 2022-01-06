class ModelRegression:
    def report(df):
        col = []
        d_type = []
        uniques = []
        n_uniques = []

        for i in df.columns:
            col.append(i)
            d_type.append(df[i].dtypes)
            uniques.append(df[i].unique()[:5])
            n_uniques.append(df[i].nunique())

        return pd.DataFrame({'Column': col, 'd_type': d_type, 'unique_sample': uniques, 'n_uniques': n_uniques})

    def Regression(params):
        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt
        import seaborn as sns

        import scipy.stats as st
        from sklearn.linear_model import LinearRegression
        from sklearn.metrics import mean_squared_error
        from sklearn.preprocessing import LabelEncoder
        # pd.set_option('display.max_rows', None)

        air_sing_url = 'https://raw.githubusercontent.com/hansrichard2000/DatasetML/main/listings.csv'
        listing_df = pd.read_csv(air_sing_url)

        air_sing2_url = 'https://raw.githubusercontent.com/hansrichard2000/DatasetML/main/listingSingapore2.csv'
        listing2_df = pd.read_csv(air_sing2_url)

        airbnb_df = pd.concat([listing_df, listing2_df], axis=0)
        airbnb_df = airbnb_df.drop_duplicates(subset = ["id"])

        airbnb_df2 = airbnb_df[['id', 'neighbourhood_cleansed', 'property_type', 'room_type', 'accommodates','bathrooms_text', 'bedrooms', 'beds', 'amenities', 'number_of_reviews', 'review_scores_rating', 'price']]

        airbnb_df2.review_scores_rating.fillna(value= 0.0, inplace= True)
        airbnb_df2['price'] = airbnb_df2['price'].str.replace('$', '')
        airbnb_df2['price'] = pd.to_numeric(airbnb_df2['price'], errors='coerce')

        # Amenities One Hot Encoding (Manual)
        amenitiesCollectionString = []
        for arrayCollection in airbnb_df2['amenities']:
            arrays = []
            tempString = arrayCollection.replace('"', '')
            tempString = tempString.replace('[', '')
            tempString = tempString.replace(']', '')
            tempString = tempString.replace("'", '')
#     tempString = tempString.replace(" ", '')
            arrays = tempString.split(',')
            for items in arrays:
                if items != '':
                    if items not in amenitiesCollectionString:
                        amenitiesCollectionString.append(items)
        for items in range(len(amenitiesCollectionString)):
            tempString = amenitiesCollectionString[items]
            if tempString[0] == ' ':
                tempString = tempString[1:]
            amenitiesCollectionString[items] = tempString
        
        print(amenitiesCollectionString)

        amenitiesEncodingDf = pd.DataFrame()

        for items in amenitiesCollectionString:
            amenitiesEncodingList = []
            for rows in airbnb_df2['amenities']: 
                if items != '':
                    if items in rows:
                        amenitiesEncodingList.append(1)
                    else:
                        amenitiesEncodingList.append(0)
            amenitiesEncodingDf[items] = amenitiesEncodingList
        print(amenitiesEncodingDf.head(100))

        airbnb_df2.drop(['id', 'amenities'], inplace=True, axis=1)
        airbnb_df2.reset_index(drop=True, inplace=True)
        amenitiesEncodingDf.reset_index(drop=True, inplace=True)
        airbnb_df2 = pd.concat([airbnb_df2, amenitiesEncodingDf], axis = 1)
        airbnb_df2.dropna(inplace= True)

        le = LabelEncoder()
        airbnb_df2['neighbourhood_cleansed'] = le.fit_transform(airbnb_df2['neighbourhood_cleansed'])
        airbnb_df2['property_type'] = le.fit_transform(airbnb_df2['property_type'])
        airbnb_df2['room_type'] = le.fit_transform(airbnb_df2['room_type'])

        #Bathrooms Text Encode
        airbnb_df2['bathrooms_text'] = airbnb_df2['bathrooms_text'].str.split(' ').str[0]
        airbnb_df2['bathrooms_text'] = airbnb_df2['bathrooms_text'].str.replace('Shared', '0.5')
        airbnb_df2['bathrooms_text'] = airbnb_df2['bathrooms_text'].str.replace('Half-bath', '0.5')
        airbnb_df2['bathrooms_text'] = airbnb_df2['bathrooms_text'].str.replace('Private', '0.5')
        airbnb_df2.bathrooms_text.fillna(value= 0, inplace= True)
        airbnb_df2['bathrooms_text'] = pd.to_numeric(airbnb_df2['bathrooms_text'], errors='coerce')

        airbnb_df2 = airbnb_df2[airbnb_df2['price'] < 320]
        airbnb_df2 = airbnb_df2[airbnb_df2['price'] > 0]

        X, y = airbnb_df2.loc[:, ['neighbourhood_cleansed', 'room_type', 'bedrooms', 'Lock on bedroom door', 
                          'accommodates', 'property_type', 'Gym', 'TV', 'Pool', 
                          'Keypad', 'Crib', 'Free street parking', 'Hair dryer', 
                          'Smoke alarm', 'Pack \\u2019n Play/travel crib', 
                          'Patio or balcony', 'Carbon monoxide alarm', 
                          'Luggage dropoff allowed', 'Indoor fireplace', 
                          'Elevator', 'High chair', 'review_scores_rating', 
                          'BBQ grill', 'Fire extinguisher', 'Bathtub', 
                          'Paid parking off premises', 'Cable TV','Kitchen',
                          'Baby bath','Shower gel','Hot tub',
                          'Free parking on premises','Shampoo','Dining table',
                          'Dryer','Cleaning before checkout','number_of_reviews',
                          'First aid kit','Cooking basics','Garden or backyard', 
                          'Iron', 'Refrigerator', 'Long term stays allowed', 
                          'Hot water kettle', 'Microwave', 'Outdoor furniture', 
                          'Hot water', 'Single level home', 'Toaster', 
                          'Clothing storage','Heating','Dishes and silverware',
                          'Wine glasses', 'beds','Rice maker','bathrooms_text',
                          'Air conditioning','Private living room',
                          'Babysitter recommendations','Backyard','Stove', 
                          'Pocket wifi', 'Dedicated workspace', 'Window guards', 
                          'Breakfast', 'Ethernet connection', 'Conditioner', 
                          'Paid parking on premises', 'Freezer', ' linens', 
                          'Bed linens', 'Essentials', 
                          'Portable fans', 'Body soap', 'Oven', 'Safe', 'Sauna', 
                          'Coffee maker', 'TV with standard cable', 'Building staff', 
                          'Bidet', 'Lake access', 'Host greets you', 'Hangers', 'Room-darkening shades', 
                          'Record player', 'Private patio or balcony', 'Baby monitor', 'Clothing storage: dresser',
                          'Lockbox', 'Piano', 'Shared outdoor olympic-sized lap pool', 'Game console', 'Baking sheet', 
                          'Keurig coffee machine', 'Cleaning products', 'Shared outdoor lap pool', 'Bikes', 
                          'Samsung refrigerator']].values, airbnb_df2.loc[:, 'price'].values

        from sklearn.model_selection import train_test_split

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.30, random_state = 42)

        predictionResult = {'Super Vector Regression': ''}

        from sklearn.svm import SVR
        regressor = SVR(kernel='linear')
        regressor.fit(X, y)
        predictionResult['Super Vector Regression'] = regressor.predict([params])

        return predictionResult
