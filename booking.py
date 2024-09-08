import streamlit as st

class HotelBookingSystem:  
    def __init__(self, total_rooms):  
        self.total_rooms = total_rooms  
        self.available_rooms = total_rooms.copy()  
        self.customers = {}  
  
    def add_customer(self, customer_id, customer_name, phone_number):  
        self.customers[customer_id] = {"name": customer_name, "phone_number": phone_number, 
                                       "allocated": {"Single": 0, "Double": 0}}  
  
    def show_available_rooms(self):  
        # Show available rooms  
        available_rooms_str = "\n".join([f"{room_type}: {num_rooms} available" for room_type, num_rooms in self.available_rooms.items()])
        return available_rooms_str
  
    def process_booking_request(self, customer_id, request):  
        if customer_id not in self.customers:  
            return "Customer not found."  
  
        # Check if the request is feasible  
        if not self.is_request_feasible(request):  
            return "Request denied. Not enough rooms available."  
  
        # Simulate the allocation  
        self.simulate_allocation(customer_id, request)  
  
        # Check for safe state  
        if self.is_safe_state():  
            self.approve_request(customer_id, request)  
            return "Request approved."  
        else:  
            self.deny_request(customer_id, request)  
            return "Request denied. Not enough rooms available for future requests."  
  
    def is_request_feasible(self, request):  
        for room_type, num_rooms in request.items():  
            if num_rooms > self.available_rooms[room_type]:  
                return False  
        return True  
  
    def simulate_allocation(self, customer_id, request):  
        for room_type, num_rooms in request.items():  
            self.available_rooms[room_type] -= num_rooms  
            self.customers[customer_id]["allocated"][room_type] += num_rooms  
  
    def is_safe_state(self):  
        remaining_rooms = self.available_rooms.copy()  
        for customer_info in self.customers.values():  
            for room_type, num_rooms in customer_info["allocated"].items():  
                if num_rooms > remaining_rooms[room_type]:  
                    return False  
                remaining_rooms[room_type] -= num_rooms  
        return True  
  
    def approve_request(self, customer_id, request):  
        for room_type, num_rooms in request.items():  
            self.available_rooms[room_type] -= num_rooms  
            self.customers[customer_id]["allocated"][room_type] += num_rooms  
  
    def deny_request(self, customer_id, request):  
        for room_type, num_rooms in request.items():  
            self.available_rooms[room_type] += num_rooms  
            self.customers[customer_id]["allocated"][room_type] -= num_rooms  
  
  
# Initialize Streamlit app
def main():
    st.title("Hotel Booking System with Banker's Algorithm")

    # Step 1: Initialize hotel rooms
    if 'hotel' not in st.session_state:
        st.session_state.hotel = None

    if st.session_state.hotel is None:
        st.header("Initialize Hotel Room Availability")
        total_single = st.number_input("Total Single Rooms", min_value=0, step=1)
        total_double = st.number_input("Total Double Rooms", min_value=0, step=1)
        if st.button("Initialize Hotel"):
            total_rooms = {"Single": total_single, "Double": total_double}
            st.session_state.hotel = HotelBookingSystem(total_rooms)
            st.success("Hotel initialized with room availability.")
    
    # Step 2: Add Customers
    if st.session_state.hotel:
        st.header("Customer Management")
        customer_id = st.text_input("Customer ID")
        customer_name = st.text_input("Customer Name")
        phone_number = st.text_input("Phone Number")
        if st.button("Add Customer"):
            if customer_id and customer_name and phone_number:
                st.session_state.hotel.add_customer(customer_id, customer_name, phone_number)
                st.success(f"Customer {customer_name} added.")
            else:
                st.error("Please provide valid customer information.")

        # Step 3: Process Booking Request
        st.header("Booking Request")
        selected_customer_id = st.selectbox("Select Customer ID", options=list(st.session_state.hotel.customers.keys()))
        if selected_customer_id:
            st.write("Selected Customer:", st.session_state.hotel.customers[selected_customer_id]['name'])
            
            # Show available rooms
            if st.button("Show Available Rooms"):
                available_rooms = st.session_state.hotel.show_available_rooms()
                st.info(f"Available rooms:\n{available_rooms}")
            
            # Room booking request form
            st.subheader("Request Rooms")
            request_single = st.number_input("Request Single Rooms", min_value=0, step=1)
            request_double = st.number_input("Request Double Rooms", min_value=0, step=1)

            if st.button("Submit Booking Request"):
                booking_request = {"Single": request_single, "Double": request_double}
                result = st.session_state.hotel.process_booking_request(selected_customer_id, booking_request)
                st.success(result)
    
# Run the Streamlit app
if __name__ == "__main__":
    main()
