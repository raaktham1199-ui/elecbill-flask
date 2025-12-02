from flask import Flask,render_template,request
import numpy as np
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("fontweb.html")

@app.route('/mont1',methods=['POST','GET'])
def mont1(): 
    if request.method == "POST":
       
       fields = ["wat", "unit", "month", "hours"]
       for f in fields:
            if not request.form.get(f):   # ว่าง = True
                return render_template("mont1.html", resulthtml="Please fill in all fields.")

       wat=float(request.form.get("wat"))
       unit=float(request.form.get("unit"))
       new_wat=wat/1000
       mont=int(request.form.get("month"))
       hours=int(request.form.get("hours"))
       if mont==1 or mont==3 or mont==5 or mont==7 or mont==8 or mont==10 or mont==12:
          result=new_wat*hours*unit*31
       elif mont==4 or mont==6 or mont==9 or mont==11:
          result=new_wat*hours*unit*30
       else:
          result=new_wat*hours*unit*28        
       return render_template("mont1.html",resulthtml=result)
    
    return render_template("mont1.html")


@app.route('/mont2',methods=['POST','GET'])
def mont2():
    if request.method == "POST":

        fields = ["wat","1","2","3","4","5","6","7","unit","month"]
        for f in fields:
            if not request.form.get(f): 
                return render_template("mont2.html",weekhtml="Please fill in all fields.",monthtml="Please fill in all fields.")

        wat=float(request.form.get("wat"))
        new_wat=wat/1000
        monday=int(request.form.get("1"))
        tuesday=int(request.form.get("2"))
        wednesday=int(request.form.get("3"))
        thursday=int(request.form.get("4"))
        friday=int(request.form.get("5"))
        saturday=int(request.form.get("6"))
        sunday=int(request.form.get("7"))
        unit=float(request.form.get("unit"))
        mont=int(request.form.get("month"))
        all_data_monday=[monday,tuesday,wednesday,thursday,friday,saturday,sunday]
        all_data_tuesday=[tuesday,wednesday,thursday,friday,saturday,sunday,monday]
        all_data_wednesday=[wednesday,thursday,friday,saturday,sunday,monday,tuesday]
        all_data_thursday=[thursday,friday,saturday,sunday,monday,tuesday,wednesday]
        all_data_friday=[friday,saturday,sunday,monday,tuesday,wednesday,thursday]
        all_data_saturday=[saturday,sunday,monday,tuesday,wednesday,thursday,friday]
        all_data_sunday=[sunday,monday,tuesday,wednesday,thursday,friday,saturday]
        zero=np.zeros((5,7))
        if mont==1 or mont==10:
            for i in range(5):
                for j in range(7):
                    if i == 4 and j in [3, 4, 5, 6]:
                        zero[i,j]=0
                    else:
                        zero[i,j]=all_data_wednesday[j]
        elif mont==2:
            for i in range(5):
                for j in range(7):
                    if i == 4 and j in [0, 1, 2, 3, 4, 5, 6]:
                        zero[i,j]=0
                    else:
                        zero[i,j]=all_data_saturday[j]
        elif mont==3:
            for i in range(5):
                for j in range(7):
                    if i == 4 and j in [3, 4, 5, 6]:
                        zero[i,j]=0
                    else:
                        zero[i,j]=all_data_saturday[j]
        elif mont==4:
            for i in range(5):
                for j in range(7):
                    if i == 4 and j in [2, 3, 4, 5, 6]:
                        zero[i,j]=0
                    else:
                        zero[i,j]=all_data_tuesday[j]
        elif mont==5:
            for i in range(5):
                for j in range(7):
                    if i == 4 and j in [3, 4, 5, 6]:
                        zero[i,j]=0
                    else:
                        zero[i,j]=all_data_thursday[j]
        elif mont==6:
            for i in range(5):
                for j in range(7):
                    if i == 4 and j in [2, 3, 4, 5, 6]:
                        zero[i,j]=0
                    else:
                        zero[i,j]=all_data_sunday[j]
        elif mont==7:
            for i in range(5):
                for j in range(7):
                    if i == 4 and j in [3, 4, 5, 6]:
                        zero[i,j]=0
                    else:
                        zero[i,j]=all_data_tuesday[j]
        elif mont==8:
            for i in range(5):
                for j in range(7):
                    if i == 4 and j in [3, 4, 5, 6]:
                        zero[i,j]=0
                    else:
                        zero[i,j]=all_data_friday[j]
        elif mont==9:
            for i in range(5):
                for j in range(7):
                    if i == 4 and j in [2, 3, 4, 5, 6]:
                        zero[i,j]=0
                    else:
                        zero[i,j]=all_data_monday[j]
        elif mont==11:
            for i in range(5):
                for j in range(7):
                    if i == 4 and j in [2, 3, 4, 5, 6]:
                        zero[i,j]=0
                    else:
                        zero[i,j]=all_data_saturday[j]
        elif mont==12:
            for i in range(5):
                for j in range(7):
                    if i == 4 and j in [3 , 4, 5, 6]:
                        zero[i,j]=0
                    else:
                        zero[i,j]=all_data_monday[j]
        totalmont=np.sum(zero)
        totalweek=np.sum(all_data_monday)
        resultmont=new_wat*totalmont*unit
        resultweek=new_wat*totalweek*unit
        return render_template("mont2.html",monthtml=resultmont,weekhtml=resultweek)
    return render_template("mont2.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)