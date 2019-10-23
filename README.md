# Gooseify

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/liamdawson/gooseify/master?filepath=experiment.ipynb)

Needs more cowbell, but for geese. "Watermarks" MP3 files with the goose honk from the Untitled Goose Game.

## Jupyter

```shell
docker-compose up --build
# http://127.0.0.1:8888/lab/tree/work/experiment.ipynb?token=effort
```

## Serverless

```shell
cd sam-app
sam build
aws-vault exec <profile> -- sam package --s3-bucket <package-destination-bucket> --output-template-file packaged.yaml
aws-vault exec <profile> -- sam deploy --stack-name <stack-name> --template-file packaged.yaml --capabilities CAPABILITY_IAM CAPABILITY_AUTO_EXPAND
```

## Attribution

Audio files [credited here](./media/CREDITS.md)
