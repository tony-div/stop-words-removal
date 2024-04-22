FROM python:latest
RUN pip install nltk
ADD stopwords.py .
ADD paragraphs.txt .
CMD ["python", "./stopwords.py"]