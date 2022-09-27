import keras
import datetime
from datetime import date, timedelta
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import csv
import time
import math

class Neural_net:
    def __init__(self, input_size, topology, output_size) -> None:
        self.topology = topology
        self.input_size = input_size
        self.output_size = output_size

        self.model = keras.Sequential()
        for i, size in enumerate(topology):
            if i == 0:
                #first layer and second layer
                act = 'relu'
                self.model.add(keras.layers.Dense(units = topology[i], activation = 'linear', input_shape=[input_size]))
                self.model.add(keras.layers.Dense(units = topology[i], activation = act)) #, kernel_initializer = keras.initializers.GlorotUniform()))
            elif i > 0 and i < len(topology)-1:
                #core layers
                self.model.add(keras.layers.Dense(units = topology[i], activation = act))
            else:
                #last layer
                self.model.add(keras.layers.Dense(units = output_size, activation = 'linear'))

            opt = tf.keras.optimizers.SGD(lr=0.00001, momentum=0.9, clipnorm=0.5)
            self.model.compile(loss='mape', optimizer=opt, metrics=['mape'])
            #loss='mse' tf.keras.metrics.MeanAbsolutePercentageError()
            #keras.metrics.RootMeanSquaredError()
    
        self.model.summary()
                
    def load_data(self, data_file, test_size):
        #input vector
        with open(data_file) as input:
            file = csv.reader(input, delimiter=',')
            self.input_data = []
            for row in file:
                input_data_row = []
                for i in range(self.input_size):
                    input_data_row.append(float(row[i]))
                self.input_data.append(input_data_row)
        #output vector
        with open(data_file) as output:
            file = csv.reader(output, delimiter=',')
            self.output_data = []
            for row in file:
                output_data_row = []
                for i in range(self.input_size, self.input_size + self.output_size):
                    output_data_row.append(float(row[i]))
                self.output_data.append(output_data_row)

        self.input_data_train, self.output_data_train= self.input_data, self.output_data      
        self.input_data_train, self.output_data_train = shuffle(self.input_data_train, self.output_data_train)
        #self.input_data_test = shuffle(self.input_data_test)

        #self.output_data_test = shuffle(self.output_data_test)



    def train_model(self, epochs, error_limit = None, savefig_name = None):
        # Training

        if error_limit is not None:
            callback=my_treshold_callback(threshold=error_limit)
            self.history = self.model.fit(self.input_data_train, self.output_data_train, epochs=epochs, verbose=2, callbacks=[callback], batch_size=16)
        else:
            self.history = self.model.fit(self.input_data_train, self.output_data_train, epochs=epochs, verbose=2, batch_size=16)

        #plot training
        plt.plot(self.history.history['mape']) #'mape'
        plt.xlabel('Epochs')
        plt.ylabel('Mean Absolute Percentage Error [%]')
        #plt.ylim((10**0,40))
        plt.yscale('log')
        plt.grid()
        if savefig_name is not None:
            plt.savefig(savefig_name + str(self.topology) + '.jpg')
        else:
            plt.show()

    def predict(self, custom_data):
        # if custom_data is None:
        #     return self.model.predict(self.input_data_test)
        # else:
        return self.model.predict(custom_data)

    def load_model(self, filename):
        self.model = keras.models.load_model(filename)
        print(f'Loaded model {filename}')

    def save_model(self, filename):
        model_name = filename + '_'+ str(self.input_size) + str(self.topology) + str(self.output_size)
        self.model.save(model_name)
        print(f'Saved model as {model_name}')

def predict_relative():

    BOX_SIZE = 30

    ticker = 'ES=F'
    period1 = int(time.mktime(datetime.datetime(2000, 12, 1, 23, 59).timetuple()))
    period2 = int(time.mktime((date.today() - timedelta(days=1)).timetuple()))   #!!!!!!!!
    interval = '1d' # 1d, 1m

    query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'

    df = pd.read_csv(query_string)
    print(df)

    input_vector = []
    test_vector = []

    price = df['Close'].iloc[-2]

    for i in range(BOX_SIZE - 1):
        val = df['Close'].iloc[0 - BOX_SIZE + i] / price
        test_vector.append([df['Close'].iloc[0 - BOX_SIZE + i]])
        if math.isnan(val):
            val = df['Close'].iloc[0 - BOX_SIZE + (i-1)] / price
        if math.isnan(val):
            val = df['Close'].iloc[0 - BOX_SIZE + (i-2)] / price
        input_vector.append([val])

    # print("input vector: ", input_vector)
    # print("test vector: ", test_vector)
    # print("base value: ", price)

    nn = Neural_net(29, (64, 128, 128, 64), 1)
    nn.load_model('neural_net/BOX_30_scale_29(64, 128, 128, 64)1')

    output_vector = nn.predict(np.transpose(input_vector))

    print("input: ", input_vector)
    print("output: ", output_vector)

    print("Yesterday relative predicted: ", round((output_vector[0][0] - 1) * 100, 5), " %")
    print("Yesterday relative real: ", round((df['Close'].iloc[-1] / price - 1) * 100, 5), " %")


    print("yesterday: ", date.today() - timedelta(days=1))

    f = open('neural_net/predictions_relative.csv', 'a', newline='')
    writer = csv.writer(f)

    row = []

    yesterday = date.today() - timedelta(days=1)
    yesterday.strftime('%d%m%y')

    row.append(yesterday)
    row.append(round((output_vector[0][0] - 1) * 100, 5))
    row.append(round((df['Close'].iloc[-1] / price - 1) * 100, 5))

    writer.writerow(row)

    f.close()


if __name__ == '__main__':
    predict_relative()