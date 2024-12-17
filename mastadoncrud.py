import streamlit as st
from mastodon import Mastodon
from bs4 import BeautifulSoup

# Initialize Mastodon API with the provided credentials
mastodon = Mastodon(
    client_id='0HTYvCvqtuSRdAbgRB57056S3hMTwTZwjW890M5tvgU',
    client_secret='_O5G_5dYG_5N_cCuXcmSm3xraxR5ZWS_XGWCyJ09TgU',
    access_token='J1HUR2REEaAfp-_qRHCmQ24OlpwjsiMJiuSVdreKxzg',
    api_base_url='https://mastodon.social'  # Replace with your instance URL if different
)

# Function to clean HTML tags from a string
def clean_html(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    return soup.get_text()

# Streamlit Sidebar for selecting actions
st.sidebar.title("Mastodon Post Manager")
action = st.sidebar.radio("Choose Action", ['Post a Message', 'Read Posts', 'Update Post', 'Delete Post'])

if action == 'Post a Message':
    st.title("Post a Message to Mastodon")
    message = st.text_area("Enter your message:")
    
    if st.button("Post"):
        if message:
            cleaned_message = clean_html(message)  # Clean the message to remove HTML tags
            posted = mastodon.status_post(cleaned_message)
            post_id = posted['id']  # Get the post ID from the response
            post_url = f"https://mastodon.social/@{posted['account']['username']}/{post_id}"  # Link to the post
            st.success(f"Your post has been published on Mastodon! Post ID: {post_id}")
            st.markdown(f"[Click here to view the post]({post_url})")
        else:
            st.error("Please enter a message to post.")

elif action == 'Read Posts':
    st.title("Read Previous Posts")
    num_posts = st.number_input("Enter the number of posts to read:", min_value=1, max_value=100, value=5)
    
    if st.button("Read Posts"):
        statuses = mastodon.timeline_home(limit=num_posts)
        if statuses:
            for status in statuses:
                cleaned_content = clean_html(status['content'])  # Clean the HTML content
                post_url = f"https://mastodon.social/@{status['account']['username']}/{status['id']}"  # Link to the post
                st.markdown(f"**ID**: {status['id']}")
                st.markdown(f"**Text**: {cleaned_content}")
                st.markdown(f"[Click here to view the post]({post_url})")
                st.markdown("---")  # Add a line break between posts
        else:
            st.warning("No posts found!")

elif action == 'Update Post':
    st.title("Update an Existing Post")
    post_id = st.text_input("Enter the Post ID to update:")
    updated_message = st.text_area("Enter the new message:")
    
    if st.button("Update Post"):
        if post_id and updated_message:
            try:
                # Delete the original post
                mastodon.status_delete(post_id)
                st.success(f"Post ID {post_id} has been deleted.")
                
                # Create a new post with the updated message
                new_post = mastodon.status_post(updated_message)
                new_post_id = new_post['id']  # Get the new post ID
                post_url = f"https://mastodon.social/@{new_post['account']['username']}/{new_post_id}"  # Link to the new post
                st.success(f"Your post has been updated! New Post ID: {new_post_id}")
                st.markdown(f"[Click here to view the new post]({post_url})")
            except Exception as e:
                st.error(f"Error updating post: {e}")
        else:
            st.error("Please provide both post ID and updated message.")

elif action == 'Delete Post':
    st.title("Delete a Post")
    post_id_to_delete = st.text_input("Enter the Post ID to delete:")
    
    if st.button("Delete Post"):
        if post_id_to_delete:
            try:
                mastodon.status_delete(post_id_to_delete)
                st.success("Your post has been deleted!")
            except Exception as e:
                st.error(f"Error deleting post: {e}")
        else:
            st.error("Please provide the post ID to delete.")
