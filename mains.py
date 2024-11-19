from flask import Flask,render_template,request

from utils import DiebeticOrNot

app = Flask(__name__)

@app.route('/')

def hello_flask():
    
    print('Diebetes Prediction...')
    
    return render_template('index.html')

@app.route('/predict_diebetic',methods = ['GET','POST'])

def diebetic_info():
    
    if request.method == 'GET':
        
        print('In GET Method...')
        
        data = request.form
        
        Glucose = eval(data['Glucose'])
        BloodPressure = eval(data['BloodPressure'])
        SkinThickness = eval(data['SkinThickness'])
        Insulin = eval(data['Insulin'])
        BMI = eval(data['BMI'])
        DiabetesPedigreeFunction = eval(data['DiabetesPedigreeFUnction'])
        Age = eval(data['Age'])
        
        diebetic = DiebeticOrNot(Glucose,BloodPressure,SkinThickness,Insulin,BMI,
                 DiabetesPedigreeFunction,Age)
        
        yes_no = diebetic.get_predicted_diebetes()
        
        if yes_no == 1 :
            
            yes_no = "Patient is Diebetic..."
            
        else :
            
            yes_no = "Patient is Not Diebetic..."
            
print('__name__ :',__name__)

if __name__ == '__main__':
    
    app.run() 