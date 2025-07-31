# Use official Python image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --upgrade pip && \
    pip install .

# Expose port (use environment variable, default 2004)
EXPOSE 2004

# Set default port env
ENV PORT=2004

# Set a volume for persistent storage of notes
VOLUME ["/data"]

# Update the NOTES_FILE path to use the volume
ENV NOTES_FILE=/data/notes.txt

# Command to run the MCP server directly
CMD ["python", "notes.py"]
