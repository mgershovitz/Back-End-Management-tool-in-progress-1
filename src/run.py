from src.app import app

if __name__ == "__main__":
    try:
        from waitress import serve
        serve(app, host='0.0.0.0', port=8000)
    except:
        print('unable to open port')
