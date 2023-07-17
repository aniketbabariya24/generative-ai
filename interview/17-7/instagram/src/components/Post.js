import React from 'react';

const Post = ({ post, onDelete, onLike, onComment }) => {
  const handleDelete = () => {
    onDelete(post);
  };

  const handleLike = () => {
    onLike(post);
  };

  const handleCommentSubmit = (e) => {
    e.preventDefault();
    const comment = e.target.comment.value;
    onComment(post, comment);
    e.target.comment.value = '';
  };

  return (
    <div>
      <h3>{post.username}</h3>
      <p>{post.caption}</p>
      <p>Likes: {post.likes}</p>
      <button onClick={handleDelete}>Delete</button>
      <button onClick={handleLike}>Like</button>
      <div>
        {post.comments.map((comment, index) => (
          <p key={index}>{comment}</p>
        ))}
      </div>
      <form onSubmit={handleCommentSubmit}>
        <input type="text" name="comment" placeholder="Add a comment" />
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default Post;
