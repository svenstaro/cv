#!/usr/bin/env bash

HOST=tank
CODE_DIR="/home/svenstaro/prj/cv"
DEPLOY_DIRS=("/srv/http/pseudoform.org" "/srv/http/customalized.org" "/srv/http/svenstaro.org")

ssh $HOST "cd $CODE_DIR && git pull"
for deploy_dir in "${DEPLOY_DIRS[@]}"; do
    ssh $HOST "cp $CODE_DIR/* $deploy_dir"
done
