import streamlit as st

st.title("Welcome to *Streamlit* with *Docker*!" )
st.write("This is a simple web application built using Streamlit and Docker.")

st.header("🚀 Introducing Streamlit with Docker")
st.write("Docker and Streamlit work together to create a streamlined and reproducible development environment for building and deploying data-driven web applications. Here’s why this combination is powerful:")
st.write("- **Reproducibility**: By containerizing the application, you ensure that it runs identically on any system with Docker installed.")
st.write("- **Easy Deployment**: Package your app and all its dependencies into a single container, simplifying sharing and deployment.")
st.write("- **Isolation**: Keeps your app's dependencies separate from other software on your machine, preventing conflicts.")
st.write("- **Consistency Across Environments**: Ensures the same behavior in development, testing, and production environments.")

st.header("⚙️ Installing Required Software")
st.write("Before getting started, ensure you have the necessary software installed:")
st.write("1. Install [Docker](https://docs.docker.com/get-docker/) for your operating system.")
st.write("2. Install Python (if not already installed) and then install Streamlit:")
st.code("""
pip install streamlit
""", language='bash')

st.header("📜 How to Get *Streamlit* Up and Running")
st.write("1. Create a Python file (e.g., `app.py`) and import Streamlit.")
st.write("2. Use `st.title()` to set the title of your app.")
st.write("3. Add interactive components using functions like `st.write()`, `st.header()`, etc.")
st.write("4. Run your Streamlit app:")
st.code("""
streamlit run app.py
""", language='bash')

st.header("🐳 Steps to Run the App in *Docker*")
st.write("1. **Create a Dockerfile** in the same directory as your `app.py` file.")
st.code("""
# Use the official Python image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy files to the container
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose port 8501
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
""", language='dockerfile')
st.write("2. **Create a `requirements.txt` file** and list the dependencies:")
st.code("""
streamlit
pandas
numpy
""", language='plaintext')
st.write("3. **Create a `.dockerignore` file** to exclude unnecessary files:")
st.code("""
__pycache__/
.git/
.venv/
*.pyc
""", language='plaintext')
st.write("4. **Build the Docker image:**")
st.code("""
docker build -t streamlit-app .
""", language='bash')
st.write("5. **Run the Docker container in detached mode:**")
st.code("""
docker run -d -p 8501:8501 streamlit-app
""", language='bash')
st.write("6. **Open your browser and visit `http://localhost:8501` to see the app in action.**")
st.write("7. **To access the app from another machine, use:**")
st.code("""
docker run -p 8501:8501 --network=host streamlit-app
""", language='bash')

st.header("☁️ Deploying a Streamlit App")
st.write("Once your app is running locally, you can deploy it using various cloud services. Here is one popular option:")

st.subheader("1️⃣ Deploying with Streamlit Cloud")
st.write("Streamlit offers an easy-to-use cloud platform for hosting apps:")
st.write("1. Push your Streamlit app to a GitHub repository.")
st.write("2. Go to [Streamlit Cloud](https://share.streamlit.io/) and sign in with GitHub.")
st.write("3. Click 'New app' and connect your repository.")
st.write("4. Select the branch and filename (`app.py`).")
st.write("5. Click 'Deploy' to launch your app online.")

st.header("🎉 Enjoy Exploring Streamlit with Docker!")
st.write("Feel free to modify the code, add new features, and experiment with Streamlit components!")
