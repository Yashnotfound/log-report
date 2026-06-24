#!/bin/bash
# pytest + pytest-json-ctrf are baked into environment/Dockerfile; install nothing here.
mkdir -p /logs/verifier

if pytest /tests/test_outputs.py -rA --ctrf /logs/verifier/ctrf.json; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

exit 0
