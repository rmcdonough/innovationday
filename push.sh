#!/bin/bash

ACCOUNT_NUMBER="REPLACEME"
ECRURL=".dkr.ecr.us-west-2.amazonaws.com/"

APPS="python-app-1
python-app-2
python-app-3"

# Login to ECR
# aws ecr get-login --no-include-email --region us-west-2 | bash

for APP in $APPS ; do
	docker tag $APP:latest $ACCOUNT_NUMBER.dkr.ecr.us-west-2.amazonaws.com/$APP:latest
	docker push $ACCOUNT_NUMBER.dkr.ecr.us-west-2.amazonaws.com/$APP:latest
done
