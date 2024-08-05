import base64

def pem_to_base64(pem_file, output_file):
    with open(pem_file, 'rb') as f:
        pem_data = f.read()
        # Removing the header and footer lines of the PEM file
        pem_data = pem_data.decode().split('\n')[1:-1]
        pem_data = ''.join(pem_data)
        
        # Base64 encoding
        base64_data = base64.b64encode(pem_data.encode())
        
        # Writing base64 encoded data to the output file
        with open(output_file, 'wb') as out:
            out.write(base64_data)

if __name__ == "__main__":
    pem_file = input("Enter the path to the PEM file: ")
    output_file = input("Enter the path for the output base64 encoded file: ")
    
    pem_to_base64(pem_file, output_file)
    print("Conversion successful.")
