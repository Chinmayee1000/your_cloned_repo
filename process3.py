# -*- coding: utf-8 -*-
"""Process3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BmCMkWMI-VU98lzpHfriGtUlONW4kq6D
"""

Copy code
import os
import json
import csv

# Input directory containing JSON files
input_directory = "path/to/your/json/files"

# Output CSV file
output_csv_file = "transformed_data.csv"

# CSV headers
csv_headers = [
    "unit",
    "trip_id",
    "toll_loc_id_start",
    "toll_loc_id_end",
    "toll_loc_name_start",
    "toll_loc_name_end",
    "toll_system_type",
    "entry_time",
    "exit_time",
    "tag_cost",
    "cash_cost",
    "license_plate_cost",
]

# Initialize a list to store the transformed data
transformed_data = []

# Iterate through each JSON file in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith(".json"):
        file_path = os.path.join(input_directory, filename)

        # Extract data from the JSON file
        with open(file_path, "r") as json_file:
            data = json.load(json_file)

            # Extract relevant information
            unit = data.get("unit")
            trip_id = filename.replace(".json", "")
            toll_info = data.get("toll_info", [])

            # Process toll information for each toll point
            for toll_point in toll_info:
                toll_loc_id_start = toll_point.get("start", {}).get("id")
                toll_loc_id_end = toll_point.get("end", {}).get("id")
                toll_loc_name_start = toll_point.get("start", {}).get("name")
                toll_loc_name_end = toll_point.get("end", {}).get("name")
                toll_system_type = toll_point.get("system_type")
                entry_time = toll_point.get("entry_time")
                exit_time = toll_point.get("exit_time")
                tag_cost = toll_point.get("tag_cost")
                cash_cost = toll_point.get("cash_cost")
                license_plate_cost = toll_point.get("license_plate_cost")

                # Append the transformed data to the list
                transformed_data.append([
                    unit,
                    trip_id,
                    toll_loc_id_start,
                    toll_loc_id_end,
                    toll_loc_name_start,
                    toll_loc_name_end,
                    toll_system_type,
                    entry_time,
                    exit_time,
                    tag_cost,
                    cash_cost,
                    license_plate_cost,
                ])

# Write the transformed data to the CSV file
with open(output_csv_file, "w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(csv_headers)
    csv_writer.writerows(transformed_data)

print(f"Transformation completed. Data saved to {output_csv_file}")

