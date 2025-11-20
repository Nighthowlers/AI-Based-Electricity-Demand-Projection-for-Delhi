from django.shortcuts import render
from django.db import connection
import numpy as np
from joblib import load

lstm_model = load('./savedModels/models.joblib')

# def Predictor(request):
#     return render(request, 'main.html')

def Predictor(request):
    return render(request, "Predictor.html")

def formInfo(request):
    if request.method == 'POST':
        fetch_data = int(request.POST.get('region'))
        l = fetch_data

        # Save data to SQLite database
        cursor = connection.cursor()
        
        cursor.execute("""
            SELECT *
            FROM factors_dataset
            WHERE Region = %s
            ORDER BY RANDOM()
            LIMIT 1
        """, [l])

        

        results = cursor.fetchall()

        # Convert the results to a list of lists
        data_list = [list(row) for row in results]

        # print(data_list)

        connection.close()
        
        list1 = []

        for i in range(1,25,3):
            data_list[0][9] = i
            new_data = np.array(data_list)
            new_data = new_data.reshape((1, 1, new_data.shape[1]))  # (1 sample, 1 time step, 12 features)

            predicted_power_load = lstm_model.predict(new_data)

            list1.append(predicted_power_load)
        # print(list1)

        single_list = [item[0][0] for item in list1]

        # print(single_list)


        # Return the predicted value as a dictionary
        return render(request, 'Predictor.html', {'result':single_list})
    #predicted_power_load[0][0]

    return render(request, 'Predictor.html', {'Predictor': 'Please submit the form to get the result'})