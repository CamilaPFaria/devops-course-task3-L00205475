#Ref.: https://prometheus.github.io/client_python/
from prometheus_client import Counter, Gauge, generate_latest, CONTENT_TYPE_LATEST

REQUEST_COUNT = Counter( #Counts events that increase over time
    'pet_catalog_requests_total',
    'Total number of requests to the Pet Catalog API'
)

PET_COUNT = Gauge( #Measures a value that can increase or decrease.
    'pet_catalog_pets_total',
    'Current number of pets registered'
)