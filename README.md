# Hotel Booking System with Banker's Algorithm

This project implements a **Hotel Booking System** using the **Banker's Algorithm** to manage room allocations while preventing resource deadlock. The system allows customers to request hotel rooms of different types and ensures that room allocations leave enough resources available for future customer requests, maintaining a safe state.

## Features

- Initialize hotel room availability for `Single` and `Double` room types.
- Add customers with basic details (Customer ID, Name, Phone Number).
- Process room booking requests using the Banker's Algorithm to ensure a safe allocation state.
- View available rooms at any time.
- Prevent over-allocation of rooms to avoid deadlock scenarios.

## Tech Stack

- **Python**
- **Streamlit**: Provides an interactive UI to manage the booking system.

## How It Works

1. **Initialize Hotel**: Define the total number of `Single` and `Double` rooms available in the hotel.
2. **Add Customers**: Add customer details like Customer ID, Name, and Phone Number.
3. **Process Booking Requests**: Allow customers to request rooms. The system checks whether the request is feasible and allocates the rooms if it's safe to do so.
4. **View Available Rooms**: At any point, the user can check the current availability of rooms.

The Banker's Algorithm is used to simulate and manage resource allocation (hotel rooms) to ensure that there will always be enough rooms to satisfy future customer requests.

## Prerequisites

Make sure you have the following installed:

- Python 3.x
- Streamlit (`pip install streamlit`)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/hotel-booking-system.git
   cd hotel-booking-system
   ```

2. Install the required dependencies:
   ```bash
   pip install streamlit
   ```

## Running the Application

1. Run the Streamlit app:
   ```bash
   streamlit run hotel_booking_streamlit.py
   ```

2. Open the URL provided by Streamlit in your browser (usually `http://localhost:8501`).

## Project Structure
```
hotel-booking-system/
│
├── hotel_booking_streamlit.py   # Main application code
├── README.md                    # Project documentation
└── requirements.txt             # Dependencies (optional)
```

## Future Enhancements

- Add room types dynamically.
- Support for booking history and cancellations.
- Integration with a database to persist customer and booking information.
