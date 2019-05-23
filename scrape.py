import os


"""
    Parse CSV File to a JSON file helper function
"""
def csv_to_json(csvname, fieldnames, jsonfilename): 
    import csv  
    import json 
    # Open the CSV  
    f = open(csvname, 'rU' )  
    # Change each fieldname to the appropriate field name. I know, so difficult.  
    reader = csv.DictReader( f, fieldnames)  
    # Parse the CSV into JSON  
    out = json.dumps( [ row for row in reader ] )  
    # Save the JSON  
    f = open( jsonfilename, 'w')  
    f.write(out)  


def split(filehandler, delimiter=',', row_limit=10000, 
    output_name_template='output_%s.csv', output_path='.', keep_headers=True):
    """
    Splits a CSV file into multiple pieces.
    
    A quick bastardization of the Python CSV library.
    Arguments:
        `row_limit`: The number of rows you want in each output file. 10,000 by default.
        `output_name_template`: A %s-style template for the numbered output files.
        `output_path`: Where to stick the output files.
        `keep_headers`: Whether or not to print the headers in each output file. 
    """
    import csv
    reader = csv.reader(filehandler, delimiter=delimiter)
    current_piece = 1
    current_out_path = os.path.join(
         output_path,
         output_name_template  % current_piece
    )
    current_out_writer = csv.writer(open(current_out_path, 'w'), delimiter=delimiter)
    current_limit = row_limit
    if keep_headers:
        headers = reader.next()
        current_out_writer.writerow(headers)
    current_time = 0
    write = 0
    for i, row in enumerate(reader):
        if (int(row[1]) - current_time > 86400 and row[2] == "gspc"):
            current_time = int(row[1])
            write += 1
            if write > current_limit:
                current_piece += 1
                current_limit = row_limit * current_piece
                current_out_path = os.path.join(
                output_path,
                output_name_template  % current_piece
                )
                current_out_writer = csv.writer(open(current_out_path, 'w'), delimiter=delimiter)
                if keep_headers:
                    current_out_writer.writerow(headers)
            current_out_writer.writerow(row)
    print(d.keys)

split(open("stocks_sentdex_1-6-2016.csv", 'r'), delimiter=',', row_limit=100000)
