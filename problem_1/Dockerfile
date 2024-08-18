FROM python:3.9-slim
WORKDIR /app
ARG export_file=spec.json
COPY $export_file /app/spec.json
COPY FixedWidthFileProcessor.py /app
CMD ["python", "FixedWidthFileProcessor.py"]