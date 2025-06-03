from app import create_app
from waitress import serve

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
    print("Servidor desde waitress en port 5000")
    #serve(app, port=5000)
    
