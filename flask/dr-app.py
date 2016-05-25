from flask import Flask, request
from pymongo import MongoClient
import hashlib
import json

app = Flask(__name__)

@app.route('/dr', methods = ['POST'])
def api_message():
    mydata = request.get_json()
    client = MongoClient('localhost', 27017)
    db = client.folksdb
    posts = db.posts
    name = ''
    for ele in mydata:
        chksum = ele['md5checksum']
        ndata = ele
        del ndata['md5checksum']
        s=json.dumps(ndata)
        md5 = hashlib.md5()
        md5.update(s)
        if md5.hexdigest() == chksum:
            post_id = posts.insert_one(ndata)
        if md5.hexdigest() != chksum:
            failed = ndata['name']
            name += "\n" + failed
   
   
    return "Records not entered for:%s " % name + "\n"


if __name__ == '__main__':
        app.run(debug=True,host='0.0.0.0', port=int("8080"))

