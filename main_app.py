import streamlit as st
import facebook_app  # Import facebook_app.py
import app  # Import app.py
import run  # Import run.py

# Main function
def main():
    st.title("Multi-Platform Post Management App")

    # Sidebar menu for navigation
    menu = ["Facebook", "Reddit", "Discord", "Exit"]
    choice = st.sidebar.selectbox("Choose an operation", menu)

    # Facebook Post Management
    if choice == "Facebook":
        st.header("Facebook Post Management App")
        facebook_app.main()  # Call the main function from facebook_app.py

    # Reddit Post Management
    elif choice == "Reddit":
        st.header("Reddit Post Management App")
        app.main()  # Call the main function from app.py

    # Discord Message Management
    elif choice == "Discord":
        st.header("Discord Bot Control Panel")
        run.main()  # Call the main function from run.py

    # Exit
    elif choice == "Exit":
        st.write("Exiting the program.")

# Run the app
if __name__ == "__main__":
    main()
