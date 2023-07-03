from flask import Flask, request, jsonify
from dictionario import AAMVA 
from pdf417decoderr import PDFDecoderLicense
app = Flask(__name__)


@app.route('/getmsg/', methods=['GET'])
def respond():
    aamva = AAMVA("""@
ANSI 636014090002DL00410276ZC03170024DLDAQA7304733
DCSNARANJOVILLALOBOS
DDEN
DACLUIS
DDFN
DADNONE
DDGN
DCAC
DCBNONE
DCDNONE
DBD09272018
DBB12271973
DBA12272023
DBC1
DAU066 IN
DAYBRO
DAGPO BX 917
DAIATWATER
DAJCA
DAK953010000
DCF09/27/201853633/AAFD/23
DCGUSA
DAW187
DAZBLK
DCK18274A73047330401
DDAF
ZCZCABRN017
ZCBBLK
ZCC
ZCD""");
    result = aamva.parseDriverLicense()
    # Retrieve the name from the url parameter /getmsg/?name=
    name = request.args.get("name", None)
    # For debugging
    print(f"Received: {name}")
    response = {}
    # Check if the user sent a name at all
    if not name:
        response["ERROR"] = "No name found. Please send a name."
    # Check if the user entered a number
    elif str(name).isdigit():
        response["ERROR"] = "The name can't be numeric. Please send a string."
    else:
        #response["MESSAGE"] = f"Welcome {name} to our awesome API!"
        response["Result"]=result

    # Return the response in json format
    return jsonify(response)

@app.route('/post/', methods=['POST'])
def post_something():
    param = request.get_json()
    #request.form.get('name')
    print(param["name"])
    # You can add the test cases you made in the previous function, but in our case here you are just testing the POST functionality
    if param:
        return jsonify({
            "Message": f"Welcome {param['name']} to our awesome API!",
            # Add this option to distinct the POST request
            "METHOD": "POST"
        })
    else:
        return jsonify({
            "ERROR": "No name found. Please send a name."
        })
@app.route("/lupitasgroup/v1/api/drivelicense/load", methods=['POST'])
def load_license():
    try:
        image=request.files['image']
        image_name=image.filename
        pdf = PDFDecoderLicense(image)
        aamva = AAMVA(pdf.decode())
        result = aamva.parseDriverLicense()
        return {"decode":result}
        #if '.jpg' in image_name:
        #    image.save(image_name)
        #    return {"response":"file saved successfully in your current durectory"}
        #elif '.jpeg' in image_name: 
        #    image.save(image_name)
        #    return {"response":"file saved successfully in your current durectory"}
        #else:
        #    return {"error":"select you image file"}
    except Exception as e:
        return {"error":str(e)}

@app.route('/')
def index():
    # A welcome message to test our server
    return "<h1>Welcome to our medium-greeting-api!</h1>"


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)