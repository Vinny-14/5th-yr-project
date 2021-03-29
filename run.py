import eventlet

eventlet.monkey_patch(select=True, socket=True)

from app import create_app

app = create_app()

if __name__ == '__main__':
    from app.sockets import socketIO
    socketIO.run(app, host='0.0.0.0', port=2791)