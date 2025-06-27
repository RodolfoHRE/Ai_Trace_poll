FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /app/ai_trace_poll


RUN pip install --upgrade pip
COPY requirements.txt /app/ai_trace_poll/
RUN pip install -r /app/ai_trace_poll/requirements.txt


COPY ai_trace_poll /app/ai_trace_poll
COPY entrypoint.sh /app/
RUN chmod +x /app/entrypoint.sh


CMD ["/app/entrypoint.sh"]



