# Weather API Client

This is a simple weather forecast application built with python programming that provides current  and future weather conditions. The Application can provide a 5 day forecast for  specified locations entered by users.

## Features

* **Current Weather:** Displays temperature, weather description, humidity, wind speed, and other relevant information for the user-entered location.
* **5-Day Weather Forecast:** Provides a forecast for several upcoming days, including daily high and low temperatures, and general weather conditions.
* **API Integration:** Uses a weather API (OpenWeatherMap) to fetch real-time weather data.

## Technologies Used

* **Python 3.13**
* **OpenWeather API** 
* **Pytest**
  
## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Data-Epic/Adenike-Awotunde-weather-api.git
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd Weaather_API_Integration
    ```
3.  **Install dependencies:**
    ~~~
        pip install -r requirements.txt
        ```

4.  **Obtain an API key:**
    * Sign up for an account on OpenWeatherMap 
    * Obtain your API key.
    * Add your API key to the `.env` file:
        ```
        API_KEY=[your_api_key]
        ```
   
6.  **Run the application:**
        ```bash
        weaher_client_.py 
        ```


## Usage

1.  Enter the desired location (city name), multiple locations can be entered using comma as the separator
2.  The application will display the current weather and forecast for the specified location.



### Future Improvements
- Creating a user friendly interface using Frontend Framework like streamlit
- Implementing interactive elements for location selection, data visualization, and settings.
- Ensuring responsiveness across various devices and screen sizes.

### Author
Adenike Awotunde 
- LinkedIn: https://www.linkedin.com/in/adenike-awotunde-b9740b80
- Email: adenikeisblessed@gmail.com

