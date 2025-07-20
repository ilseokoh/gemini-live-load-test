
## Setup
```bash
gcloud auth application-default login
gcloud auth application-default set-quota-project [PROJECT_ID]

pip install -f requirements.txt
```

## Start with log file
```bash
python -u main.py | tee text-to-audio.log
```