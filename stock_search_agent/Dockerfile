# Base image
FROM python:3.10

# Set environment variables
ENV PYTHONUNBUFFERED=TRUE
ENV OPENAI_API_KEY=<your_openai_api_key>
ENV SERPER_API_KEY=<your_serper_api_key>
ENV OPENAI_MODEL_NAME='gpt-3.5-turbo'

# Install necessary libraries
RUN pip install --upgrade pip
RUN pip install crewai==0.28.8 crewai_tools==0.1.6 pydantic boto3

# Copy your application code into the container
COPY app.py /opt/ml/code/app.py

# Set the working directory
WORKDIR /opt/ml/code

# Command to run the application
ENTRYPOINT ["python", "app.py"]
