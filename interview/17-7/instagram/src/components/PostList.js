import React from 'react';
import Post from './Post';

const PostList = ({ posts, onDelete, onLike, onComment }) => {
  return (
    <div>
      {posts.map((post, index) => (
        <Post
          key={index}
          post={post}
          onDelete={onDelete}
          onLike={onLike}
          onComment={onComment}
        />
      ))}
    </div>
  );
};

export default PostList;
