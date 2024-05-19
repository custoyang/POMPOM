from website import create_app, compartment
from threading import Thread
from time import time

app = create_app()

if __name__ == '__main__':
    # Create a thread to run the background task
    thread = Thread(target=compartment.background_task, args=(app,))
    thread.start()  # Start the background task thread

    # Now run the Flask app (in the main thread)
    app.run(debug=True, host='127.0.0.1', port=5000)

    thread.join()