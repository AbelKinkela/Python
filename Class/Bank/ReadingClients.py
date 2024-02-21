import pickle

if __name__ == "ReadingClients":
    with open("clients.data", "rb") as file:
        clients = {}
        while True:
            try:
                client = pickle.load(file)
                clients[client.name] = client
            except:
                break

        # Try and except is used because we used multiple invocations of pickle.dump 
        # to save/dump multiple objects into same stream.
        # it is prefered to use a single dump to dump all objects by packing them up in a tuple
        # ex: pickle.dump((a, b, c), file) so now a single pickle.load() will load all objects







      