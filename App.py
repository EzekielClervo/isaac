from flask import Flask, render_template, request, redirect, url_for
from remover import token_getter_flow, auto_post_reaction_flow, auto_comment_reaction_flow, auto_post_comment_flow, auto_follow_user_flow, auto_unfollow_user_flow, auto_share_post_flow

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/token', methods=['POST'])
def get_token():
    token_getter_flow()
    return redirect(url_for('index'))

@app.route('/post_reaction', methods=['POST'])
def post_reaction():
    auto_post_reaction_flow()
    return redirect(url_for('index'))

@app.route('/comment_reaction', methods=['POST'])
def comment_reaction():
    auto_comment_reaction_flow()
    return redirect(url_for('index'))

@app.route('/post_comment', methods=['POST'])
def post_comment():
    auto_post_comment_flow()
    return redirect(url_for('index'))

@app.route('/follow_user', methods=['POST'])
def follow_user():
    auto_follow_user_flow()
    return redirect(url_for('index'))

@app.route('/unfollow_user', methods=['POST'])
def unfollow_user():
    auto_unfollow_user_flow()
    return redirect(url_for('index'))

@app.route('/share_post', methods=['POST'])
def share_post():
    auto_share_post_flow()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
