import flask
from flask import request
import json
import numpy
import math

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    ret={'success': True, 'message':'This is the home page'}
    return json.dumps(ret), 200, {"Content Type":'application/json'}

@app.route('/area/square', methods=['GET'])
def area_square():
    if 's' in request.args:
        s=int(request.args['s'])
        ret={'a': s*s, 's':s}
        return json.dumps(ret), 200, {"Content Type":'application/json'}
    else:
        return(err_404(404))

#http://127.0.0.1:3001/area/rectangle?l=5&w=3
@app.route('/area/rectangle', methods=['GET'])
def area_rectangle():
    if 'l' in request.args and 'w' in request.args:
        l=int(request.args['l'])
        w=int(request.args['w'])
        ret={'a': l*w, 'l':l, 'w':w}
        return json.dumps(ret), 200, {"Content Type":'application/json'}
    else:
        return(err_404(404))

@app.route('/area/triangle', methods=['GET'])
def area_triangle():
    if 'b' in request.args and 'h' in request.args:
        b=int(request.args['b'])
        h=int(request.args['h'])
        ret={'a': b*h/2, 'b':b, 'h':h}
        return json.dumps(ret), 200, {"Content Type":'application/json'}
    else:
        return(err_404(404))

@app.route('/area/heron', methods=['GET'])
def area_heron():
    if 'x' in request.args and 'y' in request.args and 'z' in request.args:
        x=int(request.args['x'])
        y=int(request.args['y'])
        z=int(request.args['z'])
        s=x+y+z
        ret={'s':s, 'a': math.sqrt((s * (s - x) * (s - y) * s - z)), 'x':x, 'y':y, 'z':z}
        return json.dumps(ret), 200, {"Content Type":'application/json'}
    else:
        return(err_404(404))

@app.route('/area/parallelogram', methods=['GET'])
def area_parallelogram():
    if 'b' in request.args and 'h' in request.args:
        b=int(request.args['b'])
        h=int(request.args['h'])
        a=b*h/2 # This is the incorrect formula checked for by the testing
        ret={'a':a, 'b':b, 'h':h}
        return json.dumps(ret), 200, {"Content Type":'application/json'}
    else:
        return(err_404(404))

@app.route('/area/circle', methods=['GET'])
def area_circle():
    if 'r' in request.args:
        r=int(request.args['r'])
        a=math.pi*r*r
        ret={'a':a, 'r':r}
        return json.dumps(ret), 200, {"Content Type":'application/json'}
    else:
        return(err_404(404))

@app.route('/area/trapezoid', methods=['GET'])
def area_trapezoid():
    if 'b1' in request.args and 'b2' in request.args and 'h' in request.args:
        b1=int(request.args['b1'])
        b2=int(request.args['b2'])
        h=int(request.args['h'])
        a=(b1*b2)*h/2
        ret={'a':a, 'b1':b1, 'b2':b2, 'h':h}
        return json.dumps(ret), 200, {"Content Type":'application/json'}
    else:
        return(err_404(404))

@app.route('/surface/cube', methods=['GET'])
def area_surface_cube():
    if 's' in request.args:
        s=int(request.args['s'])
        sa=6*s*s
        ret={'sa':sa, 's':s}
        return json.dumps(ret), 200, {"Content Type":'application/json'}
    else:
        return(err_404(404))

@app.route('/surface/sphere', methods=['GET'])
def area_surface_sphere():
    if 'r' in request.args:
        r=int(request.args['r'])
        sa=4*math.pi*r*r
        ret={'sa':sa, 'r':r}
        return json.dumps(ret), 200, {"Content Type":'application/json'}
    else:
        return(err_404(404))

@app.route('/surface/cylinder', methods=['GET'])
def area_surface_cylinder():
    if 'r' in request.args and 'h' in request.args:
        r=int(request.args['r'])
        h=int(request.args['h'])
        sa=2*math.pi*r*h
        ret={'sa':sa, 'r':r, 'h':h}
        return json.dumps(ret), 200, {"Content Type":'application/json'}
    else:
        return(err_404(404))

@app.route('/perimeter/square', methods=['GET'])
def perimeter_square():
    if 's' in request.args:
        s=int(request.args['s'])
        p=4*s
        ret={'p':p, 's':s}
        return json.dumps(ret), 200, {"Content Type":'application/json'}
    else:
        return(err_404(404))

@app.route('/perimeter/rectangle', methods=['GET'])
def perimeter_rectangle():
    if 'l' in request.args and 'w' in request.args:
        l=int(request.args['l'])
        w=int(request.args['w'])
        p=2*l+2*w
        ret={'p':p, 'l':l, 'w': w}
        return json.dumps(ret), 200, {"Content Type":'application/json'}
    else:
        return(err_404(404))

@app.route('/perimeter/triangle', methods=['GET'])
def perimeter_triangle():
    if 's1' in request.args and 's2' in request.args and 's3' in request.args:
        s1=int(request.args['s1'])
        s2=int(request.args['s2'])
        s3=int(request.args['s3'])
        p=s1+s2+s3
        ret={'p':p, 's1':s1, 's2': s2, 's3':s3}
        return json.dumps(ret), 200, {"Content Type":'application/json'}
    else:
        return(err_404(404))

