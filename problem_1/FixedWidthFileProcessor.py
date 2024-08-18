import json

class FixedWidthFileProcessor:
    def __init__(self, spec):
        self.offsets = list(map(int, spec["Offsets"]))
        self.column_names = spec["ColumnNames"]
        self.fixed_width_encoding = spec["FixedWidthEncoding"]
        self.delimited_encoding = spec["DelimitedEncoding"]
        self.includes_header = eval(spec["IncludeHeader"])

    def generate_fixed_width_file(self, output_file):
        # specify columns
        columns = tuple(map(tuple, zip(self.column_names, list(map(int, self.offsets)))))
        
        # write file to populate values
        with open('fixed_width_text.txt', 'w', encoding=self.fixed_width_encoding) as f:
            f.write(''.join([(field_name).ljust(width, '*') for field_name, width in columns]))

    def parse_fixed_width_file(self, input_file, output_file):
        with open(input_file, 'r', encoding=self.fixed_width_encoding) as f, open(output_file, 'w', newline='', encoding=self.delimited_encoding) as csvfile:
            if self.includes_header:
                csvfile.write(','.join(map(str, self.column_names)) + '\n')

            for line in f:
                start = 0
                row = []
                for offset in self.offsets:
                    row.append(line[start:start+offset])
                    start += offset
                csvfile.write(','.join(map(str, row)) + '\n')


with open('spec.json', 'r') as spec:
    spec_data = json.load(spec)
parser = FixedWidthFileProcessor(spec_data)
parser.generate_fixed_width_file('fixed_width_text.txt')
parser.parse_fixed_width_file('fixed_width_text.txt', 'parsed_output.csv')
