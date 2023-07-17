import React, { useState } from 'react';

const PostForm = ({ onPostCreate }) => {
  const [username, setUsername] = useState('');
  const [caption, setCaption] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    const newPost = {
      username,
      caption,
      likes: 0,
      comments: [],
    };
    onPostCreate(newPost);
    setUsername('');
    setCaption('');
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Username"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />
      <input
        type="text"
        placeholder="Caption"
        value={caption}
        onChange={(e) => setCaption(e.target.value)}
      />
      <button type="submit">Create Post</button>
    </form>
  );
};

export default PostForm;
