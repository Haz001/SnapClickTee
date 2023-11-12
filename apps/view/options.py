from flask import Flask, render_template, jsonify, request

from apps import app



@app.route('/options', methods=['GET'])
def options():
    data = [
    {
        "item_code": "RNA1",
        "name": "Custom Product",
        "image_url": "https://images.teemill.com/5ac78910f1d546.28128958.png",
        "colours": {
            "White": "https://images.teemill.com/5ac78910f1d546.28128958.png",
            "Black": "https://images.teemill.com/5ac784b4ee9c11.75415064.png",
            "Bright Blue": "https://images.teemill.com/5ac785427cb151.12626171.png",
            "Pink": "https://images.teemill.com/cbhvkuohnzkqugkwflba0stxut0bpozpp9bc41yt9qvni5dr.png"
        },
        "design_placement": {
            "x": 0.318608287724785,
            "y": 0.23588410104011887,
            "w": 0.35887412040656763,
            "h": 0.4550520059435364
        }
    },
    # Include more data as needed
]

    return render_template('options.html', data=data)


@app.route('/show-product', methods=['GET'])
def show_product():
    
    data = request.args.get("image")

    return render_template('show-product.html', image_url=data)
