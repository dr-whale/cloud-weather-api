from general_api import app

if __name__ == '__main__':
    print('staring date api')
    app.run(host='0.0.0.0', port=5000, debug=True)