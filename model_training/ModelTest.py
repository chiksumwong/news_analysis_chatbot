import pickle

var = input("Please enter the news text you want to verify: ")
print("\nYou entered:\n" + str(var) +'\n')


#function to run for prediction
def detecting_fake_news(var):    
#retrieving the best model for prediction call
    load_model = pickle.load(open('model_training/model.sav', 'rb'))
    prediction = load_model.predict([var])
    prob = load_model.predict_proba([var])

    return (print("The given statement is ",prediction[0]),
        print("The fake news probability score is ",prob[0][0]))


if __name__ == '__main__':
    detecting_fake_news(var)
    