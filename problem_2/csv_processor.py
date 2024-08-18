import random
import string
import hashlib
import sys

class CSVProcessor:
    def __init__(self, num_rows, output_file):
        self.num_rows = num_rows
        self.output_file = output_file

    def random_string(self, length=10):
        return ''.join(random.choices(string.ascii_letters, k=length))

    def random_date(self):
        year = random.randint(1950, 2000)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        return f"{year}-{month:02d}-{day:02d}"

    def generate_csv(self):
        """Generate a CSV file with random data."""
        with open(self.output_file, 'w') as f:
            for _ in range(self.num_rows):
                f.write(f"{self.random_string()},{self.random_string()},{self.random_string(20)},{self.random_date()}\n")

    def anonymize_csv(self):
        """Anonymize the specified columns in the CSV file.
           Really helpful for generating hashes for string values.
        """
        with open(self.output_file, 'r') as f, open(self.output_file.rsplit('.', 1)[0] + '_anonymize.csv', 'w') as outfile:
            for line in f:
                fields = line.strip().split(',')
                fields[0] = hashlib.sha256(fields[0].encode()).hexdigest()[:16]
                fields[1] = hashlib.sha256(fields[1].encode()).hexdigest()[:16]
                fields[2] = hashlib.sha256(fields[2].encode()).hexdigest()[:16]
                outfile.write(','.join(fields) + '\n')

if __name__ == "__main__":
    num_rows = int(sys.argv[1]) if len(sys.argv) > 1 else 10000000 # Generates 2GB
    output_file = sys.argv[3] if len(sys.argv) > 3 else 'output.csv'
    processor = CSVProcessor(num_rows, output_file)

    # Determine the mode based on an argument
    mode = sys.argv[2] if len(sys.argv) > 2 else "generate"

    if mode == "generate":
        processor.generate_csv()
    elif mode == "anonymize":
        processor.anonymize_csv()
