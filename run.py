import os
import env
from bird_friend import create_app, db
from bird_friend import users

app = create_app()

if __name__ == '__main__':
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)
