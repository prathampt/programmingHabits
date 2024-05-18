#!/bin/bash

awk '{ total += $NF; count++ } END { print "Average Rating: " (total/count) }' ../logs/session.log
