#!/bin/bash
python main.py db initdb
python main.py db migrate
python main.py db upgrade
