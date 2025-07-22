
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



## Token Usage 

### 음성 데이터 (weather.wav)

#### gemini-live-2.5-flash 

Output: 내일 서울은 흐리고 최저 13도 최고 23도까지 올라가겠습니다.

*** 모델의 특성에 의해 상세 토큰에 Output Text Token 26 가 보인다 ***
*** 모델의 특성에 의해 상세 토큰에 Output Text Token 이 없고 Audio 토큰만 보인다. ***

```python
 prompt_token_count=69 cached_content_token_count=None response_token_count=176 tool_use_prompt_token_count=None thoughts_token_count=None total_token_count=245 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.AUDIO: 'AUDIO'>,
  token_count=58
), ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=11
)] cache_tokens_details=None response_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=26
), ModalityTokenCount(
  modality=<MediaModality.AUDIO: 'AUDIO'>,
  token_count=150
)] tool_use_prompt_tokens_details=None traffic_type=None
```

#### gemini-live-2.5-flash-preview-native-audio

Output: 네, 내일 서울은 가끔 구름이 끼는 날씨일 것 같아요. 낮 최고 기온은 30도 최저 기온은 22도 정도 예상됩니다. 강수 확률은 좀 낮고요. 바람은 강하지 않을 거예요. 더 자세한 날씨 정보가 필요하시면 다시 말씀해주세요.

```python
prompt_token_count=70 cached_content_token_count=None response_token_count=440 tool_use_prompt_token_count=None thoughts_token_count=None total_token_count=510 prompt_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.AUDIO: 'AUDIO'>,
  token_count=59
), ModalityTokenCount(
  modality=<MediaModality.TEXT: 'TEXT'>,
  token_count=11
)] cache_tokens_details=None response_tokens_details=[ModalityTokenCount(
  modality=<MediaModality.AUDIO: 'AUDIO'>,
  token_count=440
)] tool_use_prompt_tokens_details=None traffic_type=None
```

