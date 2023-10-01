from flask import Flask, render_template, request
import requests
from spellchecker import SpellChecker

spell=SpellChecker()

app = Flask(__name__)

client_id = "Your API KEY Here"

@app.route('/', methods=['GET', 'POST'])
def img_search_engine():
    response = None 
    result=[]
    if request.method == 'POST':
        query = request.form['query']
        query=spell.correction(query)
        url = f"https://api.unsplash.com/search/photos?page=all&query={query}&client_id={client_id}"
        response = requests.get(url)
        response = response.json()
        if int(response['total_pages'])>=10:

    
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

    
    return render_template("index.html", data=result,query=query)

if __name__ == '__main__':
    app.run(debug=False)
