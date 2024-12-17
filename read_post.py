import praw
from prawcore.exceptions import Redirect, NotFound, Forbidden

# Initialize Reddit API client
reddit = praw.Reddit(
    client_id="ieNyn26FvRYU8Ho7pCZpLw",
    client_secret="IkH2ZRtjAfdmhwpa__ST5mQIB6SxGg",
    user_agent="script:crud:v1.0 (by u/Holiday-Box3743)",
    username="Holiday-Box3743",
    password="soumya2854"
)

def get_user_posts(subreddit_name=None, post_limit=5):
    try:
        # If a subreddit name is provided, validate it
        if subreddit_name:
            subreddit = reddit.subreddit(subreddit_name)
            subreddit._fetch()  # Explicitly fetch subreddit details to trigger any exceptions
            
        # Fetch user posts
        user = reddit.user.me()
        user_posts = user.submissions.new(limit=post_limit)
        
        posts_data = []
        count = 0

        for post in user_posts:
            # Filter by subreddit if specified
            if subreddit_name and post.subreddit.display_name.lower() != subreddit_name.lower():
                continue
            
            count += 1
            posts_data.append({
                'id': post.id,  # Include the post ID
                'title': post.title,
                'score': post.score,
                'url': post.url,
                'content': post.selftext[:200]  # Truncate content for brevity
            })

        # Handle case where no posts are found for the subreddit
        if count == 0 and subreddit_name:
            return f"No posts found in subreddit '{subreddit_name}'."

        return posts_data

    except Redirect:  # Handle invalid subreddit names
        return f"Subreddit '{subreddit_name}' does not exist."
    except NotFound:  # Handle any additional "not found" errors
        return f"Subreddit '{subreddit_name}' does not exist."
    except Forbidden:  # Handle private or restricted subreddits
        return f"Subreddit '{subreddit_name}' is private or restricted."
    except Exception as e:  # General exception handling
        return f"An error occurred: {str(e)}"

# Example Usage
if __name__ == "__main__":
    # Fetch user's posts without subreddit filter
    print("Fetching all posts:")
    posts = get_user_posts(post_limit=5)
    for post in posts:
        print(post)

    # Fetch user's posts from a specific subreddit
    subreddit_name = "learnpython"
    print(f"\nFetching posts from subreddit '{subreddit_name}':")
    posts_from_sub = get_user_posts(subreddit_name=subreddit_name, post_limit=5)
    print(posts_from_sub)
