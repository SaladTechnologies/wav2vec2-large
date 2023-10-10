# wave2vec2-large
An inference server for jonatasgrosman/wav2vec2-large-xlsr-53-english

## Build

```bash
docker buildx build -t saladtechnologies/wav2vec2-large:latest \
--provenance=false \
--output type=docker \
.
```

## Run

```bash
docker run \
-p 1111:1111 \
docker.io/saladtechnologies/wav2vec2-large:latest
```

## Test

```bash
curl  -X POST \
  'http://localhost:1111/transcribe' \
  --header 'Content-Type: application/octet-stream' \
  --data-binary '@/home/shawn/code/SaladTechnologies/wav2vec2-large/Recording.mp3'
```

```json
{"text":"wavetevec to infancs server is working as intended","inference_time":1.0019206859869882}
```