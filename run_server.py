import sys
from medivac import app


def main():
    try:
        port = int(sys.argv[1])
    except:
        print 'Usage:\n\t./api_server port'
        sys.exit(1)
    app.run(host='0.0.0.0', debug=True, port=port)

if __name__ == '__main__':
    main()
