from fastapi import FastAPI, Query
from typing import List, Optional

app = FastAPI()

# Sample data
posts_data = [
    {"id": 1, "user_id": 1, "title": "Post 1", "status": "published"},
    {"id": 2, "user_id": 1, "title": "Post 2", "status": "draft"},
    {"id": 3, "user_id": 2, "title": "Post 3", "status": "published"},
    {"id": 4, "user_id": 1, "title": "Post 4", "status": "published"},
]

@app.get("/users/{user_id}/posts")
def get_user_posts(user_id: int, status: Optional[str] = Query(None, description="Filter by status")):
    # Filter posts by user_id
    user_posts = [post for post in posts_data if post["user_id"] == user_id]
    
    # If status query parameter is provided, filter by status
    if status:
        user_posts = [post for post in user_posts if post["status"] == status]
    
    return {"user_id": user_id, "posts": user_posts}
