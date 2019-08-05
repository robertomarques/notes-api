from flask import Flask, request, Response
import notesrepo

app = Flask(__name__)


@app.route('/', methods=['POST'])
def notes_create():
    note = request.json
    post_id = notesrepo.notes_create(note)
    resp = Response(status=201, mimetype='application/json')
    resp.headers['Location'] = f'http://localhost:5000/{post_id}'
    return resp

'''
@app.route('/', methods=['PUT'])
def notes_update(note)
    notesrepo.update(note)

@app.route('/<int:note_id>', methods=['GET'])
def notes_find(note_id)
    notesrepo.update(note_id)

@app.route('/<int:note_id>', methods=['DELETE'])
def notes_del(note_id)
    notesrepo.delete(note_id)

'''

if __name__ == "__main__":
	app.run()