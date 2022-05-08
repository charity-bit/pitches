from app import create_app,db
from flask_script import Manager,Server
from flask_migrate import Migrate,MigrateCommand
from app.models import User,Pitch,Comment
app = create_app('development')


migrate= Migrate(app,db)
manager = Manager(app)
manager.add_command('server',Server)
manager.add_command('run',Server)
manager.add_command('db',MigrateCommand)


@manager.shell
def make_shell_context():
    return dict(app = app,User = User,db = db,Pitch = Pitch)



if __name__ == '__main__':
    manager.run()
