from python:3.10.2

EXPOSE 8501

Add . /dashboard

WORKDIR /dashboard

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN python3 -m nltk.downloader stopwords

CMD ["streamlit", "run", "dashboard.py"]