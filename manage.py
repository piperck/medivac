from app import app
from flask_script import Manager, Server

manager = Manager(app)

manager.add_command("server", Server(port=10207, use_debugger=True))


@manager.shell
def make_shell_context():
    return dict(app=app)


if __name__ == "__main__":
    manager.run()
