# 🕒 IST Time Printer (Dockerized Python App)

This is a simple Python application that prints the **current date, time, and day** in **Indian Standard Time (IST)**. The app is containerized using Docker and can be pulled and run easily.

## 📌 Features
- Prints current IST date, time, and day.
- Uses Python's `datetime` and `pytz` libraries.
- Fully containerized with Docker.
- Lightweight image using `python:3.9-slim`.

# How to run this 
1) Make sure 
-Docker installed
-Git installed

2) In CMD print this one by one

---Clone the Repository   

-git clone https://github.com/Mamta-Rajbhar/ist-time-docker.git
-cd ist-time-docker

---Build the Docker Image

docker build -t ist-time-printer .

---Run the Container

docker run ist-time-printer

