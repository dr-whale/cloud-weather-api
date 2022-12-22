from testapi import app

if __name__ == '__main__':
    print('staring flask app')
    app.run(host='0.0.0.0', port=5000, debug=True)
