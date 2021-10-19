import os
from bird_friend import create_app, db
from bird_friend.models import User, Birdtype

app = create_app()

if __name__ == '__main__':
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User,
            'Bird': Bird, 'Birdtype': Birdtype}
