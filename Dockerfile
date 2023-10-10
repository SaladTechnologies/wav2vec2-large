FROM python:3.10-slim

ARG MODEL_ID=jonatasgrosman/wav2vec2-large-xlsr-53-english
ENV MODEL_ID=$MODEL_ID

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt --extra-index-url https://download.pytorch.org/whl/cu116

# Download the model
RUN python -c "from huggingsound import SpeechRecognitionModel; model = SpeechRecognitionModel('$MODEL_ID')"

# Copy the code
COPY main.py .

CMD ["python", "main.py"]