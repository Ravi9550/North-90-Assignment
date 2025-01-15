# North 90 Assignment

## Overview

This project consists of a full-stack web application built with **Django**, **JavaScript**, and **AWS Lambda** services. It includes the following components:

1. **Frontend Development:**
   - A responsive webpage featuring a fixed navbar, a collapsible left menu, a main content area, and a right-side panel.
   - A footer at the bottom of the page.
   - JavaScript functionality for dynamically adjusting the page size based on screen width.
   
2. **Django Chat Application:**
   - A user authentication system (sign up and login).
   - A collapsible left menu that displays all registered users.
   - A chat interface where users can select other users from the menu and initiate a chat.
   - All user data and chat messages are stored in a database.
   - Old chat messages are retrieved and displayed in the interface.
   - WebSockets are used for real-time chat.

3. **AWS Lambda Functions:**
   - A Lambda function that adds two numbers and returns the result.
   - A Lambda function that stores documents or PDFs in an S3 bucket.

## Features

### Frontend Features:
1. **Fixed Navbar:**
   - The navbar remains fixed at the top of the page and does not move when scrolling.
   
2. **Responsive Layout:**
   - The page has three main sections:
     - Left Menu (collapsible).
     - Main Content Area.
     - Right-Side Panel.

3. **Footer:**
   - A footer is displayed at the bottom of the page.

4. **JavaScript Responsiveness:**
   - The page size dynamically shrinks based on the screen width:
     - 992px to 1600px: Shrinks by 90%.
     - 700px to 767px: Shrinks by 80%.
     - 600px to 700px: Shrinks by 75%.
     - 600px or less: Shrinks by 50%.

### Django Chat Application:
1. **User Authentication:**
   - Users can sign up, log in, and authenticate via Django's built-in user authentication system.
   
2. **Collapsible Left Menu:**
   - Displays all registered users, allowing logged-in users to select and start a conversation.

3. **Real-Time Chat Interface:**
   - WebSockets allow users to send and receive messages in real time.
   - Old messages are stored in the database and displayed when users revisit chats.

4. **Database Integration:**
   - User data and chat messages are stored securely in the database.

### AWS Lambda Functions:
1. **Add Two Numbers Lambda:**
   - An AWS Lambda function that adds two numbers and returns the result.

2. **Store Documents in S3 Lambda:**
   - An AWS Lambda function to upload documents or PDFs to an S3 bucket for storage.

## Technologies Used:
- **Frontend:** HTML, CSS, JavaScript 
- **Backend:** Django (Python)
- **Database:** SQLite 
- **WebSockets:** Django Channels
- **Cloud Services:** AWS Lambda, S3
- **Version Control:** Git, GitHub

## Screenshots
![registration](https://github.com/user-attachments/assets/eac8f050-0f5d-4155-b0bd-18e17cf55baa)
![login](https://github.com/user-attachments/assets/b7aae308-0331-4319-b4a1-235cc7b7200a)
![home](https://github.com/user-attachments/assets/1f7a579b-c01d-4236-aa98-45c6913f0592)
![home2](https://github.com/user-attachments/assets/f1ed8d2e-2bb5-4284-b1eb-ef4d94505656)


## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Ravi9550/North-90-Assignment.git
   ```
2. **Go to the folder**
   ```bash
    cd ChatProject
3. **Create a virtual environment**
   ```bash
   python3 -m venv venv
3. **Activate the virtual environment**

   - For Linux/macOS
     ```bash
     source venv/bin/activate
     ```
  
   - For Windows
     ```bash
     venv\Scripts\activate
4. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
5. **Create Django project**
   ```bash
   django-admin startproject chatproject
   ```
6. **Go to project folder**
   ```bash
    cd fintrack
7. **Create a Django app**
   ```bash
   django-admin startapp chatapp
8. **Apply database migrations**
   ```bash
   python manage.py migrate
9. **Create a superuser**(for admin access)
    ```bash
    python manage.py createsuperuser
10. **Run the development server**
    ```bash
    python manage.py runserver
   
