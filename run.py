from diabetes_ai import create_app

app = create_app()

if __name__ == '__main__':
    # Increase security by turning off debug in real production, 
    # but keep it on for now as per dev requirements.
    app.run(debug=True, host='0.0.0.0', port=8000)
