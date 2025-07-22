
## Setup
```bash
gcloud auth application-default login
gcloud auth application-default set-quota-project [PROJECT_ID]

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Start with log file
```bash
python -u main.py | tee log-file-name.log
```

## Reference
 - [Live API reference](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/multimodal-live)
 - [Google Gen AI SDK python](https://cloud.google.com/vertex-ai/generative-ai/docs/sdks/overview)
 - [genai.live module](https://googleapis.github.io/python-genai/genai.html#module-genai.live)
