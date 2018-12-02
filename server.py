from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Welcome to EatGeek!'


@app.route('/nutrition')
def nutrition():
    description = request.args.get(
        'description') or request.args.get('desciption')

    return {
        "Loaded Fries queso monterey jack cheddar bacon green onions bbq ranch": jsonify({"sugar": "6 g", "carbohydrates": "95 g"}),
        "Spinach Florentine Flatbread spinach artichoke hearts monterey jack parmesan romano tomatoes garlic fresh basil crushed red pepper oregano": jsonify({"sugar": "4 g", "carbohydrates": "51 g"}),
        "BBQ Chicken Flatbread chipotle chicken bbq sauce monterey jack cheddar cilantro red peppers red onions": jsonify({"sugar": "18 g", "carbohydrates": "66 g"}),
        "Crispy Brussels Sprouts lemon soy vinaigrette roasted onions croutons cotija cheese": jsonify({"sugar": "8 g", "carbohydrates": "38 g"}),
        "Giant Onion Rings bbq ranch": jsonify({"sugar": "33 g", "carbohydrates": "155 g"}),
        "none": jsonify({"sugar": "0-7 g", "carbohydrates": "0-10 g"})
    }[description or "none"]
