# Miguel Viloria
# Assignment 6 - Regular Expressions Validation
# October 10, 2026

import re


def validate_phone(phone_number):
    # Check if phone matches standard format like 555-123-4567 or (555) 123-4567
    pattern = r"^(\(\d{3}\)|\d{3})[-.\s]?\d{3}[-.\s]?\d{4}$"
    return bool(re.match(pattern, phone_number))


def validate_ssn(ssn):
    # Check if ssn matches standard format 000-00-0000
    pattern = r"^\d{3}-\d{2}-\d{4}$"
    return bool(re.match(pattern, ssn))


def validate_zip(zip_code):
    # Check if zip code matches 5 digits or 5+4 format
    pattern = r"^\d{5}(-\d{4})?$"
    return bool(re.match(pattern, zip_code))


def main():
    print("--- Data Validation Program ---")

    # Get user inputs
    phone = input("Enter phone number (e.g., 555-123-4567): ")
    ssn = input("Enter Social Security Number (e.g., 000-00-0000): ")
    zip_c = input("Enter ZIP code (e.g., 34232 or 34232-1234): ")

    # Validate and display results
    print("\n--- Validation Results ---")
    if validate_phone(phone):
        print("Phone Number: Valid")
    else:
        print("Phone Number: Invalid")

    if validate_ssn(ssn):
        print("Social Security Number: Valid")
    else:
        print("Social Security Number: Invalid")

    if validate_zip(zip_c):
        print("ZIP Code: Valid")
    else:
        print("ZIP Code: Invalid")


if __name__ == "__main__":
    main()