# Use the official n8n image as the base image
FROM n8nio/n8n

# Switch to root user to install packages
USER root

# Install Python 3 and pip with necessary dependencies
RUN apk add --update python3 py3-pip gcc python3-dev musl-dev curl ffmpeg

# Create and activate virtual environment
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install yt-dlp
RUN pip install yt-dlp

# Make sure the node user can access the Python environment
ENV PYTHONPATH="/opt/venv/lib/python3.11/site-packages:${PYTHONPATH:-}"

# Switch back to node user (the default n8n user)
USER node