from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash
from app.data.db import get_db_connection

user_blueprint = Blueprint('user', __name__)

# User Login
@user_blueprint.route('/login', methods=['POST'])
def login_user():
    connection = None
    try:
        # Get data from the incoming JSON request
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        # Validate required fields
        if not username or not password:
            return jsonify({"error": "Username and password are required"}), 400

        connection = get_db_connection()
        cursor = connection.cursor()

        # Check if the username exists
        cursor.execute("SELECT uid, password FROM public.user WHERE username = %s", (username,))
        user = cursor.fetchone()

        if user:
            user_id = user['uid']
            plain_password = user['password']

            # Verify the password
            if plain_password == password:
                # Successful login
                return jsonify({"message": "Login successful", "uid": user_id}), 200
            else:
                return jsonify({"error": "Invalid password"}), 401
        else:
            return jsonify({"error": "User not found"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        if connection:
            cursor.close()
            connection.close()

@user_blueprint.route('/register', methods=['POST'])
def register_user():
    connection = None
    try:
        # Get data from the incoming JSON request
        data = request.get_json()
        full_name = data.get('full_name')
        username = data.get('username')
        email = data.get('email')
        phone_num = data.get('phone_num')
        plain_password = data.get('password')

        # Validate required fields
        if not full_name or not username or not email or not phone_num or not plain_password:
            return jsonify({"error": "All fields are required"}), 400

        # Connect to the database
        connection = get_db_connection()
        cursor = connection.cursor()

        # Check if the username already exists
        cursor.execute("SELECT * FROM public.user WHERE username = %s", (username,))
        if cursor.fetchone():
            return jsonify({"error": "Username already exists"}), 400
        
        # Check if the email already exists
        cursor.execute("SELECT * FROM public.user WHERE email = %s", (email,))
        if cursor.fetchone():
            return jsonify({"error": "Email already exists"}), 400

        # Insert the new user into the database
        cursor.execute(
            "INSERT INTO public.user (full_name, username, email, phone_num, password) "
            "VALUES (%s, %s, %s, %s, %s) RETURNING uid",
            (full_name, username, email, phone_num, plain_password)
        )

        # Fetch the inserted user ID
        user_id = cursor.fetchone()

        if user_id:
            user_id = user_id['uid']
            connection.commit()  # Commit the transaction
            print(f"User registered successfully with user_id: {user_id}")
            return jsonify({"message": "User registered successfully", "uid": user_id}), 201
        else:
            raise Exception("Failed to fetch user_id after insert")

    except Exception as e:
        # Log and return the error details
        print(f"Error occurred: {str(e)}")
        if connection:
            connection.rollback()  # Rollback any failed transaction
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

    finally:
        if connection:
            cursor.close()
            connection.close()