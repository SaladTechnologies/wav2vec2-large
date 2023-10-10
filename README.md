# wave2vec2-large
An inference server for jonatasgrosman/wav2vec2-large-xlsr-53-english

## Build

```bash
docker buildx build -t saladtechnologies/wave2vec2-large:latest \
--provenance=false \
--output type=docker \
.
```

## Run

```bash
docker run \
-p 1111:1111 \
docker.io/saladtechnologies/wave2vec2-large:latest
```

## Test

```bash
curl  -X POST \
  'http://localhost:1111/transcribe' \
  --header 'Content-Type: application/octet-stream' \
  --data-binary '@/home/shawn/code/SaladTechnologies/wave2vec2-large/Recording.wav'
```

```json
{"text":"lthe whisper-large infranc server is functioning as intended","inference_time":1.1895841190125793}
```