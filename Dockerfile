# Light-weight version of python
FROM python:3.11-buster

ARG GITHUB_TOKEN

WORKDIR /src

# Copy source code
COPY app.py app.py
COPY consts.py consts.py
COPY utils.py utils.py
COPY res res
COPY requirements.txt requirements.txt
COPY .streamlit/config.toml .streamlit/config.toml

# Install python dependencies using pip3
# sed here turns -> the git url of "ssh://" -> "https://$GITHUB_TOKEN"
# to utilize the GITHUB_TOKEN as auth instead of the SSH.
RUN sed -E "s/git\+.+northvolt\//git+https:\/\/$GITHUB_TOKEN@github.com\/northvolt\//g" requirements.txt > requirements.tmp
RUN mv requirements.tmp requirements.txt
RUN pip3 install -r requirements.txt

# Expose port
EXPOSE 8501

# Clean image
RUN rm -rf /var/cache/apt/* /var/lib/apt/lists/*

# Clean pip cache
RUN pip3 cache purge

ENTRYPOINT streamlit run app.py
