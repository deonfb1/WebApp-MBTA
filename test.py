from multiprocessing import Process

server = Process(target=app.run)
server.start()
# ...
server.terminate()
server.join()