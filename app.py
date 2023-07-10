from flask import Flask,request,jsonify


posts = {

}


app = Flask(__name__)


@app.route("/add-post",methods=["POST"])
def add_post():
          post_id = request.json['post_id']
          user_name = request.json['user_name']
          caption = request.json['caption']

          posts[post_id] = {
                    user_name:user_name,
                    caption :caption
          }
          return jsonify({'msg':"post added successfully"})



# get all the posts
@app.route("/get-post",methods=["GET"])
def get_posts():
          return jsonify(posts)



# delete a post
@app.route("/delete-post/<post_id>",methods=['DELETE'])
def deletePost(post_id):
         post_id = int(post_id)
         del posts['post_id']
         return jsonify({'msg:':"post deleted!"})
          







if(__name__) == "__main__":
          app.run(debug=True)