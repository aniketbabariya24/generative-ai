import React, { useState } from 'react';
import './styles/App.css';
import PostForm from './components/PostForm';
import PostList from './components/PostList';

const App = () => {
  const [posts, setPosts] = useState([]);

  const handlePostCreate = (newPost) => {
    setPosts([...posts, newPost]);
  };

  const handlePostDelete = (postToDelete) => {
    setPosts(posts.filter((post) => post !== postToDelete));
  };

  const handlePostLike = (postToLike) => {
    setPosts(
      posts.map((post) =>
        post === postToLike ? { ...post, likes: post.likes + 1 } : post
      )
    );
  };

  const handlePostComment = (post, comment) => {
    setPosts(
      posts.map((p) =>
        p === post ? { ...p, comments: [...p.comments, comment] } : p
      )
    );
  };

  return (
    <div className="App">
      <h1>Instagram App</h1>
      <PostForm onPostCreate={handlePostCreate} />
      <PostList
        posts={posts}
        onDelete={handlePostDelete}
        onLike={handlePostLike}
        onComment={handlePostComment}
      />
    </div>
  );
};

export default App;
