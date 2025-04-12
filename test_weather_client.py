import pytest
import requests
import datetime
from unittest.mock import Mock
from weather_client import get_weather_data, get_current_weather, get_weather_forecast

# Add fixtures
@pytest.fixture
def mock_weather_response():
    """Mock response for current weather data to avoid API Call."""
    return {
        "name": "Ogbomoso",
        "main": {"temp": 30, "humidity": 80},
        "weather": [{"description": "clear sky"}],
        "wind": {"speed": 2.5}
    }

@pytest.fixture
def mock_forecast_response():
    """Mock response for weather forecast data to avoid API call."""
    return {
        "city": {"name": "Ogbomoso"},
        "list": [
            {
                "dt_txt": "2025-04-09 12:00:00",
                "main": {"temp": 28},
                "weather": [{"description": "light rain"}]
            },
            {
                "dt_txt": "2025-04-10 12:00:00",
                "main": {"temp": 27},
                "weather": [{"description": "cloudy"}]
            }
        ]
    }

# Testing for successful response
def test_get_weather_data_success(mock_weather_response):
    """Test successful fetching of data."""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = mock_weather_response

    data = get_weather_data(mock_response, "Ogbomoso")
    assert data is not None
    assert data["name"] == "Ogbomoso"
    assert data["main"]["temp"] == 30
    assert data["weather"][0]["description"] == "clear sky"

def test_get_weather_data_failure():
    """Test failure when user input a non-existing city."""
    mock_response = Mock()
    mock_response.status_code = 404
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Client Error")

    data = get_weather_data(mock_response, "noplace222")
    assert data is None

# Test forecast
def test_get_weather_forecast(mock_forecast_response):
    """Test fetching weather forecast."""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = mock_forecast_response

    data = get_weather_data(mock_response, "Ogbomoso")
    assert data["city"]["name"] == "Ogbomoso"
    assert len(data["list"]) > 0 # Testing to ensure list is not empty
    assert "dt_txt" in data["list"][0] # Testing to ensure forecast contains timestamp
    assert "main" in data["list"][0] # Testing if temperature details are present
    assert "weather" in data["list"][0] # Testing if other weather conditions are displayed in the forecast
