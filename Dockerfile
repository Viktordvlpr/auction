FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

# Set the working directory in the container
WORKDIR /auction

# Copy the rest of the application code
COPY . /auction/

# Install dependencies
RUN pip install -r auctionsonline/requirements.txt

# Expose the port
EXPOSE 8000

# Define the command to run your application
CMD ["sh", "start.sh"]

