#!/bin/bash
set -eu

ATTEMPTS=0
MAX_ATTEMPTS=30
SLEEP=10
DEPLOYMENT="deployment/$PRINT_NANNY_USER-sandbox"
ROLLOUT_STATUS_CMD="kubectl rollout status $DEPLOYMENT"
until $ROLLOUT_STATUS_CMD || [ $ATTEMPTS -eq $MAX_ATTEMPTS ]; do
  $ROLLOUT_STATUS_CMD
  ATTEMPTS=$((attempts + 1))
  echo "Waiting $SLEEP sec for $DEPLOYMENT rollout to complete"
  sleep $SLEEP
done

DEPLOYMENT="deployment/$PRINT_NANNY_USER-octoprint"
ROLLOUT_STATUS_CMD="kubectl rollout status $DEPLOYMENT"
until $ROLLOUT_STATUS_CMD || [ $ATTEMPTS -eq $MAX_ATTEMPTS ]; do
  $ROLLOUT_STATUS_CMD
  ATTEMPTS=$((attempts + 1))
  echo "Waiting $SLEEP sec for $DEPLOYMENT rollout to complete"
  sleep $SLEEP
done