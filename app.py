#%%
import streamlit as st
#%%
st.title("Welcome to *Streamlit* with *Docker*!")
st.write("This is a simple web application built using Streamlit and Docker.")
# %%
st.header("Introducing, Streamlit with Docker")
st.write("* This is a simple web application running in a Docker container.")
st.write("* You can use this app to demonstrate the capabilities of Streamlit.")
st.write("* Feel free to modify the code and see the changes live!")
st.write("* To run this app, make sure you have Docker installed and use the provided Dockerfile.")
# %% 
st.write("The reason you would use Streamlit with docker would be to create a reproducible environment for your app, ensuring that it runs consistently across different machines.")
#%%
st.header("How to get *Streamlit* up and running")
st.write("1. Install Streamlit using pip: `pip install streamlit`")
st.write("2. Create a Python file (e.g., app.py) and import Streamlit.")
st.write("3. Import streamlit as `st` and use the `st.title()` function to set the title of your app.")
st.write("4. You can also use other Streamlit functions like `st.write()`, `st.header()`, and more to create interactive components.")
st.write("5. To run your Streamlit app, use the command: streamlit run app.py")
# %%
st.header("Steps to Run the App in *Docker*")
st.write("1. Create a Dockerfile in the same directory as this app.py file. Then create a .dockerignore file to exclude unnecessary files.")
st.write("2. Build the Docker image using the command: `docker build -t streamlit-app .`")
st.write("3. Run the Docker container using the command: `docker run -p 8501:8501 streamlit-app`")
st.write("4. Open your web browser and go to `http://localhost:8501` to see the app in action.")
# %%
st.write("5. Enjoy exploring the features of Streamlit!")