from flask import Blueprint, render_template, request, jsonify
from .models import Sample
from . import db

from io import StringIO
import json

import pandas as pd

api = Blueprint('api', __name__)

@api.route('/api', methods=['GET', 'POST'])
def sample_api():
    """
        Sample API

        Parameters:
        url route
        methods: GET, POST request

        Returns
        Get: template and HTTPResponse
        Get: json data and HTTPResponse
    """

    if request.method == 'GET':
        data = [row.serialize() for row in Sample.query.all()]        
        return render_template('api.html', title="page",jsonfile=json.dumps(data)), 200        

    elif request.method == 'POST':
        """
            Receives sample data file and insert top 10 of each sample into the database.                    
        """

        # check that file conforms to specifications:
        # - tab delimited
        # - has #chrom1, start1, end1, chrom2, end2, sample, score columns
                
        # The input file into curl is in data-binary which is sent to request.data
        sample_file_data = request.data

        # check format
        if request.content_type != 'text/xml':
            error = 'content type must be text/xml. Received {}'.format(request.content_type)
            return jsonify(msg='Error: {}. '.format(error)), 400                    
        
        if not sample_file_data:
            error = "No file input."
            return jsonify(msg='Error: {}. '.format(error)), 400
            
        if sample_file_data:
            df = pd.read_csv(StringIO(sample_file_data.decode('utf-8')), sep='\t')            

            # check non delimited tab
            # if we get NaN values, then we have a non tab delimited cell
            if df.isnull().values.any():                
                error = "Non delimited tabs exist."
                return jsonify(msg='Error: {}. '.format(error)), 400                
            
            # data cleaning - remove column leading and trailing whitespace
            df.rename(columns=lambda x: x.strip(), inplace=True)            

            # check required file attributes            
            # has #chrom1, start1, end1, chrom2, end2, sample, score columns
            # the sample file has 'start2'
            for col_name in ['#chrom1', 'start1', 'end1', 'chrom2', 'start1', 'end2', 'sample', 'score']:
                if col_name not in df.columns:                    
                    error = col_name
                    return jsonify(msg='Error: missing column {}.'.format(error)), 400
                    
            # data cleaning - remove str data leading and trailing whitespace
            df = df.applymap(lambda x: x.strip() if type(x) == str else x)
                                   
            # delete all rows of new samples to replace with new entries
            for new_sample in df['sample'].unique().tolist():                                
                Sample.query.filter_by(sample=new_sample).delete()
                db.session.commit()                            
                             
            # * get only top 10 lines per sample (with highest score) and save to a database.
            # * This also can be achieved by importing all the lines into the database and then outputting only latest top 10 entries per sample in the view.
            # Each sample has multiple entries in the file. 
            # Insert top 10 sample entries by score
            for curr_sample in df['sample'].unique().tolist():                
                top_10 = df.loc[df['sample']==curr_sample].sort_values(by=['score'], ascending=False).head(10)
                                
                for index, row in top_10.iterrows():
                                        
                    new_sample = Sample(
                        chrom1 = row['#chrom1'],
                        start1 = row['start1'],
                        end1 = row['end1'],
                        chrom2 = row['chrom2'],
                        start2 = row['start2'],
                        end2 = row['end2'],
                        sample = row['sample'],
                        score = row['score'],                    
                    )                    
                                  
                    try:
                        db.session.add(new_sample)                        
                    except AssertionError as e:
                        return jsonify(msg='Error: {}. '.format(e)), 400
                        
            db.session.commit()
        response_data = [row.serialize() for row in Sample.query.all()] 
        return jsonify(response_data), 201