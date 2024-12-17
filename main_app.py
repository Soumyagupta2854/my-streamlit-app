import streamlit as st
import mastadoncrud  
import app  
import app_telegram  

# Main function
def main():
    st.title("Multi-Platform Post Management App")

    # Sidebar menu for navigation
    menu = ["Telegram", "Reddit", "Mastadon", "Exit"]
    choice = st.sidebar.selectbox("Choose a social media platform", menu)

    # Telegram Post Management
    if choice == "Telegram":
        
        app_telegram.main()  

    # Reddit Post Management
    elif choice == "Reddit":
        st.header("Reddit Post Management App")
        app.main()  # Call the main function from app.py

    
    elif choice == "Mastadon":
        st.header("Mastadon Bot Control Panel")
        mastadoncrud.main()  

    # Exit
    elif choice == "Exit":
        st.write("Exiting the program.")

# Run the app
if __name__ == "__main__":
    main()
