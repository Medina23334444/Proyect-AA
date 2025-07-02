from flask import Flask, request, jsonify
from automaton import ProbabilisticDeterministicAutomaton

app = Flask(__name__)
automaton = ProbabilisticDeterministicAutomaton()

@app.route('/process', methods=['POST'])
def process_events():
    data = request.get_json(force=True)
    events = data.get('events', [])
    if not isinstance(events, list):
        return jsonify({'error': 'events must be a list'}), 400
    try:
        state, probability = automaton.process_sequence(events)
        return jsonify({
            'final_state': state,
            'probability': probability,
            'accepting': automaton.is_accepting()
        })
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
