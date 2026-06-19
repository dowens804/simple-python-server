from api import *

if __name__ == '__main__':
   app = create_app()

   app.run(port=8000, debug=True)

   #flask --app api run --debug