import praw

# Set up Reddit API client
reddit = praw.Reddit(
    client_id="ieNyn26FvRYU8Ho7pCZpLw",
    client_secret="IkH2ZRtjAfdmhwpa__ST5mQIB6SxGg",
    user_agent="script:crud:v1.0 (by u/Holiday-Box3743)",
    username="Holiday-Box3743",
    password="soumya2854"
)

# Function to delete a Reddit post
def delete_reddit_post(post_id):
    try:
        # Fetch the post by ID
        post = reddit.submission(id=post_id)
        
        # Check if the post exists (author will be None if post doesn't exist)
        if post.author is None:
            return "The post does not exist or has already been deleted."

        # Check if the authenticated user is the author
        if post.author.name != reddit.user.me().name:
            return "You can only delete posts that you have created."
        
        # Delete the post
        post.delete()
        return "Post deleted successfully!"
    
    except Exception as e:
        return f"An error occurred: {e}"



