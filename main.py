import firebase_admin
import os
from flask import Flask, render_template, redirect, request, url_for
from firebase_admin import db
from imagekitio import ImageKit

# Firebase initialisation
cred_obj = firebase_admin.credentials.Certificate('accountKey.json')
default_app = firebase_admin.initialize_app(cred_obj, {
    'databaseURL': 'https://shopify-image-repo-7f0bf-default-rtdb.firebaseio.com/'
})
ref = db.reference("/images/")

#Image Kit Init
imagekit = ImageKit(private_key='private_azyVXCwBdmBM9TO++PkJErGG3sU=', public_key='public_e1i/9agQd1MCaDe1JVh40+sPVAM=', url_endpoint='https://ik.imagekit.io/dijbqlcndty/')


# Flask initialization
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


def saveUrl(upload):
    res = list(upload.values())[1] #Get the response from the upload
    uri = list(res.values())[4] #Get the url from the response
    ref.push().set({"url":uri}) #Put the url in firebase for later use

@app.route('/add', methods=['POST'])
def addFile():
    if request.method == 'POST':
        files = request.files.getlist('file') #Get chosen files as an array
        # PROCESS FILES HERE

        for f in files: #Loop through files array
            upload = imagekit.upload( #Upload individual files to imagekit
                file=f,
                file_name=f.filename)

            saveUrl(upload) #Save upload url to firebase

        return render_template('view.html', len=len(getImages()), links=getImages())


@app.route('/view')
def myfunc():
    links = getImages()
    return render_template('view.html', links=links, len=len(links))

def getImages(): #Retreives image urls from firebase and returns as array of strings
    images = ref.get()
    toRet = []
    for key, val in images.items():
        toRet.append(val['url'])
    return toRet

