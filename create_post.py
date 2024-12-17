import praw

# Set up Reddit API client
reddit = praw.Reddit(
    client_id="ieNyn26FvRYU8Ho7pCZpLw",
    client_secret="IkH2ZRtjAfdmhwpa__ST5mQIB6SxGg",
    user_agent="script:crud:v1.0 (by u/Holiday-Box3743)",
    username="Holiday-Box3743",
    password="soumya2854"
)

# Create a post with user input
def create_reddit_post(subreddit_name, title, content):
    try:
        # Make the post
        subreddit = reddit.subreddit(subreddit_name)
        
        # Submit the post and store the result
        submission = subreddit.submit(title, selftext=content)
        
        # Print the post ID
        print(f"Post created successfully! Post ID: {submission.id}")
        return f"Post created successfully! Post ID: {submission.id}"
    
    except praw.exceptions.PRAWException as e:
        print(f"Error: {e}")
        return "Subreddit not valid or other PRAW exception occurred."


