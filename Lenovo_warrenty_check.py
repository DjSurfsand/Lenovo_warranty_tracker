import urllib.request
from bs4 import BeautifulSoup
import re

def get_warranty_status(serial_number):
    # URL for Lenovo warranty checker
    url = "https://pcsupport.lenovo.com/us/en/products/warranty-status/WarrantyStatusLookup"

    try:
        # Create a dictionary with the serial number
        data = {"sn-input-sec-nav": serial_number}

        # Send a POST request to the website
        response = urllib.request.urlopen(url, data=urllib.parse.urlencode(data).encode("utf-8"))
        html_content = response.read().decode("utf-8")

        # Extract the warranty status using BeautifulSoup
        soup = BeautifulSoup(html_content, "html.parser")
        warranty_status = soup.find("span", class_="months_remaining")

        if warranty_status:
            return warranty_status.text.strip()
        else:
            return "< im dumb, i cant find it"  # Assume < 8 months if warranty info not found
    except Exception as e:
        return f"Error fetching warranty information: {str(e)}"

def main():
    # Get serial numbers from user input (comma-separated)
    serial_numbers_input = input("Enter serial numbers (comma-separated): ")
    serial_numbers = [s.strip() for s in serial_numbers_input.split(",")]

    # Create a dictionary to store results
    warranty_results = {}

    # Retrieve warranty status for each serial number
    for serial_number in serial_numbers:
        warranty_status = get_warranty_status(serial_number)
        warranty_results[serial_number] = warranty_status

    # Print the results
    print("\nWarranty Status for Serial Numbers:")
    for serial, status in warranty_results.items():
        print(f"{serial}: {status}")

if __name__ == "__main__":
    main()