@app.route('/perimeter/circle', methods=['GET'])
def perimeter_circle():
    if 'd' in request.args:
        d=int(request.args['d'])
        c=math.pi*d
        ret={'c':c, 'd':d}
        return json.dumps(ret), 200, {"Content Type":'application/json'}
    else:
        return(err_404(404))

@app.route('/volume/cube', methods=['GET'])
def volume_cube():
    if 's' in request.args:
        s=int(request.args['s'])
        v=s*s*s
        ret={'v':v, 's':s}
        return json.dumps(ret), 200, {"Content Type":'application/json'}
    else:
        return(err_404(404))

@app.route('/volume/prism', methods=['GET'])
def volume_prism():
    if 'l' in request.args and 'w' in request.args and 'h' in request.args:
        l=int(request.args['l'])
        w=int(request.args['w'])
        h=int(request.args['h'])
        v=l*w*h
        ret={'v':v, 'l':l, 'w':w, 'h':h}
        return json.dumps(ret), 200, {"Content Type":'application/json'}
    else:
        return(err_404(404))

@app.route('/volume/pyramid', methods=['GET'])
def volume_pyramid():
    if 'b' in request.args and 'h' in request.args:
        b=int(request.args['b'])
        h=int(request.args['h'])
        v=b*b*h/3
        ret={'v':v, 'b':b, 'h':h}
        return json.dumps(ret), 200, {"Content Type":'application/json'}
    else:
        return(err_404(404))

@app.route('/volume/cylinder', methods=['GET'])
def volume_cylinder():
    if 'r' in request.args and 'h' in request.args:
        r=int(request.args['r'])
        h=int(request.args['h'])
        v=math.pi*r*r*h
        ret={'v':v, 'r':r, 'h':h}
        return json.dumps(ret), 200, {"Content Type":'application/json'}
    else:
        return(err_404(404))

@app.route('/volume/cone', methods=['GET'])
def volume_cone():
    if 'r' in request.args and 'h' in request.args:
        r=int(request.args['r'])
        h=int(request.args['h'])
        v=math.pi*r*r*h/3
        ret={'v':v, 'r':r, 'h':h}
        return json.dumps(ret), 200, {"Content Type":'application/json'}
    else:
        return(err_404(404))

@app.route('/volume/sphere', methods=['GET'])
def volume_sphere():
    if 'r' in request.args:
        r=int(request.args['r'])
        v=4*math.pi*r*r*r/3
        ret={'v':v, 'r':r}
        return json.dumps(ret), 200, {"Content Type":'application/json'}
    else:
        return(err_404(404))

@app.route('/distance', methods=['GET'])
def distance():
    if 'x1' in request.args and 'x2' in request.args and 'y1' in request.args and 'y2' in request.args:
        x1=int(request.args['x1'])
        x2=int(request.args['x2'])
        y1=int(request.args['y1'])
        y2=int(request.args['y2'])
        d=math.sqrt(math.pow((x2-x1), 2)+math.pow((y2-y1), 2))
        ret={'d':d, 'x1':x1, 'x2':x2, 'y1':y1, 'y2':y2}
        return json.dumps(ret), 200, {"Content Type":'application/json'}
    else:
        return(err_404(404))

@app.route('/slope', methods=['GET'])
def slope():
    if 'x1' in request.args and 'x2' in request.args and 'y1' in request.args and 'y2' in request.args:
        x1=int(request.args['x1'])
        x2=int(request.args['x2'])
        y1=int(request.args['y1'])
        y2=int(request.args['y2'])
        m=(y2-y1)/(x2-x1)
        ret={'m':m, 'x1':x1, 'x2':x2, 'y1':y1, 'y2':y2}
        return json.dumps(ret), 200, {"Content Type":'application/json'}
    else:
        return(err_404(404))

@app.route('/pythag', methods=['GET'])
def pythag():
    if 'a' in request.args and 'b' in request.args:
        a=int(request.args['a'])
        b=int(request.args['b'])
        c=math.sqrt(math.pow(a, 2)+math.pow(b, 2))
        ret={'a':a, 'b':b, 'c':c}
        return json.dumps(ret), 200, {"Content Type":'application/json'}
    elif 'a' in request.args and 'c' in request.args:
        a=int(request.args['a'])
        c=int(request.args['c'])
        b=math.sqrt(math.pow(c, 2)-math.pow(a, 2))
        ret={'a':a, 'b':b, 'c':c}
        return json.dumps(ret), 200, {"Content Type":'application/json'}
    elif 'b' in request.args and 'c' in request.args:
        b=int(request.args['b'])
        c=int(request.args['c'])
        a=math.sqrt(math.pow(c, 2)-math.pow(b, 2))
        ret={'a':a, 'b':b, 'c':c}
        return json.dumps(ret), 200, {"Content Type":'application/json'}
    else:
        return(err_404(404))

@app.route('/average', methods=['GET'])
def average():
    if 'nums' in request.args:
        nums=(request.args['nums'])
        realnums=nums.split(",")
        result=0
        count=0
        allnums=[]
        for x in realnums:
            result=result+int(x)
            count=count+1
            allnums.append(int(x))
        result=result/count
        ret={'avg':result, 'nums':allnums}
        return json.dumps(ret), 200, {"Content Type":'application/json'}
    else:
        return(err_404(404))

@app.errorhandler(404)
def err_404(e):
    return "Couldn't find page", 404

app.run(host='127.0.0.1', port=3001)
