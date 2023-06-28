# Mannor-Play

Mannor-Play is a web application that serves as a platform for users to explore upcoming and past shows performed by artists in various venues. This project aims to provide a user-friendly interface for registering artists and venues, allowing them to create and manage their profiles. Unregistered users can browse through the available venues, artists, and shows.

## Table of Contents
- [Features](#features)
- [Database Models](#database-models)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- User registration and authentication
- Creation and management of artist profiles
- Creation and management of venue profiles
- Browse upcoming and past shows
- View details of shows, including artists and venues

## Database Models

The following are the models used in the database:

1. **Users Model**
   - `email`: Email of the user
   - `password`: User password

2. **Artists Model**
   - `name`: Name of the artist
   - `social_media_links`: Social media links of the artist

3. **Venue Model**
   - `city`: City of the venue
   - `state`: State of the venue
   - Additional data needed to create a venue

4. **Show Model**
   - `venue`: Relationship with the venues table
   - `artist`: Relationship with the artists table

The `Artists` and `Venue` tables also have a relationship with the `Users` table.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/mannor-play.git

2. Navigate to the project directory:

   ```bash
   cd mannor-play

3. Initialize and activate a virtual environment

  For Linux/Mac:

   ```bash
    python -m virtualenv env
    source env/bin/activate
  
  For Windows:

    ```bash
    python -m virtualenv env
    source env/Scripts/activate

4. Install the dependencies:

   ```bash
   pip install -r requirements.txt

5. Set up the database according to your preferred database management system.

6. Configure the database connection in the project.

7. Run the development server:

    ```bash
    export FLASK_APP=myapp
    export FLASK_ENV=development # enables debug mode
    python3 app.py



## Usage

To use the Mannor-Play website, follow these steps:

1. Visit the website homepage.

2. If you are a new user, click on the "Register" button and provide the necessary details.

3. Once registered, you can log in with your credentials.

4. As a registered user, you can create artist profiles and venue profiles.

5. Browse through the available venues, artists, and shows.

6. View the details of each show, including the associated artist(s) and venue.
