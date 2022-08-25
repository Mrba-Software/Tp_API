#!/bin/bash

export PGPASSWORD='student'
psql -U 'student' -d 'plants' -a -f /sql/plants.psql