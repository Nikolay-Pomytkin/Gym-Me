#!/bin/bash

cd server

# export environment variables to run server
export FLASK_APP=server.py
export FLASK_ENV=development

# run the server
flask run

