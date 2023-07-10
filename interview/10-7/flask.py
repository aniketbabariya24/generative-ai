from flask import Flask
app= Flask(__name__)

post=[]

# CREATING POST  
@app.route('/createpost', methods=['POST'])
def createPost():
    id=1
    username="Provide Username"
    caption="Provide caption"
    likes=0
    comments=[]

    myPost={id:id,username:username, caption:caption, likes:likes, comments:comments}
    post.append(myPost)
    return "Post created successfully"

# VIEW POSTS 
@app.route('/viewpost', methods=['GET'])
def viewPost():
    return post

# DELETE POST 
@app.route('/deletepost/<postId>', methods=['DELETE'])
def viewPost(postId):
    for i in post:
        if i.id==postId:
            post.remove()
            return "Post is deleted" 
    
    return "ERROR: Id is not Found"
    
             

# LIKE POST              
@app.route('/likepost/<postId>', methods=['DELETE'])
def viewPost(postId):
    for i in post:
        if i.id==postId:
            i.likes=i.likes+1
            return "Post is Liked" 

    return "ERROR: Id is not Found"           
   

# COMMENT POST    
@app.route('/commentpost/<postId>', methods=['DELETE'])
def viewPost(postId):
    yourComment="Provide your comment"
    for i in post:
        if i.id==postId:
            i.comments.append(yourComment)
            return "Post is Liked" 

    return "ERROR: Id is not Found"              

if __name__ == '__main__':
    app.run(debug=True)