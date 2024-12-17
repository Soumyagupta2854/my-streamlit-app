import streamlit as st
import requests

# Telegram Bot API setup
BOT_TOKEN = "7901217182:AAFNZSo0fIgM6ypMPzkVpcD2a74SPq8rY2s"
CHAT_ID = "@crudtelegram"  # Replace with your Telegram chat ID
BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

# Initialize session state for messages log
if "messages_log" not in st.session_state:
    st.session_state["messages_log"] = []

# Streamlit app
def main():
    st.title("Telegram Bot Manager")
    st.sidebar.header("Telegram Bot Actions")
    
    # Dropdown for actions
    actions = {
        "Create Post": create_post,
        "Read Posts": read_posts,
        "Update Post": update_post,
        "Delete Post": delete_post,
    }
    action = st.sidebar.selectbox("Choose an Action", list(actions.keys()))
    
    # Call the respective function
    actions[action]()

def create_post():
    """Function to create a new post"""
    st.header("Create a New Post")
    message = st.text_area("Enter your message:")
    if st.button("Send Message"):
        if message:
            response = requests.post(f"{BASE_URL}/sendMessage", data={
                "chat_id": CHAT_ID,
                "text": message
            })
            if response.status_code == 200:
                response_data = response.json()
                message_id = response_data.get("result", {}).get("message_id")
                if message_id:
                    # Append to the session state log
                    st.session_state["messages_log"].append({"message_id": message_id, "text": message})
                    st.success(f"Message sent successfully! Message ID: {message_id}")
                else:
                    st.warning("Message sent but could not retrieve Message ID.")
            else:
                st.error(f"Failed to send message: {response.json()}")

def read_posts():
    """Function to read previously sent posts"""
    st.header("Read Sent Posts")
    if st.session_state["messages_log"]:
        for msg in st.session_state["messages_log"]:
            st.write(f"Message ID: {msg['message_id']}")
            st.write(f"Text: {msg['text']}")
            st.write("---")
    else:
        st.info("No messages have been logged yet.")

def update_post():
    """Function to update a post"""
    st.header("Update a Post")
    message_id = st.number_input("Enter the Message ID to update:", min_value=1, step=1)
    new_message = st.text_area("Enter the new message:")
    if st.button("Update Message"):
        if new_message:
            response = requests.post(f"{BASE_URL}/editMessageText", data={
                "chat_id": CHAT_ID,
                "message_id": message_id,
                "text": new_message
            })
            if response.status_code == 200:
                st.success("Message updated successfully!")
                # Update the log
                for msg in st.session_state["messages_log"]:
                    if msg["message_id"] == message_id:
                        msg["text"] = new_message
                        break
            else:
                st.error(f"Failed to update message: {response.json()}")

def delete_post():
    """Function to delete a post"""
    st.header("Delete a Post")
    message_id = st.number_input("Enter the Message ID to delete:", min_value=1, step=1)
    if st.button("Delete Message"):
        response = requests.post(f"{BASE_URL}/deleteMessage", data={
            "chat_id": CHAT_ID,
            "message_id": message_id
        })
        if response.status_code == 200:
            st.success("Message deleted successfully!")
            # Remove from the log
            st.session_state["messages_log"] = [
                msg for msg in st.session_state["messages_log"]
                if msg["message_id"] != message_id
            ]
        else:
            st.error(f"Failed to delete message: {response.json()}")

if __name__ == "__main__":
    main()
