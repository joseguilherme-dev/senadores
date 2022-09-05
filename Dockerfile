FROM python:3
 
# Set the working directory.
WORKDIR /usr/src/app/senators
 
# Copy the project source code.
COPY . ./

# Install all pip dependencies.
RUN pip3 install --no-cache-dir -r requirements.txt