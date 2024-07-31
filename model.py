from fastapi import FastAPI
#import ray
from ray import serve

#ray.init(address="auto")  # Connect to the Ray cluster

app = FastAPI()

@serve.deployment(num_replicas=1)
@serve.ingress(app)
class HelloModel:
    def __init__(self):
        # Load your model here
        pass

    @app.get("/classify")
    def classify(self, request):
        # Perform inference here
        return {"result": "Hello world"}

hello = HelloModel.bind()
