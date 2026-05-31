from flask import Flask, request, render_template
from main import get_list
import traceback

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        prompt = request.form.get("prompt", "")
        if not prompt.strip():
            return render_template("index.html", error="Please enter a valid event description.")

        try:
            data = get_list(prompt)
            
            # Calculate total budget from the items
            total_price = 0
            for item in data.get('items', []):
                try:
                    price_str = ''.join(c for c in str(item.get('price', '0')) if c.isdigit())
                    if price_str:
                        total_price += int(price_str)
                except Exception:
                    pass

            return render_template("index.html", res=data, total_price=total_price)

        except Exception as e:
            traceback.print_exc()
            return render_template("index.html", error=str(e))

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)