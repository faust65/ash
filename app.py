from flask import Flask, request, jsonify, render_template
import random

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/atk', methods=['POST'])
def atk():
    data=request.get_json()
    atk=int(data.get('atk', '0'))
    damage=10
    
    g=random.randrange(1, 101)
    
    if(g==1):
        result=f"대성공({g})"
        damage+=5
    elif(g==99 or g==100):
        result=f"대실패({g})"
        damage-=10
    elif((atk==1 and g>30) or (atk==2 and g>40) or (atk==3 and g>50) or (atk==4 and g>70) or (atk==5 and g>80)):
        result=f"실패({g})"
        damage-=5
    elif((atk==1 and g<=30) or (atk==2 and g<=40) or (atk==3 and g<=50) or (atk==4 and g<=70) or (atk==5 and g<=80)):
        result=f"보통 성공({g})"
        if((atk==1 and g<=15) or (atk==2 and g<=20) or (atk==3 and g<=25) or (atk==4 and g<=35) or (atk==5 and g<=40)):
            result=f"어려운 성공({g})"
            damage+=1
            if((atk==1 and g<=6) or (atk==2 and g<=8) or (atk==3 and g<=10) or (atk==4 and g<=14) or (atk==5 and g<=16)):
                result=f"극단적 성공({g})"
                damage+=1
        
    return jsonify({'result':result,'damage':damage})

@app.route('/min', methods=['POST'])
def min():
    data=request.get_json()
    min=int(data.get('min', '0'))
    damage=10
  
    g=random.randrange(1, 101)
    
    if(g==1):
        result=f"대성공({g})"
        damage+=5
    elif(g==99 or g==100):
        result=f"대실패({g})"
        damage-=10
    elif((atk==1 and g>30) or (atk==2 and g>40) or (atk==3 and g>50) or (atk==4 and g>70) or (atk==5 and g>80)):
        result=f"실패({g})"
        damage-=10
    elif((atk==1 and g<=30) or (atk==2 and g<=40) or (atk==3 and g<=50) or (atk==4 and g<=70) or (atk==5 and g<=80)):
        result=f"보통 성공({g})"
        damage-=5
        if((atk==1 and g<=15) or (atk==2 and g<=20) or (atk==3 and g<=25) or (atk==4 and g<=35) or (atk==5 and g<=40)):
            result=f"어려운 성공({g})"
            damage+=5
            if((atk==1 and g<=6) or (atk==2 and g<=8) or (atk==3 and g<=10) or (atk==4 and g<=14) or (atk==5 and g<=16)):
                result=f"극단적 성공({g})"
                damage+=2
        
    return jsonify({'result':result,'damage':damage})

@app.route('/run', methods=['POST'])
def run():
    data=request.get_json()
    run=int(data.get('run', '0'))
    
    g=random.randrange(1, 101)
    
    if(g==1):
        result=f"대성공({g})"
    elif(g==99 or g==100):
        result=f"대실패({g})"
    elif((atk==1 and g>30) or (atk==2 and g>40) or (atk==3 and g>50) or (atk==4 and g>70) or (atk==5 and g>80)):
        result=f"실패({g})"
    elif((atk==1 and g<=30) or (atk==2 and g<=40) or (atk==3 and g<=50) or (atk==4 and g<=70) or (atk==5 and g<=80)):
        result=f"보통 성공({g})"
        if((atk==1 and g<=15) or (atk==2 and g<=20) or (atk==3 and g<=25) or (atk==4 and g<=35) or (atk==5 and g<=40)):
            result=f"어려운 성공({g})"
            if((atk==1 and g<=6) or (atk==2 and g<=8) or (atk==3 and g<=10) or (atk==4 and g<=14) or (atk==5 and g<=16)):
                result=f"극단적 성공({g})"
        
    return jsonify({'result':result})

if __name__ == '__main__':

    app.run(debug=True)
