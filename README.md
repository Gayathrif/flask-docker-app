flask-docker-app

Simple Flask Web Application with Docker Compose
This project contains a simple Flask web application that responds with Hello, Gayathri C Nair & Register Number 2022BCD0011. The application is containerized using Docker and managed with Docker Compose, including a PostgreSQL database.

Project Structure
/
├── app.py              # Flask application
├── Dockerfile          # Docker configuration for web service
├── docker-compose.yml  # Docker Compose configuration
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
Prerequisites
Install Docker: Follow instructions from Docker's official website.
Install Docker Compose: Follow Docker Compose installation guide.
Create a GitHub repository to store your project.
Setup Instructions
1. Clone the Repository
Clone the repository to your local machine:

git clone https://github.com/Gayathrif/flask-docker-app.git
cd flask-docker-app
2. Create a requirements.txt File
Ensure you have a requirements.txt file with the necessary dependencies:

flask
psycopg2
3. Build and Run the Application
a) Build the Docker images
docker-compose build
b) Start the services (web and database)
docker-compose up -d
c) Verify running containers
Check if both web and db services are running:

docker ps
4. Access the Web Application
Open your browser and navigate to:

http://localhost:5000
You should see the message: Hello, Gachu & Register Number 12345

5. Connect to the Database
To connect to the PostgreSQL database from a terminal:

docker exec -it <container_id> psql -U user -d testdb
Replace <container_id> with the actual ID of your PostgreSQL container (find it using docker ps).

6. Stop and Remove Containers
a) Stop the running containers
docker-compose down
b) Remove all containers, networks, and volumes (optional)
docker system prune -a
Pushing the Project to GitHub
If you haven’t pushed your project to GitHub yet, follow these steps:

git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/Gayathrif/flask-docker-app.git
git push -u origin main
Troubleshooting
1. Check logs if something isn't working
docker-compose logs
2. Restart the services
docker-compose down && docker-compose up -d