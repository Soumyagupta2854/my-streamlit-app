import praw
import streamlit as st
from delete_post import delete_reddit_post
from update_post import update_reddit_post
from read_post import get_user_posts
from create_post import create_reddit_post

# Set up Reddit API client
reddit = praw.Reddit(
    client_id="ieNyn26FvRYU8Ho7pCZpLw",
    client_secret="IkH2ZRtjAfdmhwpa__ST5mQIB6SxGg",
    user_agent="script:crud:v1.0 (by u/Holiday-Box3743)",
    username="Holiday-Box3743",
    password="soumya2854"
)

# Streamlit App
def create_post():
    st.header("Create a New Post")
    
    # User input fields for creating a post
    subreddit_name = st.text_input("Enter Subreddit Name")
    title = st.text_input("Enter Title of the Post")
    content = st.text_area("Enter Content of the Post")

    if st.button("Create Post"):
        if subreddit_name and title and content:
            # Call the create post function
            result_message = create_reddit_post(subreddit_name, title, content)
            if "successfully" in result_message.lower():
                st.success(result_message)
            else:
                st.error(result_message)
        else:
            st.error("Please fill in all the fields.")

def read_posts():
    st.header("Read Your Posts")

    with st.form(key='read_form'):
        subreddit_name = st.text_input("Enter Subreddit Name (leave blank for all)")
        post_limit = st.number_input("Enter Number of Posts to Display", min_value=1, max_value=10, value=5)
        
        submit_button = st.form_submit_button(label="Show Posts")
        
        if submit_button:
            st.write(f"Fetching posts (limit: {post_limit})...")

            # Fetch posts
            posts_data = get_user_posts(subreddit_name=subreddit_name, post_limit=post_limit)

            # Check if we got posts data or a specific message
            if isinstance(posts_data, list) and posts_data:
                for post in posts_data:
                    st.write(f"**Post ID:** {post['id']}")
                    st.write(f"**Title:** {post['title']}")
                    st.write(f"**Score:** {post['score']}")
                    st.write(f"**URL:** {post['url']}")
                    st.write(f"**Content:** {post['content']}")
                    st.markdown("---")
            else:
                st.error(posts_data)

def update_post():
    st.header("Update an Existing Post")
    
    # User input fields for updating a post
    post_id = st.text_input("Enter Post ID (found in URL)")
    new_content = st.text_area("Enter New Content for the Post")

    if st.button("Update Post"):
        if post_id and new_content:
            # Call the update post function
            result_message = update_reddit_post(post_id, new_content)
            if "successfully" in result_message.lower():
                st.success(result_message)
            else:
                st.error(result_message)
        else:
            st.error("Please fill in all the fields.")

def delete_post():
    st.header("Delete a Post")
    
    # User input field for deleting a post
    post_id = st.text_input("Enter Post ID to Delete")

    if st.button("Delete Post"):
        if post_id:
            # Call the function to delete the post
            result_message = delete_reddit_post(post_id)
            if "successfully" in result_message.lower():
                st.success(result_message)
            else:
                st.error(result_message)
        else:
            st.error("Please enter a valid Post ID.")

def main():
    # Streamlit Sidebar with navigation
    st.sidebar.title("Navigation")
    app_mode = st.sidebar.selectbox("Choose a task", ["Create Post", "Read Posts", "Update Post", "Delete Post"])

    if app_mode == "Create Post":
        create_post()
    elif app_mode == "Read Posts":
        read_posts()
    elif app_mode == "Update Post":
        update_post()
    elif app_mode == "Delete Post":
        delete_post()

if __name__ == "__main__":
    main()
