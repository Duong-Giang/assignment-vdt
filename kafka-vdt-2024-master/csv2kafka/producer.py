import csv
from kafka import KafkaProducer
import json

# Kafka producer configuration
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092', 'localhost:9094'],
    value_serializer=lambda v: v.encode('utf-8')
)

data_path = '../data/log_action.csv'

# Open the CSV file for reading
with open(data_path, 'r') as csvfile:
    reader = csv.reader(csvfile)

    # Skip the first row (header)
    #next(reader)

    # Process each data row
    for row in reader:
        # Create a dictionary with meaningful keys
        data = {
            
            "student_code": int(row[0]),  # Assuming "write" is in the second column
            "activity": row[1],  # Assuming "7" is the count
            "numberOfFile": int(row[2]),
            "timestamp": row[3]  # Assuming "6/10/2024" is the date
        }

        # Convert the dictionary to JSON
        data_json = json.dumps(data)

        # Send the JSON data to Kafka topic
        producer.send('vdt2024', value=data_json)

# Close the producer connection
producer.close()

