from flask import Flask, request, jsonify

app = Flask(_name_)

html_page = """

<!DOCTYPE html>
<html>

<head>

<title>AdSpark</title>

<style>

body{
font-family: Arial;
background:#f0f2f5;
text-align:center;
}

header{
background:#2f6ea6;
color:white;
padding:30px;
}

.container{
margin-top:40px;
}

input{
display:block;
margin:15px auto;
padding:12px;
width:300px;
border:1px solid #ccc;
border-radius:4px;
}

button{
padding:12px 25px;
background:#2f6ea6;
color:white;
border:none;
cursor:pointer;
border-radius:4px;
}

button:hover{
background:#1e4f7a;
}

#result{
margin-top:25px;
font-size:18px;
color:green;
}

</style>

</head>

<body>

<header>

<h1>AdSpark</h1>

<p>Generative AI Marketing Intelligence Platform</p>

</header>

<div class="container">

<h2>AI Campaign Generator</h2>

<input type="text" id="product" placeholder="Enter Product Name">

<input type="text" id="audience" placeholder="Target Audience">

<button onclick="generateCampaign()">Generate Campaign</button>

<div id="result"></div>

</div>

<script>

async function generateCampaign(){

let product = document.getElementById("product").value

let audience = document.getElementById("audience").value

let response = await fetch("/generate",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({
product:product,
audience:audience
})

})

let data = await response.json()

document.getElementById("result").innerHTML =
"AI Marketing Strategy: " + data.idea

}

</script>

</body>
</html>

"""

@app.route("/")
def home():
    return html_page


@app.route("/generate", methods=["POST"])
def generate():

    data = request.json

    product = data["product"]
    audience = data["audience"]

    strategies = [
    "Use Instagram influencers and short video ads.",
    "Launch a limited-time discount campaign.",
    "Promote through YouTube tech reviewers.",
    "Run targeted Facebook and Google ads.",
    "Use email marketing campaigns."
    ]

    import random

    result = f"Promote {product} to {audience}. Strategy: {random.choice(strategies)}"

    return jsonify({"idea": result})


if _name_ == "_main_":
    app.run(debug=True)