from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from models import Base, engine, SessionLocal, User, Post

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a new user
@app.post("/users/")
def create_user(name: str, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.name == name).first()
    if db_user:
        raise HTTPException(status_code=400, detail="User already exists")
    new_user = User(name=name)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Create a new post
@app.post("/posts/")
def create_post(user_id: int, title: str, status: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    new_post = Post(user_id=user_id, title=title, status=status)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

# Get posts by user, optional status filter
@app.get("/users/{user_id}/posts")
def get_user_posts(user_id: int, status: str = Query(None), db: Session = Depends(get_db)):
    posts = db.query(Post).filter(Post.user_id == user_id)
    if status:
        posts = posts.filter(Post.status == status)
    return {"user_id": user_id, "posts": [ {"id": p.id, "title": p.title, "status": p.status} for p in posts ]}
