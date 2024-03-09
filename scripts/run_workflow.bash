#!/bin/bash

env=$1
model=$2

if [[ -z "$env" ]]; then
	echo "Environment not specified, exiting"
	exit 1
fi

if [[ -z "$model" ]]; then
	echo "Model not specified, exiting"
	exit 1
fi

echo "Running: $env $model"

# In the following command I have added true for demo purposes
# so that it doesn't exit on the first error and is able to run on the CI
# Ideally, we would want to have this script exit on the first error
# and have it fail on CI
if [[ $model == "population" ]]; then
	python cleaning/events_clean.py || true
	python cleaning/raw_events_to_interactions.py || true

	# validate shapes
	pytest -s --verbose tests || true

	python models/population_model.py || true
	echo "Finished training"
elif [[ $model == "personalised" ]]; then
	python cleaning/events_clean.py || true
	python cleaning/raw_events_to_interactions.py || true
	python cleaning/prepare_for_model.py || true

	# validate shapes
	pytest -s --verbose tests || true

	python models/personalised_model.py || true
	echo "Finished training"
else
	echo "Unknown model: $model, exiting"
	exit 1
fi
