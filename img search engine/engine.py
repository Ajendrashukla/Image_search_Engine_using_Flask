from flask import Flask, render_template, request
import requests
from spellchecker import SpellChecker
import pandas as pd
app = Flask(__name__)
spell=SpellChecker()
client_id = "Your API KEY"

@app.route('/', methods=['GET', 'POST'])
def img_search_engine():
    response = None 
    result=[]
    if request.method == 'POST':
        query = request.form['query']
        t=query.split()
        query=""
        for word in t:
            word= spell.correction(word)
            query=query+str(word)+" "

        url = f"https://api.unsplash.com/search/photos?page=all&query={query}&client_id={client_id}"
        response = requests.get(url)
        response = response.json()
        response= response["results"]
        for i in range(9):
            temp= response[i]
            l=[]
            l.append(temp["urls"]["small"])
            l.append(temp["likes"])
            l.append(temp["alt_description"].capitalize())
            l.append(temp["urls"]["raw"])
            result.append(l)
        result=sorted(result,key=lambda x:x[1],reverse=True)
            
    else:
        query='Please Enter a KeyWOrd to Search Images'
    print(pd.DataFrame(result))
    
    return render_template("index.html", data=result,query=query)

if __name__ == '__main__':
    app.run(debug=True)
