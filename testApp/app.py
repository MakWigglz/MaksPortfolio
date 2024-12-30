from flask import Flask, render_template, jsonify
from pyClassesAndSets import Topics_of_study

app = Flask(__name__)

topics = Topics_of_study()
topics.add_item("Science", "Physics", "Chemistry", "Biology", "Mathematics")
topics.add_item("History", "Ancient civilizations", "Modern history")
topics.add_item("Art", "Painting", "Sculpture", "Architecture")
topics.add_item("Technology", "Computer Science", "Artificial Intelligence", "Robotics")
topics.add_item("Philosophy", "Ethics", "Metaphysics", "Epistemology")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/subtopics/<topic>')
def get_subtopics(topic):
    return jsonfy(topics.get_items(topic))

@app.route('/content/<topic>/<subtopic>')
def get_content(topic, subtopic):
    #this is a placeholder, replace with actual content retrieval logic.
    return jsonfy({"content": f"This is the content {subtopic} in {topic}."})

if __name__ == '__main__':
    app.run(debug=True)
