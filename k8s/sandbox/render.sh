#!/bin/bash

set -u

pip install j2cli[yaml]
j2 k8s/sandbox/configmap.j2 -o k8s/sandbox/configmap.yaml
j2 k8s/sandbox/monolith.j2 -o k8s/sandbox/monolith.yaml