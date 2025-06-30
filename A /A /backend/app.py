import os
import psycopg2
import psycopg2.extras # Import for DictCursor
from flask import Flask, jsonify, request
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
# Configure CORS. For production, restrict origins to your frontend domain.
# Example: CORS(app, resources={r"/api/*": {"origins": "https://your-frontend.netlify.app"}})
# For now, allowing all for simplicity in development/testing.
CORS(app) 

def get_db_connection():
    conn = psycopg2.connect(os.environ['DATABASE_URL'])
    return conn

@app.route('/leads', methods=['POST'])
def add_lead():
    data = request.get_json()
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO leads (company_name, contact_person, organization_number, industry, website, status, summary) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id",
        (data['company_name'], data.get('contact_person'), data.get('organization_number'), data.get('industry'), data.get('website'), data['status'], data.get('summary'))
    )
    lead_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'id': lead_id, **data}), 201

@app.route('/leads', methods=['GET'])
def get_leads():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT id, company_name, contact_person, organization_number, industry, website, status, summary, created_at, updated_at FROM leads ORDER BY created_at DESC")
    leads = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([dict(lead) for lead in leads])

@app.route('/leads/<int:lead_id>', methods=['GET'])
def get_lead(lead_id):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT id, company_name, contact_person, organization_number, industry, website, status, summary, created_at, updated_at FROM leads WHERE id = %s", (lead_id,))
    lead = cur.fetchone()
    cur.close()
    conn.close()
    if lead is None:
        return jsonify({'error': 'Lead not found'}), 404
    return jsonify(dict(lead))

@app.route('/leads/<int:lead_id>', methods=['PUT'])
def update_lead(lead_id):
    data = request.get_json()
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE leads SET company_name = %s, contact_person = %s, organization_number = %s, industry = %s, website = %s, status = %s, summary = %s WHERE id = %s",
        (data['company_name'], data.get('contact_person'), data.get('organization_number'), data.get('industry'), data.get('website'), data['status'], data.get('summary'), lead_id)
    )
    updated_rows = cur.rowcount
    conn.commit()
    cur.close()
    conn.close()
    if updated_rows == 0:
        return jsonify({'error': 'Lead not found'}), 404
    return jsonify({'message': 'Lead updated successfully'})

@app.route('/leads/<int:lead_id>', methods=['DELETE'])
def delete_lead(lead_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM leads WHERE id = %s", (lead_id,))
    deleted_rows = cur.rowcount
    conn.commit()
    cur.close()
    conn.close()
    if deleted_rows == 0:
        return jsonify({'error': 'Lead not found'}), 404
    return jsonify({'message': 'Lead deleted successfully'})

@app.route('/leads/<int:lead_id>/notes', methods=['POST'])
def add_note_to_lead(lead_id):
    data = request.get_json()
    if not data or 'note' not in data:
        return jsonify({'error': 'Note content is required'}), 400

    conn = get_db_connection()
    cur = conn.cursor()
    # Check if lead exists
    cur.execute("SELECT id FROM leads WHERE id = %s", (lead_id,))
    if cur.fetchone() is None:
        cur.close()
        conn.close()
        return jsonify({'error': 'Lead not found'}), 404

    cur.execute(
        "INSERT INTO notes (lead_id, note) VALUES (%s, %s) RETURNING id, created_at",
        (lead_id, data['note'])
    )
    note_id, created_at = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'id': note_id, 'lead_id': lead_id, 'note': data['note'], 'created_at': created_at}), 201

@app.route('/leads/<int:lead_id>/notes', methods=['GET'])
def get_lead_notes(lead_id):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    # Check if lead exists
    cur.execute("SELECT id FROM leads WHERE id = %s", (lead_id,))
    if cur.fetchone() is None:
        cur.close()
        conn.close()
        return jsonify({'error': 'Lead not found'}), 404

    cur.execute("SELECT id, note, created_at FROM notes WHERE lead_id = %s ORDER BY created_at DESC", (lead_id,))
    notes = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([dict(note) for note in notes])

if __name__ == '__main__':
    # It's good practice to make the port configurable
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
