import os
import psycopg2

#print (os.environ["postgres://avtewvteiychwo:9c83675ee5711d33eda27d2695c9ef0edf09773d7e263bb659a430f509aba9fa@ec2-34-247-72-29.eu-west-1.compute.amazonaws.com:5432/d36nh82s7jdv8s"])
DATABASE_URL = os.environ.get('postgres://avtewvteiychwo:9c83675ee5711d33eda27d2695c9ef0edf09773d7e263bb659a430f509aba9fa@ec2-34-247-72-29.eu-west-1.compute.amazonaws.com:5432/d36nh82s7jdv8s')
#DATABASE_URL = os.environ["HEROKU_POSTGRESQL_CRIMSON_URL"]

conn = psycopg2.connect(DATABASE_URL, password="")

print("connected")